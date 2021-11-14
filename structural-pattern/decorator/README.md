# Decorator

## 📜 Mục đích

**Decorator** là một design pattern dạng structural giúp bạn thêm một hành mới vào đối tượng bằng cách đặt đối tượng đó vào trong một đối tượng đặc biệt có chứa hành vi đấy

![intent](./assets/intent.png)

## 😟 Vấn đề

Imagine that you’re working on a notification library which lets other programs notify their users about important events.

Tưởng tượng bạn đang làm việc với một thư viện thông báo, nơi giúp các chương trình khác thông báo cho người dùng của họ các sự kiện quan trọng.

Phiên bản ban đầu của thư viện dựa trên lớp `Notifier` chỉ gồm một vai trường, hàm khởi tạo và phương thức `send` duy nhất. Phương thức này nhận các tham số tin nhắn từ client và gửi tin đến danh sách email đã được truyền đến `notifier` thông qua hàm khởi tạo. Ứng dụng bên thứ ba sẽ hành động như client phải tạo và cấu hình đối tượng `notifier` một lần, sau đó sử dụng nó cho tất cả các sự kiện quan trọng diễn ra.

![problem1](./assets/problem1.png)

Vào một thời điểm nào đó, bạn nhận ra người dùng của thư viện mong muốn nhiều hơn thông báo từ email. Phần lớn họ muốn nhận thêm thông báo SMS. Số khác muốn thông báo trên Facebook, và một  
vài doanh nghiệp sử dụng muốn nhận thông báo từ Slack.

![problem2](./assets/problem2.png)

Điều này khó khăn như thế nào? Bạn phải mở rộng lớp `Notifier` và thêm các phương thức thông báo bổ sung vào lớp con mới. Bây giờ client sẽ tạo lớp thông báo mong muốn và sử dụng nó cho tất cả thông báo trong tương lai.

Nhưng nếu có thêm một góp ý nữa như "Tại sao bạn không gửi nhiều kiểu thông báo cùng lúc? Nếu nhà bạn đang cháy, bạn có muốn nhận được thông tin từ mọi phương tiện."

Bạn sẽ giải quyết vấn đề này bằng cách tạo lớp con đặc biệt là kết hợp tất cả phương thức thông báo trong một lớp. Tuy nhiên, bạn sẽ nhanh chóng nhận ra là cách tiếp cận này làm code phình to lên, không chỉ là ở thư viện mà cả ở client code.

![problem3](./assets/problem3.png)

Bạn cần tìm cách khác để cấu trúc lớp thông báo sao cho số lượng của chúng không vô tình phá vỡ kỷ lục Guinnesss.

## 😊 Giải pháp

Mở rộng lớp là điều đầu tiên người ta nghĩ đến khi cần thay đổi hành vi đối tượng. Tuy nhiên, kế thừa có nhiều cảnh báo mà ta cần phải biết:
- Kế thừa là tĩnh. Bạn không thể thay đối hành vi của đối tượng đã tồn tại khi chạy. Bạn chỉ có thể thay thế đối tượng đấy với đối tượng khác đã tạo từ lớp con khác.
- Lớp con có thể chỉ có một lớp cha. Trong hầu hết ngôn ngữ, kế thừa không giúp lớp kế thừa các hành vi của nhiều lớp cùng thời điểm.

Một trong những cách khắc phục các cảnh báo trên là sử dụng Aggregation(tổng hợp) hoặc Composition(phức hợp) thay vì kế thừa. Cả hai thay thế đều hoạt động cùng một cách: tạo đối tượng tham chiếu đến cái khác và uỷ quyền một số công việc cho nó. Nhưng trái lại với kế thừa bản thân đối tượng có thể thực hiện công việc đó, bằng cách kế thừa hành vi từ lớp cha của nó.

Với cách tiếp cận mới bạn có thể dễ dàng thay thế liên kết "helper" giữa đối tượng với một cái khác, thay đổi hành vi của container khi đang chạy. Một đối tượng có thể sử dụng hành vi của lớp biến thể, có tham chiều đến nhiều đối tượng và uỷ thác cho nó tất cả công việc.
Aggregation/composition là từ khoá cho khá nhiều design pattern, bao gồm cả Decorator. Ta sẽ thảo luận về pattern này sau.

![solution1](./assets/solution1.png)

**Wrapper** là tên thay thể cho Decorator đễ diễn đạt rõ ràng ý tưởng chính của pattern. Một Wrapper là một đối tượng có thể liên kết với một vài đối tượng đích. Wrapper bao gồm tập hợp phương thức giống nhau là mục tiêu và ủy quyền cho nó tất cả các yêu cầu mà nó nhận được. Tuy nhiên, Wrapper có thể thay đổi kết quả bằng một vài hành động trước hoặc sau khi truyền yêu cầu đến đích.

Khi nào một wrapper đơn giản trở thành một decorator? Như đã nhấn mạnh, wrapepr triển khai cùng một interface như một đối tượng wrapper. Đấy là lý do tại sao từ góc nhìn client tất cả đối tượng là như nhau. Các trường tham chiếu của wrapper chấp nhận bất kỳ đối tượng nào theo sao interface đấy. Điều này giúp bạn bao một đối tượng trong nhiều wrapper và thêm các hành vi kết hợp của tất cả wrapper cho nó.

Trong ví dụ thư viện thông báo, ta chỉ chuyển hành vi thông báo email vào lớp cơ sở Notifier, và chuyển tất cả phương thức thông báo khác vào decorator.

In our notifications example, let’s leave the simple email notification behavior inside the base Notifier class, but turn all other notification methods into decorators.

![solution2](./assets/solution2.png)

Client code có thể cần bọc đối tượng notifier đơn giản vào tập hợp của decorato ứng với mong muốn client. Đối tượng kết quả sẽ có cấu trúc như một ngăn xếp.

![solution3](./assets/solution3.png)

Decorator cuối cùng của ngăn xếp sẽ là đối tượng mà client thực sự làm việc. Vì tất cả decorator triển khai cùng interface, nên phần client code còn lại không quan tâm các nó làm việc là đối tượng `notifier` thuần hay là decorator.

Ta có thể áp dụng cách tiếp cận này cho các hành vi khác như định dạng tin nhắn hoặc tạo danh sách người nhân. Client có thể tạo đối tượng với bất kỳ decorator nào, miễn là nó theo cùng interface với những cái khác.
