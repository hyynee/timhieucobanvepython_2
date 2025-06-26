# GIL: Global Interpreter Lock

Khóa thông dịch toàn cục Python (GIL) hoạt động như một khóa đặc biệt chỉ cho phép một luồng chạy mã Python tại một thời điểm. Nó hoạt động giống như một semaphore nhị phân (mutex) bằng cách cấp quyền truy cập độc quyền vào trình thông dịch cho một luồng trong khi các luồng khác phải chờ.

Điều này có nghĩa là ngay cả trong kiến ​​trúc đa luồng, chỉ có một luồng có thể ở trạng thái thực thi tại bất kỳ thời điểm nào.

GIL có thể là nút thắt về hiệu suất trong mã liên quan đến CPU và đa luồng, nhưng nó không ảnh hưởng đến các chương trình luồng đơn.


GIL giúp giải quyết các vấn đề quản lý bộ nhớ trong CPython bằng cách ngăn chặn tình trạng chạy đua.
Nó đảm bảo rằng chỉ có một luồng thực thi mã byte Python tại một thời điểm, bảo vệ biến số đếm tham chiếu khỏi bị nhiều luồng sửa đổi không nhất quán. Điều này ngăn ngừa rò rỉ bộ nhớ và sự cố có thể xảy ra nếu số đếm tham chiếu không được duy trì chính xác.

# Cách xử lý GIL: Multi-processing vs multi-threading

# MULTI THREADING: đa luồng (chạy đồng thời)
Ví dụ : 1 ng mẹ có công việc chính là nấu ăn; 2 luồng phụ (thread) là trông con và nghe điện thoại.
(công việc nấu ăn vẫn được tiếp tục, tới khi các thread kết thúc và ng mẹ sẽ tiếp tục với công việc nấu ăn)
import time
import threading
def square(numbers):
    print("caculate square of numbers")
    for x in numbers:
        time.sleep(1)
        print("Square: ", x*x);
def cube(numbers):
    print("caculate cube of numbers")
    for x in numbers:
        time.sleep(1)
        print("Cube: ", x*x*x);
arr=[1,3,5,7,9];
t=time.time()
thread1 = threading.Thread(target=square, args=(arr,))
thread2 = threading.Thread(target=cube, args=(arr,))
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Time taken: ",time.time()-t)