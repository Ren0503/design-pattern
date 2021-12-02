# Observer

## 📜 Mục đích

Observer là một design pattern dạng behavioral giúp bạn xác định một cơ chế đăng ký để thông báo cho nhiều đối tượng bất kỳ sự kiện nào diễn ra với đối tượng mà chúng quan sát.

![intent](./assets/intent.png)

## 😟 Vấn đề
Imagine that you have two types of objects: a Customer and a Store. The customer is very interested in a particular brand of product (say, it’s a new model of the iPhone) which should become available in the store very soon.

Tưởng tượng bạn có hai kiểu đối tượng: `Customer` và `Store`. Khách hàng thường bị hấp dẫn với một vài thương hiệu sản phẩm nổi bật, ví dụ như mẫu iPhone mới sẽ sớm được bán ở của hàng.

Khách hàng sẽ đến cửa hàng mỗi ngày để kiểm tra sản phẩm đã có bán chứa. Nhưng nếu sản phẩm vẫn đang nhập về, thì phần lớn công sức của họ cho mỗi chuyến đi sẽ vô nghĩa.

![problem](./assets/problem.png)

Thế nên, cửa hàng sẽ gửi hàng tấn mail (có thể là spam) cho tất cả khách hàng mỗi lần có sản phẩm mới. Điều này giúp khách hàng tránh những chuyến đi vô nghĩa đến cửa hàng. Nhưng nó sẽ các khách hàng khác (những người không có hứng thú với sản phẩm mới) khó chịu.

Có vẻ như chúng ta đã xảy ra xung đột. Khách hàng lãng phí thời gian kiểm tra sản phẩm đã bán chưa hoặc cửa hàng lãng phí nguồn lực để thông báo thừa cho khách hàng.

## 😊 Giải pháp

Đối tượng có trạng thái hấp dẫn thường được gọi là subject(chủ thể), nhưng vì nó cũng sẽ thông báo cho các đối tượng khác về những thay đổi đối với trạng thái của nó, nên ta sẽ gọi nó là **publisher**. Tất cả đối tượng khác muốn theo dõi trạng thái của publisher được gọi là **subscriber**.

Pattern Observer đề nghị giải pháp là bạn thêm một cơ chế đăng ký đến lớp publisher nên các đối tượng riêng biệt có thể đăng ký hoặc huỷ đăng ký từ một dòng các sự kiện xảy đến từ publisher. Thật ra mọi thứ không đến nổi quá phức tạp. Thực tế, cơ chế này bao gồm một trường mảng cho lưu trữ danh sách tham chiếu đến đối tượng subscriber và nhiều phương thức công khai cho phép thêm hay xoá subscriber khỏi danh sách.

![solution1](./assets/solution1.png)

Bây giờ, bất cứ khi nào có sự kiện quan trọng diễn ra với publisher, nó đi qua tất cả subscriber và gọi phương thức thông báo cụ thể trên đối tượng của chúng.

Ứng dụng thực có thể có hàng tá lớp subscriber khác nhau quan tâm đến việc theo dõi các sự kiện của cùng một lớp publisher. Bạn sẽ không muốn ghép publiser với tất cả các lớp đó. Bên cạnh đó, bạn thậm chí có thể không biết về một số trong số họ trước nếu lớp publisher của bạn được người khác sử dụng. 

Đó là lý do tại sao điều quan trọng là tất cả subscriber phải triển khai cùng một interfacen và publisher chỉ giao tiếp với họ qua interface đó. Interface này phải khai báo phương thức thông báo cùng với một tập hợp các tham số mà publisher có thể sử dụng để chuyển một số dữ liệu ngữ cảnh cùng với thông báo.

![solution2](./assets/solution2.png)

Nếu ứng dụng của bạn có nhiều kiểu publisher khác nhau và bạn muốn làm cho subscriber của mình tương thích với tất cả họ, bạn có thể tiến xa hơn nữa và khiến tất cả các publishern tuân theo cùng một interface. Interface này sẽ chỉ cần mô tả một số phương pháp đăng ký. Interface sẽ cho phép subscriber quan sát trạng thái của publisher mà không liên quan đến các lớp cụ thể của họ.

## 🚗 Thế Giới Thực

Nếu bạn đăng ký một tờ báo hoặc tạp chí, bạn không cần phải đến cửa hàng để kiểm tra xem số tiếp theo có sẵn hay không. Thay vào đó, nhà xuất bản gửi các số báo mới trực tiếp đến hộp thư của bạn ngay sau khi xuất bản hoặc thậm chí trước.

Nhà xuất bản duy trì danh sách người đăng ký và biết họ quan tâm đến tạp chí nào. Người đăng ký có thể rời khỏi danh sách bất kỳ lúc nào khi họ muốn ngăn nhà xuất bản gửi các số tạp chí mới cho họ.