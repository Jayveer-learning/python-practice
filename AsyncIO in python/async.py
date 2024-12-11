# Asynchronous Programmer

# import asyncio library for async/ await code

# keywords async and await 

# async define asynchronous function 
# await is used to call asynchronous function (i.e,, 
# pause the axecution until the awaited task id 
# completed). 

import asyncio
import time
# async def greet():
#     print("Start")
#     await asyncio.sleep(1) # simulates an asynchronous I/O task
#     print("End")

# asyncio.run(greet()) # runs the asynchronous function
# output:- 
# Start
# wait 1 second then execute the last print
# End

# async def task1():
#     await asyncio.sleep(2)
#     print("Task 1 finished")

# async def task2():
#     await asyncio.sleep(1)
#     print("Task 2 finished")


# async def main():
#     task_1 = asyncio.create_task(task1())
#     task_2 = asyncio.create_task(task2())

#     await task_1
#     await task_2

# asyncio.run(main())

# await 1 second and then execite the task2
# Task 2 finished
# then complete 2 second the execute the task1
# Task 1 finished

# gather :

# async def fetch_data(delay, data):
#     await asyncio.sleep(delay)
#     return data 

# async def main():
#     result = await asyncio.gather(
#         fetch_data(1, "data1"),
#         fetch_data(2, "data1"),
#         fetch_data(3, "data1")
#     )
#     print(result)

# asyncio.run(main())

# ['data1', 'data1', 'data1'] wait total 3s and then
# return the data
