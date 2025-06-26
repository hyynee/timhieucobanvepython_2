# Threading trong python: (giải quyết I/O-bound)
- Luồng là một luồng thực thi riêng biệt. Điều này có nghĩa là chương trình của bạn sẽ có hai việc (hoặc nhiều việc) xảy ra cùng một lúc.
- Luồng Python cho phép bạn chạy đồng thời nhiều phần khác nhau của chương trình và có thể đơn giản hóa thiết kế của bạn.
- Các luồng có thể chạy trên các bộ xử lý khác nhau, nhưng chúng sẽ chỉ chạy một bộ xử lý tại một thời điểm.
- Sử dụng luồng trong chúng giúp thiết kế sạch hơn và dễ lý giải hơn.

Ví dụ: 
Để bắt đầu một luồng riêng biệt, bạn tạo một Thread thể hiện và sau đó yêu cầu nó .start():

import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    # x.join()
    logging.info("Main    : all done")

$ ./single_thread.py
Main    : before creating thread
Main    : before running thread
Thread 1: starting
Main    : wait for the thread to finish
Main    : all done
Thread 1: finishing


# Daemon Threads : là một tiến trình chạy ẩn
- Một luồng daemon  sẽ tắt ngay lập tức khi chương trình thoát (exit())
- là một luồng chạy trong nền mà không cần lo lắng về việc tắt nó.
- các daemon sẽ bị giết bất cứ nơi nào chúng đang ở khi chương trình thoát.
def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,), daemon=True)
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    # x.join()
    logging.info("Main    : all done")

$ ./daemon_thread.py
Main    : before creating thread
Main    : before running thread
Thread 1: starting
Main    : wait for the thread to finish
Main    : all done

==> Sự khác biệt ở đây là dòng cuối cùng của đầu ra bị thiếu. thread_function() không có cơ hội hoàn thành.Đó là một daemon luồng, vì vậy khi __main__đến cuối mã của nó và chương trình muốn hoàn thành, daemon đã bị tắt


# join(): Để yêu cầu một luồng chờ luồng khác hoàn tất, gọi .join()
- Nếu .join() là luồng, câu lệnh đó sẽ đợi cho đến khi một trong hai loại luồng hoàn tất.
- Nếu k gọi join() thì thread daemon có thể không hoàn thành công việc.
Ví dụ:
def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,), daemon=True)
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    x.join()
    logging.info("Main    : all done")

# Làm việc với nhiều luồng:
import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    threads = list()
    for index in range(3):
        logging.info("Main    : create and start thread %d.", index)
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)
==> OUTPUT LẦN 1:
09:17:56: Main    : create and start thread 0.
09:17:56: Thread 0: starting
09:17:56: Main    : create and start thread 1.
09:17:56: Thread 1: starting
09:17:56: Main    : create and start thread 2.
09:17:56: Thread 2: starting
09:17:56: Main    : before joining thread 0.  
09:17:58: Thread 0: finishing
09:17:58: Thread 1: finishing
09:17:58: Thread 2: finishing
09:17:58: Main    : thread 0 done
09:17:58: Main    : before joining thread 1.      
09:17:58: Main    : thread 1 done
09:17:58: Main    : before joining thread 2.      
09:17:58: Main    : thread 2 done
==> OUTPUT LẦN 2:
09:17:56: Main    : create and start thread 0.
09:17:56: Thread 0: starting
09:17:56: Main    : create and start thread 1.
09:17:56: Thread 1: starting
09:17:56: Main    : create and start thread 2.
09:17:56: Thread 2: starting
09:17:56: Main    : before joining thread 0.  
09:17:58: Thread 1: finishing
09:17:58: Thread 0: finishing
09:17:58: Thread 2: finishing
09:17:58: Main    : thread 0 done
09:17:58: Main    : before joining thread 1.      
09:17:58: Main    : thread 1 done
09:17:58: Main    : before joining thread 2.      
09:17:58: Main    : thread 2 done

