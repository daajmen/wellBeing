from utils.API_tools import *
from utils.websockets_module import * 
from utils.utils import *
from utils.database import init_db
import asyncio
from datetime import datetime

async def main():
    init_db()
    await listen_to_events()


async def run():
    await asyncio.gather(
        main(),
        runscript("06:30", NotifySleepWell, 'master'),

        runscript("09:00", NotifyFood, 'master'),
        runscript("11:00", NotifyFood, 'master'),
        runscript("16:00", NotifyFood, 'master'),

        runscript("16:30", NotifyWorkday, 'master'),

        runscript("21:00", NotifyGoodday, 'master')


    )

asyncio.run(run())

