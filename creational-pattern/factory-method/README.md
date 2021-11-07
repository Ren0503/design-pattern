# Factory Method

## Mục đích

**Factory method** là một design pattern thuộc nhóm Creational, nó cung cấp một interface để tạo đối tượng cho lớp cha (superclass), nhưng cũng cho phép các lớp con (subclass) thay đổi đối tượng sẽ được tạo.

![intent](./assets/intent.png)

## Vấn đề

Tưởng tượng bạn đang tạo một ứng dụng quản lý chuỗi cung ứng. Phiên bản đầu tiên của ứng dụng chỉ quản lý vận chuyển cho các xe tải, thế nên phần lớn code của bạn sẽ nằm trong lớp `Truck`. 

Sau đó ứng dụng của bạn ngày càng phổ biến và bạn nhận được yêu cầu từ các công ty hàng hải để hợp nhất chuỗi cung ứng qua đường biển vào ứng dụng. Đấy là một thông tin tuyệt vời! Nhưng còn code thì sao?

![problem](./assets/problem.png)
*Việc thêm một lớp mới vào ứng dụng không hề đơn giản nếu phần lớn code đã được kết nối với các lớp hiện có.*

Hiện tại hầu hết code của bạn đã được ghép với clas `Truck`. Việc thêm `Ship` vào ứng dụng sẽ yêu cầu các thay đổi với toàn bộ codebase. Và nếu bạn thêm một phương tiện vận tải nào vào ứng dụng, thì bạn sẽ thay đổi code lần nữa.

Kết quả là bạn có một đống code tạp nham với rất nhiều điều kiện thay đổi của ứng dụng tùy thuộc vào loại đối tượng vận chuyển.

## Giải pháp