==> Thứ tự chạy các luồng được xác định bởi hệ điều hành và có thể khá khó để dự đoán. Nó có thể (và có khả năng sẽ) thay đổi tùy theo từng lần chạy, vì vậy bạn cần lưu ý điều đó khi thiết kế các thuật toán sử dụng luồng.

Vì vậy để quản lý nhóm luồng 1 cách hiệu quả:
+ ThreadPoolExecutor (là 1 thư viện chuẩn của  concurrent.futures kể từ python 3.2 trở lên): Cách dễ nhất để tạo ra nó là sử dụng trình quản lý ngữ cảnh, sử dụng with: câu lệnh để quản lý việc tạo và hủy nhóm.
Ví dụ:
import concurrent.futures

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(thread_function, range(3))
==>OUT PUT: 
09:25:04: Thread 0: starting
09:25:04: Thread 1: starting
09:25:04: Thread 2: starting
09:25:06: Thread 1: finishing
09:25:06: Thread 2: finishing
09:25:06: Thread 0: finishing
==>  ThreadPoolExecutor: trình quản lý ngữ cảnh, cho nó biết có bao nhiêu luồng mà nó muốn trong nhóm;
.map() sẽ block cho đến khi tất cả task hoàn tất;
Nên sử dụng nhưThreadPoolExecutor một trình quản lý ngữ cảnh khi có thể để không bao giờ quên .join()các luồng.
Lưu ý: Sử dụng a ThreadPoolExecutorcó thể gây ra một số lỗi khó hiểu.
Ví dụ, nếu bạn gọi một hàm không có tham số nhưng lại truyền tham số vào nó .map(), thì luồng sẽ đưa ra một ngoại lệ.
Thật không may, ThreadPoolExecutorsẽ ẩn ngoại lệ đó và (trong trường hợp trên) chương trình kết thúc mà không có đầu ra. Điều này có thể khá khó hiểu khi gỡ lỗi lúc đầu.
Ví dụ tiếp theo:
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

# Race condition: có thể xảy ra khi hai hoặc nhiều luồng truy cập vào một phần dữ liệu hoặc tài nguyên được chia sẻ, race condition sẽ xảy ra mọi lúc
counter = 0
def increment():
    global counter
    for _ in range(100000):
        counter += 1
==> Nhiều thread gọi increment() có thể gây sai lệch dữ liệu.

# Cách giải quyết vấn đề này: Sử dụng Lock
Lock : chỉ cho phép một luồng tại một thời điểm vào phần đọc-sửa-ghi của mã của bạn. Bất kỳ luồng nào khác muốn Lock phải đợi cho đến khi chủ sở hữu của Lock nó từ bỏ nó.
Ví dụ:
lock = threading.Lock()
def safe_increment():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1
luồng chạy hàm này sẽ giữ nguyên Lock cho đến khi hoàn tất việc cập nhật cơ sở dữ liệu. Trong trường hợp này, điều đó có nghĩa là nó sẽ giữ Lock trong khi sao chép, cập nhật, ngủ và sau đó ghi giá trị trở lại cơ sở dữ liệu.

# Dead Lock
Ví dụ:
import threading
l = threading.Lock()
print("before first acquire")
l.acquire()
print("before second acquire")
l.acquire()
print("acquired lock twice")
==> chương trình treo chờ được giải phóng.
Dealock thường xảy ra do 1 trong 2 điều sau:
- Một lỗi triển khai Lockkhông được phát hành đúng cách
- Một vấn đề thiết kế trong đó một hàm tiện ích cần được gọi bởi các hàm có thể đã hoặc chưa có Lock

ĐỂ GIẢI QUYẾT VẤN ĐỀ NÀY THÌ Python có 1 đối tượng gọi là Rlock. Rlock cho phép một luồng thực hiện .acquire()nhiều RLock lần trước khi gọi .release(). Luồng đó vẫn được yêu cầu gọi .release()cùng số lần như đã gọi .acquire()
==> Lock và RLock là hai trong số các công cụ cơ bản được sử dụng trong lập trình luồng để ngăn chặn tình trạng race condition

