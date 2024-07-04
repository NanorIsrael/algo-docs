import asyncio

async def main():
    name = 'Hello ...'
    for char in name:
        print(char, end='', flush=True)
        await asyncio.sleep(0.5)
    print()

if __name__ == '__main__':
    asyncio.run(main())
