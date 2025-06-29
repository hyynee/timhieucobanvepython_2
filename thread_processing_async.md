công việc 1: 3s
công việc 2: 5s
công việc 3: 7s
---
   -----    
        -------
--------------- : tổng thời gian thực hiện (lập trình tuần tự)

# MultiThreading/Thread: concurrent.futures.ThreadPoolExecutor : tạo luồng dữ liệu riêng để chạy đồng thời: nên tổng thời gian có thể bằng tổng thằng chạy lâu nhất
---
-----
-------
------- : tổng thời gian thực hiện (có thể bị lệnh một xíu khi bắt đầu chạy)

# Async: bất đồng bộ : chạy trên 1 thread và 1 core CPU
------
  ----------
    --------------
# đang chạy thằng cv1 chưa xong có thể chạy luôn cv2 ...


# chạy đồng thời và chạy song song
# đồng thời: (chuyển đổi qua lại nhiều tác vụ)
Là khả năng của chương trình xử lý nhiều tác vụ cùng lúc về mặt logic, nhưng không nhất thiết là cùng lúc về mặt vật lý (CPU chỉ làm một việc tại một thời điểm, nhưng chuyển đổi giữa các tác vụ rất nhanh).
Ví dụ:
Một đầu bếp nấu ăn và đang nấu cả canh và chiên trứng. Trong lúc chờ canh sôi, đầu bếp chuyển sang chiên trứng → chuyển đổi liên tục giữa các nhiệm vụ.
- thread hoặc asyncio

# song song:
Là khi nhiều tác vụ được thực thi thực sự cùng một lúc, bằng cách chạy trên nhiều CPU / core khác nhau.
Ví dụ:
Có 2 đầu bếp, một người nấu canh, người kia chiên trứng → hai người làm việc cùng lúc thật sự.
- multiprocess để tận dụng cpu