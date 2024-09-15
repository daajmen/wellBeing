from datetime import datetime
import asyncio


async def check_time(time_input):
    while True:
        actualTime = datetime.now().strftime("%H:%M")
        if actualTime == time_input:
            return True
        return False
      
async def runscript(time_input, execute, phone):
    while True: 
        triggered = await check_time(time_input)
        if triggered: 
            print('tänd var det här')
            execute(phone)
            await asyncio.sleep(61)
        await asyncio.sleep(10)
