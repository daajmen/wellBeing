from utils.API_tools import *
from utils.websockets_module import * 
import asyncio

async def main():
    await listen_to_events()

# Skicka fråga 
NotifySleepWell('master')
NotifyFood('master')
NotifyWorkday('master')


asyncio.run(main())

