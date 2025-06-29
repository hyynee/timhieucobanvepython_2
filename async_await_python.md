Bất đồng bộ (asynchronous) là: Một cách tổ chức chương trình để không bị chặn khi chờ một tác vụ mất thời gian — ví dụ như gọi API, chờ phản hồi từ database, hoặc đọc file.
Ví dụ: Gọi món trong quán ăn ==> order ; làm việc khác trong lúc chờ ; nhận kết quả khi món ăn sẵn sàng
# async await là xử lý bất đồng bộ (nó chạy song song về mặt logic)

Ví dụ:
import asyncio
async def task(name, delay):
    print(f"Start {name}")
    await asyncio.sleep(delay)
    print(f"End {name}")
async def main():
    await asyncio.gather(
        task("A", 2),
        task("B", 3),
        task("C", 1),
    )
asyncio.run(main())
==> Tất cả bắt đầu cùng lúc.Task nào xong sớm thì kết thúc sớm. Hoàn thành trong vòng 3s chứ k phải (2+1+3 = 6s)

# Coroutine (đồng trình) là: Một hàm có thể tạm dừng (pause) và tiếp tục (resume) lại sau đó. Được khai báo bằng:  async def
Ví dụ:
async def say_hello():
    print("Hello")

coro = say_hello()
print(coro)  
await say_hello()  

# EXP: coroutine song song với asyncio.gather()
async def greet(name, delay):
    await asyncio.sleep(delay)
    print(f"Hi {name}")

async def main():
    await asyncio.gather(
        greet("Alice", 1),
        greet("Bob", 2),
    )

asyncio.run(main())
==> Hai coroutine được chạy song song về mặt logic, thời gian tổng = task lâu nhất.

