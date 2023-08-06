import asyncio
import concurrent.futures

import nest_asyncio


def sig_get(hub) -> asyncio.AbstractEventLoop:
    ...


def post_get(hub, ctx):
    loop = ctx.ret
    if isinstance(loop, asyncio.BaseEventLoop):
        nest_asyncio.apply(loop)
    return loop


def sig_policy(hub) -> asyncio.AbstractEventLoopPolicy:
    ...


def sig_executor(hub) -> concurrent.futures.Executor:
    ...


def post_executor(hub, ctx):
    """
    Provide a default if no executor was given
    """
    if ctx.ret is None:
        return concurrent.futures.ThreadPoolExecutor()
    else:
        return ctx.ret
