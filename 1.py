import asyncio
from loguru import logger
async def sink(message):
    await asyncio.sleep(2)  # IO processing...
    print('1212', end="")
    # logger.info("Start")

async def work():
    # logger.info("Start")
    logger.info("End")
    await logger.complete()

logger.add(sink)

asyncio.run(work())
