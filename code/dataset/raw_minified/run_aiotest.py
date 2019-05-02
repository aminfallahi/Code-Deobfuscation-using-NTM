import aiotest.run,asyncio as B,sys
if sys.platform=='win32':from asyncio.windows_utils import socketpair
else:from socket import socketpair
A=aiotest.TestConfig()
A.asyncio=B
A.socketpair=socketpair
A.new_event_pool_policy=B.DefaultEventLoopPolicy
A.call_soon_check_closed=True
aiotest.run.main(A)