import logging
import threading
import time

# def thread_function(name):
#     logging.info("Thread %s: starting", name)
#     time.sleep(2)
#     logging.info("Thread %s: finishing", name)

# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO,
#                         datefmt="%H:%M:%S")

#     logging.info("Main    : before creating thread")
#     x = threading.Thread(target=thread_function, args=(1,))
#     logging.info("Main    : before running thread")
#     x.start()
#     logging.info("Main    : wait for the thread to finish")
#     logging.info("Main    : all done")

# def thread_function(name):
#     logging.info("Thread %s: starting", name)
#     time.sleep(2)
#     logging.info("Thread %s: finishing", name)

# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO,
#                         datefmt="%H:%M:%S")

#     logging.info("Main    : before creating thread")
#     x = threading.Thread(target=thread_function, args=(1,), daemon=True)
#     logging.info("Main    : before running thread")
#     x.start()
#     logging.info("Main    : wait for the thread to finish")
#     logging.info("Main    : all done")

# def thread_function(name):
#     logging.info("Thread %s: starting", name)
#     time.sleep(2)
#     logging.info("Thread %s: finishing", name)

# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO,
#                         datefmt="%H:%M:%S")

#     logging.info("Main    : before creating thread")
#     x = threading.Thread(target=thread_function, args=(1,), daemon=True)
#     logging.info("Main    : before running thread")
#     x.start()
#     logging.info("Main    : wait for the thread to finish")
#     x.join()
#     logging.info("Main    : all done")


# import logging
# import threading
# import time

# def thread_function(name):
#     logging.info("Thread %s: starting", name)
#     time.sleep(2)
#     logging.info("Thread %s: finishing", name)

# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO,
#                         datefmt="%H:%M:%S")

#     threads = list()
#     for index in range(3):
#         logging.info("Main    : create and start thread %d.", index)
#         x = threading.Thread(target=thread_function, args=(index,))
#         threads.append(x)
#         x.start()

#     for index, thread in enumerate(threads):
#         logging.info("Main    : before joining thread %d.", index)
#         thread.join()
#         logging.info("Main    : thread %d done", index)




# import concurrent.futures
# def thread_function(name):
#     logging.info("Thread %s: starting", name)
#     time.sleep(2)
#     logging.info("Thread %s: finishing", name)

# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO,
#                         datefmt="%H:%M:%S")

#     with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
#         executor.map(thread_function, range(3))

# counter = 0

# def increment():
#     global counter
#     for _ in range(100000):
#         counter += 1
# import threading
# counter = 0
# def increment():
#     global counter
#     for _ in range(1000000):
#         counter += 1
# threads = []
# for i in range(5):  
#     t = threading.Thread(target=increment)
#     threads.append(t)
#     t.start()
# for t in threads:
#     t.join()
# print("Expected counter = ", 500000)
# print("Actual counter   =", counter)

# import threading

# l = threading.Lock()
# print("before first acquire")
# l.acquire()
# print("before second acquire")
# l.acquire()
# print("acquired lock twice")

# import time
# import threading
# def square(numbers):
#     print("caculate square of numbers")
#     for x in numbers:
#         time.sleep(1)
#         print("Square: ", x*x);
# def cube(numbers):
#     print("caculate square of numbers")
#     for x in numbers:
#         time.sleep(1)
#         print("Cube: ", x*x*x);
# arr=[1,3,5,7,9];
# t=time.time()
# thread1 = threading.Thread(target=square, args=(arr,))
# thread2 = threading.Thread(target=cube, args=(arr,))
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print("Time taken: ",time.time()-t)


import concurrent.futures
# def sum_exponent(list,name):
#     sum = 0
#     for x in list:
#         sum += x**x
#     # print(f"Sum of squares: {sum}")
#     print(f"Thread {name} finished")
#     return sum

# myList = [x for x in range(1,101)]

# with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
# .submit() : chỉ cho phép 1 worker làm việc. Mỗi worker sẽ nhận một task và thực hiện nó.
    # for i in range(5):
    #     executor.submit(sum_exponent,myList)
    # futures = [executor.submit(sum_exponent,myList,i) for i in range(15)] # 1 đối tượng mà sẽ chứa kết quả trả về của hàm sum_exponent
    # for future in concurrent.futures.as_completed(futures): 
    #     print(future.result())
    # khi thực hiện xong as_completed thì nó ms in ra dc kết quả mà futures = [executor.submit(sum_exponent,myList) for i in range(5)] mà xét thứ tự submit 0,1,2,3,4 (không phải là thứ tự hoàn thành mà có thể thằng này chạy trước thằng kia)
    # for future in futures:
    #     print(future.result())
# .submit() sẽ trả về một đối tượng Future, nó sẽ chứa kết quả trả về của hàm sum_exponent

# .map()
def sum_exponent(list):
    sum = 0
    for x in list:
        sum += x**x
    # print(f"Sum of squares: {sum}")
    print(f"Thread finished")
    return sum

myList = [x for x in range(1,101)]
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    # executor.map(sum_exponent,[myList,myList,myList]) # sẽ trả về một iterator, nó sẽ trả về kết quả của hàm sum_exponent theo thứ tự của myList
    results = executor.map(sum_exponent,[myList,myList,myList])
    for result in results:
        print(result) # sẽ in ra kết quả của hàm sum_exponent theo thứ tự của myList