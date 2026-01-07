import asyncio
from bot import Bot

async def main():
    bot = Bot()
    await bot.start()
    await asyncio.Event().wait()  # process ko zinda rakhega

if __name__ == "__main__":
    asyncio.run(main())
import time
while True:
    time.sleep(10)
