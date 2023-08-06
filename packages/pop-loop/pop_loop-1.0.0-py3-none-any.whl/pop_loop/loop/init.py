import asyncio
import concurrent.futures

import sniffio


def __init__(hub):
    hub.loop.init.BACKEND = None


def get(hub) -> asyncio.AbstractEventLoop:
    """
    Reliably get an active loop
    """
    if hub.pop.loop.POLICY:
        asyncio.set_event_loop_policy(hub.pop.loop.POLICY)
    loop = None
    if hub.pop.loop.CURRENT_LOOP is None:
        if hub.loop.init.BACKEND and hub.loop.init.BACKEND != "init":
            loop = hub.loop[hub.loop.init.BACKEND].get()
        else:
            loop = asyncio.get_event_loop()
    elif hub.pop.loop.CURRENT_LOOP.is_closed():
        # Create a new loop with the same policy
        loop = asyncio.new_event_loop()

    if loop:
        # If there was a change in loop
        asyncio.set_event_loop(loop)
        hub.pop.loop.CURRENT_LOOP = loop
    return hub.pop.loop.CURRENT_LOOP


def policy(hub):
    if hub.loop.init.BACKEND:
        return hub.loop[hub.loop.init.BACKEND].policy()
    return asyncio.DefaultEventLoopPolicy()


def executor(hub):
    if hub.loop.init.BACKEND:
        return hub.loop[hub.loop.init.BACKEND].executor()
    return concurrent.futures.ThreadPoolExecutor(thread_name_prefix="pop-loop-init")


def create(hub, loop_plugin: str = None):
    """
    Create the event loop with the named plugin

    :param hub:
    :param loop_plugin: The pop-loop plugin to use for the async loop backend
    """
    # Automatically determine which backend to use
    if loop_plugin:
        loop_backend = loop_plugin
    elif "uv" in hub.loop._loaded:
        loop_backend = "uv"
    elif "trio" in hub.loop._loaded:
        loop_backend = "trio"
    elif "proactor" in hub.loop._loaded:
        loop_backend = "proactor"
    elif "selector" in hub.loop._loaded:
        loop_backend = "selector"
    else:
        loop_backend = "init"

    # Use the named plugin to set up the loop
    hub.pop.loop.POLICY = hub.loop[loop_backend].policy()
    hub.pop.loop.CURRENT_LOOP = hub.loop[loop_backend].get()
    hub.pop.loop.EXECUTOR = hub.loop[loop_backend].executor()
    hub.loop.init.BACKEND = loop_backend


def backend(hub) -> str:
    """
    Determine the async library backend for the current loop
    """

    async def _backend():
        # An asynchronous context for sniffio to use
        return sniffio.current_async_library()

    try:
        # Run the sniffio function with the current loop
        return hub.pop.Loop.run_until_complete(_backend())
    except Exception as e:
        hub.log.debug(f"Unable to detect aio backend: {e}")
        return "unknown"
