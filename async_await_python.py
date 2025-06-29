# import asyncio

# async def say_hello(): # định nghĩa một coroutine function.
#     print("Hello")

# async def main():
#     # Khi gọi say_hello(), nó không chạy liền — nó trả về một coroutine object.
#     # Để chạy coroutine, chúng ta cần sử dụng await.
#     # await sẽ tạm dừng hàm main cho đến khi say_hello hoàn thành.
#     await say_hello() 
#     # await cũng cho phép tạm dừng coroutine đang chạy, để hệ thống chạy cái khác → bất đồng bộ hiệu quả hơn
# if __name__ == "__main__":
#     asyncio.run(main())



# import asyncio
# import threading
# async def counter():
#     print('ONE')
#     await asyncio.sleep(3);
#     print('TWO')

# async def sayhi():
#     print('Hi')
#     await asyncio.sleep(1)
# async def hello():
#     print('Hello')
# async def main():
#     # await counter()
#     # await counter()
#     # await counter()
#     # tổng 9s

#     print(f'Thread is running: {threading.current_thread().name}')

#     await asyncio.gather(
#         counter(),
#         sayhi(),
#         counter(),
#         hello(),
#         counter(),
#     )
#     #  await counter() sẽ chạy 3 lần, nhưng không chờ đợi nhau, vì vậy tổng thời gian chỉ là 3 giây.
# asyncio.run(main())


import asyncio
async def add_number(a,b):
    print(f"Add function: {a+b}")

async def subs_number(a,b):
    print(f"Subtract function: {a-b}")

async def mul_number(a,b):
    print(f'Multiply function: {a*b}')
async def divide_number(a,b):
    print(f'Divide function: {a/b}')

async def main(): 
    await add_number(1,2)
    await subs_number(3,1)
    await mul_number(2,3)
    await divide_number(10,2)


# Chương trình sẽ báo lỗi vì asyncio.run chỉ nhận một coroutine.
# asyncio.run(add_number(1,2), subs_number(3,1)) 
asyncio.run(main())


