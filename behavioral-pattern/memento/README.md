# Memento

## 📜 Mục đích

Memento là một desgin pattern dạng behavioral giúp bạn lưu và phụ hồi trạng thái trước đó của một đối tượng mà không để chi tiết triển khai của nó

![intent](./assets/intent.png)

## 😟 Vấn đề

Tưởng tượng bạn đang tạo một ứng dụng soạn thảo văn bản. Bên cạnh việc chỉnh sửa đơn giản, bạn còn phải tạo chức năng định dạng văn bản, thêm ảnh, chỉnh phông,...

Vào một thời điểm nào đó, bạn quyết định thêm chức năng giúp người dùng hoàn tác bất kỳ thao tác nào được thực hiện trên văn bản. Chức năng này rất phồ biến trong thời gian gần đây và người dùng thường kỳ vọng là mọi ứng dụng đều có nó.
Để triển khai, bạn chọn cách tiếp cận trực tiếp. Trước khi thực hiện bất kỳ thao tác nào, ứng dụng sẽ ghi trạng thái của tất cả đối tượng trong nó và lưu chúng vào một vài nơi lưu trữ. Sau đó khi người dùng muốn hoàn tác hành động, ứng dụng lấy bản lưu nhanh gần nhất từ lịch sử và dùng nó để phục hồi trạng thái của mọi đối tượng.

![problem1](./assets/problem1.png)

Xem xét kỹ bản lưu nhanh của các trạng thái này. Tự hỏi bạn làm thế nào để tạo chính xác nó? Có lẽ bạn sẽ đi qua tất cả trường trong đối tượng sao chép giá trị của chúng và lưu vào bộ nhớ. Tuy nhiên nó sẽ chỉ hoạt động nếu đối tượng của bạn không hạn chế truy cập đến nội dung của nó. Không may, phần lớn đối tượng thực sẽ không để những thứ bên ngoài nhìn vào bên trong của nó dễ dàng, nó sẽ ẩn tất cả dữ liệu có ích vào các trường riêng tư.

Bây giờ tạm bỏ qua vấn đề này và mặc định rằng tất cả đối tượng của chúng ta như những con hà mã: thích cái quan hệ mở và công khai trạng thái của chúng. Lúc này, ngay cả khi cách tiếp cận trên giải quyết vấn đề ngay lập tức và giúp bạn tạo bản lưu nhanh của trạng thái đối tượng tuỳ ý, thì nó vẫn tồn đọng nhiều vấn đề nghiêm trọng. Trong tương lai, khi bạn quyết định cấu trúc lại một vài lớp chỉnh sửa, thêm hoạt xoá một vài trường. Bạn sẽ nhận về yêu cầu thay đổi tất cả các lớp chịu trách nhiệm cho sao chép trạng thái của đối tượng chịu ảnh hưởng.

![problem2](./assets/problem2.png)

Hơn thế nữa. Hãy xem xét các bản lưu nhanh của trạng thái chỉnh sửa. Dữ liệu trong nó bao gồm những gì? Ở mức tối thiểu, nó phải bao gồm các văn bản thực, toạ độ con trỏ, vị trí hiện tại đang scroll,... Để tạo bản lưu nhanh, bạn cần phải tìm kiếm các giá trị này và đặt chúng vào trong một kiều vùng chứa.

Phần lớn, bạn sẽ lưu một lượng đối tượng vùng chứa này trong một vài danh sách để biểu diễn lịch sử thao tác. Do đó, vùng chứa có lẽ là sẽ trở thành đối tượng của một lớp. Lớp này không có phương thức, những có nhiều trường để nhân bản trạng thái của editor. Để cho phép các đối tượng khai viết và đọc dữ liệu từ bản lưu nhanh, bạn phải công khai tất cả các trường của nó. Điều này vô tình làm lộ trạng thái của ứng dụng bất kể nó riêng tư hay không. Các lớp khác sẽ trở nên phụ thuộc vào mọi thay đổi nhỏ đến lớp của bản lưu, nếu không thì nó sẽ diễn ra bên trong các trường riêng tử và phương thức mà không ảnh hưởng đến bên ngoài lớp.

Có vẻ như chúng ta đã đi đến ngõ cụt: bạn để lộ tất cả chi tiết bên trong của các lớp, khiến chúng quá mỏng manh hoặc hạn chế quyền truy cập vào trạng thái của chúng, khiến bạn không thể tạo bản lưu nhanh. Có cách nào khác để thực hiện "hoàn tác" không?
