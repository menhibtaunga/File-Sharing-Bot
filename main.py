import asyncio
from bot import Bot

async def main():
    bot = Bot()
    await bot.start()
    await asyncio.Event().wait()  # bot ko zinda rakhega

if __name__ == "__main__":
    asyncio.run(main())
