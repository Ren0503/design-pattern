# Chain of Responsibility

## 📜 Mục đích

**Chain of Responsibility** là một design pattern trong nhóm behavioral cho phép bạn truyền các yêu cầu dọc theo một chuỗi xử lý. Khi nhận được yêu cầu, mỗi trình xử lý sẽ quyết định xử lý yêu cầu hoặc truyền nó cho trình xử lý tiếp theo trong chuỗi.

## 😟 Vấn đề

Tưởng tượng bạn đang làm việc với hệ thống đặt hàng trực tuyến. Bạn muốn giới hạn truy cập đến hệ thống để chỉ những người dùng đã xác thực mới có thể đặt đơn hàng. Còn người quản trị viên (admin) có thể truy cập đến tất cả đơn hàng.

Sau khi lên kế hoạch, bạn nhận ra là các trình kiểm tra(check) phải làm việc liên tục. Vì ứng dụng có thể phải xác thực người dùng bất cứ khi nào hệ thống nhận về yêu cầu có kèm theo chứng thư của người dùng. Tuy nhiên, nếu chứng thư không hợp lệ và việc xác thực thất bại, thì sẽ không có bất kỳ trình kiểm tra nào khác xử lý nó.

![problem1](./assets/problem1.png)

Trong nhiều tháng tiếp theo, bạn đã phải triển khai nhiều hơn các trình kiểm tra liên tục:
- Một người đồng nghiệp đề nghị rằng sẽ không an toàn khi truyền dữ liệu thuần thẳng đến hệ thống. Bạn cần thêm một bước xác nhận tính hợp lệ của dữ liệu trong yêu cầu.
- Sau đó, một ai đó nói rằng hệ thống của bạn dễ bị tấn công brute force để dò mật khẩu. Để tránh điều đó, bạn phải thêm một trình kiểm tra để lọc các yêu cầu thất bại lặp lại bởi cùng một địa chỉ IP.
- Tiếp đến bạn có thêm đề nghị là nên tăng tốc hệ thống bằng cách sử dụng kết quả từ bộ đệm với những yêu cầu lặp lại cùng một dữ liệu. Do đó, bạn phải thêm tiếp một trình kiểm tra khác để chỉ truyền các yêu cầu đến hệ thống khi nó không phù hợp với phản hồi từ cache.

![problem2](./assets/problem2.png)

Code cho trình kiểm tra của bạn đã lộn xộn, giờ đây nó còn tệ hơn lúc trước khi bạn thêm các tính năng mới. Thay đổi một trình kiểm tra thỉnh thoảng sẽ ảnh hưởng lên cả những cái khác. Và tệ hơn nữa là khi bạn muốn dùng lại trình kiểm tra cho các bộ phận khác trong hệ thống, bạn phải sao chép một phần code vì bộ phận đó chỉ yêu cầu vài trình kiểm tra chứ không phải tất cả.

Hệ thống sẽ trở nên rất khó hiểu và khó hơn để bảo trì. Sau nhiều ngày đấu tránh với code bạn quyết định refactor tất cả mọi thứ.

## 😊 Giải pháp

Giống nưh các behavioral khác, **Chain of Responsibility** dựa trên việc truyền đổi các hành vi riêng biệt thành các đối tượng độc lập được gọi là **handlers**. Trong trường hợp này, mỗi trình kiểm tra sẽ mở rộng các lớp của nó với một phương thức đơn nhất thực hiện công việc kiểm tra. Yêu cầu và liệu của nó, được truyền đến phương thức này như là một tham số.

Pattern gợi ý bạn liên kết các handler thành một chuỗi(chain). Một handler được liên kết có một trường cho lưu trữ tham chiếu đến handler kế tiếp trong chuỗi. Thêm vào đó, để xử lý một yêu cầu, handler truyền yêu cầu đến xa hơn theo chuỗi. Yêu cầu sẽ chạy khắp chuỗi cho đến khi tất cả handler có cơ hội xử lý nó.

