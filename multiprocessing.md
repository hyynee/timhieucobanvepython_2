# Process (tiến trình) là một chương trình độc lập có bộ nhớ và tài nguyên riêng.
# Multiprocessing là kỹ thuật chạy nhiều process song song → mỗi process là một bản sao độc lập của Python interpreter → tránh GIL (Global Interpreter Lock).
Dùng để xử lý CPU-bound tasks như xử lý ảnh, tính toán nặng, AI/ML...
| Threading           | Multiprocessing             |
| Dùng chung bộ nhớ   | Tách biệt bộ nhớ            |
| Bị giới hạn bởi GIL | Không bị giới hạn bởi GIL   |
| Tốt cho I/O-bound   | Tốt cho CPU-bound           |
| Nhanh khởi tạo hơn  | Tốn thời gian và bộ nhớ hơn |

Ví dụ:
import time
import multiprocessing
def add_199_to_value(number):
    time.sleep(0.1)  
    number += 199
    print(f"Processed number: {number}")
    return number
# add_199_to_value(1)
if __name__ == '__main__':
    my_process = multiprocessing.Process(target=add_199_to_value, args=(1,))
    my_process.start()
    my_process.join()  
    my_process2 = multiprocessing.Process(target=add_199_to_value, args=(111,))
    my_process2.start()
    my_process2.join()
# mỗi process sẽ dùng 1 trình biên dịch riêng, bộ nhớ riêng
#Mỗi Process là một Python interpreter riêng.
#Không chia sẻ biến toàn cục (global) giữa các process.
#Sử dụng .start() để chạy, .join() để đợi hoàn thành.

Dùng Pool để quản lý process tự động (from multiprocessing import Pool)
def f(x):
    return x*x
if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))

 # multiprocessing hỗ trợ ba cách để bắt đầu một quy trình. Các phương pháp bắt đầu này là:
- spawn : Tạo process mới hoàn toàn; Code chạy trong process con sẽ kế thừa những tài nguyên cần thiết để chạy run(); Không kế thừa tài nguyên như socket, file descriptor
Ví Dụ:
from multiprocessing import get_context
import time

def worker():
    print("Spawned process started")
    time.sleep(1)
    print("Done")

if __name__ == "__main__":
    ctx = get_context("spawn")
    p = ctx.Process(target=worker)
    p.start()
    p.join()
- fork (coppy): tiến trình con; Tất cả tài nguyên của tiến trình cha được tiến trình con kế thừa (Kế thừa tất cả biến, file, socket, lock… mà k cần khởi động lại)
Ví dụ:
from multiprocessing import get_context
def worker():
    print("Forked process running")
if __name__ == "__main__":
    ctx = get_context("fork")
    p = ctx.Process(target=worker)
    p.start()
    p.join()

- forkserver: để yêu cầu tạo process mới. Từ đó trở đi, bất cứ khi nào cần một tiến trình mới, tiến trình cha sẽ kết nối với máy chủ và yêu cầu nó phân nhánh một tiến trình mới. Tiến trình máy chủ phân nhánh là luồng đơn trừ khi các thư viện hệ thống hoặc các bản nhập được tải trước sinh ra các luồng như một tác dụng phụ nên nhìn chung là an toàn khi sử dụng os.fork(). Không có tài nguyên không cần thiết nào được kế thừa.
Ví dụ:
import multiprocessing
def worker():
    print("Forkserver process")
if __name__ == "__main__":
    multiprocessing.set_start_method("forkserver")
    p = multiprocessing.Process(target=worker)
    p.start()
    p.join()





# Trao đổi các đối tượng giữa các tiến trình
- Queue:
ví dụ:
from multiprocessing import Process, Queue
def f(q):
    q.put([42, None, 'hello'])
if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())    # prints "[42, None, 'hello']"
    p.join()
Hàng đợi an toàn với luồng và quy trình. Bất kỳ đối tượng nào được đưa vào multiprocessinghàng đợi sẽ được tuần tự hóa (làm theo thứ tự)
- Pipe : trả về một cặp đối tượng kết nối được kết nối bằng một đường ống mà theo mặc định là song song (hai chiều)




# 1-Value, 2-Array trong multiprocessing thì mới có thể trao đổi được dữ liệu với nhau
Ví dụ: Value
import time
import multiprocessing
import concurrent.futures
ORIGIN_VALUE = multiprocessing.Value('i', 0)
def add_199_to_value(number):
    time.sleep(0.1)  
    number.value += 199
    ORIGIN_VALUE = number.value
    print(f"Processed number: {number.value}")
    return number.value
def doit():
    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     [executor.submit(add_199_to_value, ORIGIN_VALUE) for _ in range(5)]
        
if __name__ == '__main__':
    doit()
    print(f'final: {ORIGIN_VALUE.value}')
Ví dụ 2: Array : 
import time
import multiprocessing
import concurrent.futures
# multiprocessing.Array cho phép chia sẻ dữ liệu giữa các process.
list_to_square = multiprocessing.Array('i', [1, 2, 3, 4, 5])  
def square_element(list):
    time.sleep(0.1)
    for i in range (len(list)):
        list[i] = list[i] * list[i]
    print(f"Processed list: {list[:]}") # cú pháp bắt buộc
    return list
def doit():
    p1 = multiprocessing.Process(target=square_element, args=(list_to_square,))
    p1.start()
    p1.join() 
if __name__ == '__main__':
    doit()
    print(f"Main process list: {list_to_square[:]}")