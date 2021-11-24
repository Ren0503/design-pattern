# Iterator

## 📜 Mục đích

Iterator là một design pattern thuộc nhóm behavioral giúp bạn duyệt phần tử của một tập hợp mà không để lộ dạng cơ bản của nó (danh sách, ngăn xếp, cây, ...)

![intent](,/assets/intent.png)

## 😟 Vấn đề

Collection(tập hợp) là một trong những kiểu dữ liệu được sử dụng nhiều nhất trong lập trình. Hiểu đơn giản nó chỉ là nơi chứa cho một nhóm đối tượng.

![problem1](./assets/problem1.png)

Phần lớn tập hợp lưu trữ phần tử của nó bằng danh sách đơn giản. Tuy nhiên một số lại sử dụng ngăn xếp, cây, đồ thị hoặc một cấu trúc dữ liệu phức tạp nào khác.

Nhưng việc tập hợp được tạo như thế nào không quan trọng, nó chỉ cần cung cấp một số cách để truy cập phần tử của nó cho các đoạn code khác có thể dùng cho phần tử đấy. Nên có một cách để duyệt qua từng phần tử của tập hợp mà không truy cập trùng lại phần tử nào đấy.

Điều này nghe có vẻ dễ dàng nếu bạn có một tập hợp dựa trên danh sách. Bạn chỉ cần lặp lại tất cả phần tử, nhưng nếu nó là một cấu trúc dữ liệu phức tạp khác như cây thì sao? Ví dụ, hôm nay bạn chỉ thực hiện duyệt cây theo chiều sâu(depth-first traversal), nhưng ngày hôm sau bạn lại nhận yêu cầu là cần thêm tìm kiếm theo chiều rộng(breadth-first traversal), và các ngày kế tiếp bạn phải thực hiện các công việc khác như truy cập ngẫu nhiên ba phần tử,...

![problem2](./assets/problem2.png)

*Một tập hợp có thể duyệt theo nhiều cách*

Việc thêm nhiều thuật toán duyệt vào tập hợp có thể làm mờ đi nhiệm vụ chính của nó, là lưu trữ dữ liệu hiệu quả. Thêm vào đó, một vài thuật toán chỉ phù hợp với vài ứng dụng cơ bản, thể nên thêm nó vào lớp tập hợp chung có thể sẽ không phù hợp.

Mặt khác, code cliend làm việc với nhiều tập hợp khác nhau sẽ không quan tâm đến chúng lưu trữ phần tử như thế nào. Tuy nhiên, vì tập hợp cung cấp các cách khác nhau để truy cập phần tử, nên bạn không có lựa chọn nào khác ngoài kết hợp code của bạn với lớp tập hợp cụ thể.

## 😊 Giải pháp

Ý tượng ở đây là mở rộng hành vi duyệt của một tập hợp thành một đối tượng riêng biệt gọi là *iterator*.

![solution](./assets/solution.png)

Ngoài việc triển khai thuật toán chính, một đối tượng iterator còn đóng gói tất cả các chi tiết duyệt, chẳng hạn như vị trí hiện tại và số phần tử còn lại cho đến cuối. Do đó, một số iterator có thể đi qua cùng một tập hợp cùng một lúc, độc lập với nhau.

Thông thường, các iterator cung cấp một phương thức chính để tìm nạp các phần tử của tập hợp. Client có thể tiếp tục chạy phương thức này cho đến khi nó không trả về bất kỳ thứ gì, có nghĩa là iterator đã duyệt qua tất cả các phần tử.

Tất cả các iterator phải triển khai cùng một interface. Điều này làm cho code client tương thích với bất kỳ loại tập hợp nào hoặc bất kỳ thuật toán duyệt nào miễn là có một iterator thích hợp. Nếu bạn cần một cách đặc biệt để duyệt qua một tập hợp, bạn chỉ cần tạo một lớp iterator mới mà không cần phải thay đổi tập hợp hoặc ứng dụng client.