Điều quan trọng ở đây: handler có thể quyết định không truyền yêu cầu sâu hơn trong chuỗi và dừng bất kỳ việc xử lý nào một cách hiệu quả.

Ở ví dụ với hệ thống đặt hàng, một handler thực hiện xử lý sau đó quyết định truyền yêu cầu sâu hơn. Giả định yêu cầu bao gồm dữ liệu hợp lý, tất cả handler có thể thực thi hành vi chính của nó, cho dù đó là kiểm tra xác thực hay bộ nhớ đệm.

![solution1](./assets/solution1.png)

Tuy nhiên, có một cách tiếp cận khác nhẹ nhàng hơn (và chuẩn hơn), mỗi khi nhận được yêu cầu, một handler quyết định liệu nó có thể xử lý hay không. Nếu nó có thể, sẽ không phải truyền yêu cầu xa hơn. Thế nên, nó chỉ có một handler để xử lý tất cả yêu cầu hoặc không có handler nào cả. Cách tiếp cận này rất giống với xử lý sự kiện trong ngăn xếp phần tử ở giao diện đồ hoạ người dùng.

Ví dụ, khi người dùng click một button, sự kiện sẽ truyền đến chuỗi phần tử GUI, bắt đầu với button, tiếp đến là container(có thể là form hoặc panel) và kết thúc ở ứng dụng window chính. Sự kiện sẽ được xử lý ở phần tử đầu tiên trong chuỗi có thể xử lý nó. Ví dụ này đáng lưu tâm vì nó cho thấy một chuỗi có thể mở rộng từ một đối tượng cây.

![solution2](./assets/solution2.png)

Điều quan trọng là tất cả lớp handler phải triển khai cùng interface. Mỗi handler cụ thể chỉ nên quan tâm một thứ theo sau phương thức thực thi. Cách này giúp bạn có thể tạo chuỗi khi đang chạy, sử dụng handler khác nhau mà không cần ghép code với lớp cụ thể của nó.

It’s crucial that all handler classes implement the same interface. Each concrete handler should only care about the following one having the execute method. This way you can compose chains at runtime, using various handlers without coupling your code to their concrete classes.

## 🚗 Thế Giới Thực

Bạn vừa mua và cài đặt một vài phần cứng lên máy tính của bạn. Ví lý do cá nhân, nên máy tính bạn có nhiều hệ điều hành. Bạn thử boot tất cả và xem phần cứng có được hỗ trợ không. Window nhận ra nó và tự động enable phần cứng. Nhưng, Linux yêu dấu của bạn lại từ chối làm việc với phần cứng mới. Bất lực, bạn quyết định gọi đến số điện thoại hỗ trợ ghi trên hộp.

Thứ đầu tiên là bạn nghe là giọng robot phản hồi tự động. Nó đề nghị các giải pháp phổ biến với nhiều vấn đề khác nhau nhưng không cái nào liên quan đến trường hợp của bạn. Sau đấy, robot kết nối bạn với nhà điều hành trực tiếp.

Xui xẻo, nhà điều hành cũng không thể đề xuất được điều gì cụ thể. Anh ta cứ nói theo hướng dẫn sử dụng, và không chịu lắng nghe bạn. Sau khi nghe: "bạn đã thử tắt máy và bật lại chưa" khoảng 10 lần, bạn đề nghi kết nối đến kỹ sư thích hợp.

Sau cùng, nhà điều hành chuyển cuộc gọi của bạn đến kỹ sư, một người có lẽ khao khát được nói chuyện trực tiếp với con người hàng giờ khi anh ta ngồi cô đơn trong phòng server ở một hầm tối nào đó trong toà nhà nào đó. Kỹ sư nói với bạn nơi tải về drive thích hợp cho phần cứng của bạn và cách cài đặt nó trên Linux. Cuối cùng vấn đề được giải quyết. 
