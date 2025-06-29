# import time
# import multiprocessing


# def add_199_to_value(number):
#     time.sleep(0.1)  
#     number += 199
#     print(f"Processed number: {number}")
#     return number

# # add_199_to_value(1)

# if __name__ == '__main__':
#     my_process = multiprocessing.Process(target=add_199_to_value, args=(1,))
#     my_process.start()
#     my_process.join()  
#     my_process2 = multiprocessing.Process(target=add_199_to_value, args=(111,))
#     my_process2.start()
#     my_process2.join()  
# mỗi process sẽ dùng 1 trình biên dịch riêng, bộ nhớ riêng
#Mỗi Process là một Python interpreter riêng.
#Không chia sẻ biến toàn cục (global) giữa các process.
#Sử dụng .start() để chạy, .join() để đợi hoàn thành.


# from multiprocessing import get_context
# import time

# def worker():
#     print("Spawned process started")
#     time.sleep(1)
#     print("Done")

# if __name__ == "__main__":
#     ctx = get_context("spawn")
#     p = ctx.Process(target=worker)
#     p.start()
#     p.join()


import time
import multiprocessing
import concurrent.futures

list_to_square = multiprocessing.Array('i', [1, 2, 3, 4, 5])
ORIGIN_VALUE = multiprocessing.Value('i', 0)
def add_199_to_value(number):
    time.sleep(0.1)  
    number.value += 199
    ORIGIN_VALUE = number.value
    print(f"Processed number: {number.value}")
    return number.value
def square_element(list):
    time.sleep(0.1)
    for i in range (len(list)):
        list[i] = list[i] * list[i]
    print(f"Processed list: {list[:]}") # cú pháp bắt buộc
    return list
def doit():
    p1 = multiprocessing.Process(target=add_199_to_value, args=(ORIGIN_VALUE,))
    p1.start()
    p1.join() 
    p2 = multiprocessing.Process(target=square_element, args=(list_to_square,))
    p2.start()
    p2.join() 
        
if __name__ == '__main__':
    doit()
    print(f"Origin value: {ORIGIN_VALUE.value}")
    print(f"Main process list: {list_to_square[:]}")

