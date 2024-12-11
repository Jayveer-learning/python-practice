import asyncio

# async def main():
#     print("Hello")

# asyncio.run(main())

async def say_hello():
    print("Hello")
    await asyncio.sleep(10) # Non-blocking sleep for 1 second
    print("World")

asyncio.run(say_hello())
