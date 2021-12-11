# Bridge

## 📜 Mục đích

**Bridge** là design pattern thuộc nhóm structural giúp bạn tách một lớp khổng lồ hoặc một tập hợp lớp có quan hệ gần gũi với nhau thành hai hệ thống phân cấp lớp riêng biệt là - abstraction(trừu tượng) và implementation(triển khai) - có thể phát triển độc lập với nhau.

![intent](./assets/intent.png)

## 😟 Vấn đề

Giả sử bạn có một lớp hình học `Shape` với các lớp con: `Circle` và `Square`. Bạn muốn mở rộng hệ thống phân cấp lớp này để kết hợp với màu sắc, kế hoạch của bạn là tạo lớp con `Red` và `Blue`. Tuy nhiên, vì bạn đã có hai lớp con rồi, nên bạn sẽ cần tạo bốn lớp kết hợp, vd như `BlueCircle` và `RedSquare`.

![problem](./assets/problem.png)

*Số lượng kết hợp tăng lên theo tiến trình hình học.*

Thêm một hình dạng mới hay màu sắc vào hệ thống phân cấp sẽ làm nó phát triển theo cấp số mũ. Ví dụ, thêm hình tam giác vào bạn sẽ cần thêm hai lớp con cho mỗi màu, sau đó nếu thêm một màu vàng vào sẽ lại cần thêm ba lớp con cho từng hình dạng. Càng thêm nhiều thì mọi thứ càng tệ đi.

## 😊 Giải pháp

Vấn đề này xảy ra khi ta cố gắng mở rộng lớp `Shape` thành hai phần độc lập là: hình dạng và màu sắc. Đây là vấn đề rất phổ biến với kế thừa lớp.

Pattern Bridge giải quyết vấn đề này bằng cách chuyển từ kế thừa sang cấu thành đối tượng. Có nghĩa là bạn sẽ trích xuất một phần trong lớp gốc thành các hệ thống phân cấp lớp riêng biệt, thế nên lúc này lớp gốc của bạn sẽ tham chiếu đến đối tượng của hệ thống phân cấp mới, thay vì chứa tất cả trạng thái và hành vi của nó trong một lớp.

![solution](./assets/solution.png)

*Bạn có thể ngăn chặn sự bùng nổ của hệ thống phân cấp lớp bằng cách chuyển đổi nó thành một số hệ thống phân cấp có quan hệ*

Với cách tiếp cận này ta sẽ trích xuất code liên quan đến màu sắc thành một lớp riêng với hai lớp con: `Red` và `Blue`. Lớp `Shape` sẽ lấy trường tham chiếu đến một trong những đối tượng màu sắc. Bây giờ `Shape` có thể uỷ thác mọi công việc liên quan đến màu sắc cho đối tượng `color` được liên kết. Tham chiếu này hoạt động như một cây cầu (bridge) giữa lớp `Shape` và `Color`. Từ giờ khi thêm màu mới sẽ không cần thay đổi hệ thống phân cấp lớp `Shape` và ngược lại.

### Abstraction và Implementation

Quyền sách [GoF](https://www.amazon.com/Design-Patterns-Object-Oriented-Addison-Wesley-Professional-ebook/dp/B000SEIBB8) giới thiệu thuật ngữ *Abstraction* và *Implementation* như là một phần trong định nghĩa Bridge. Theo quan điểm cá nhân thì thuật ngữ này khá hàn lâm và làm cho pattern trông phức tạp hơn. Sau khi xem ví dụ đơn giản hơn với màu sắc và hình dạng, ta có thể diễn giải lại nó như sau:

**Abstraction** (còn gọi là interface) là một lớp(tầng) điều khiển cấp cao cho một vài thực thể. Lớp này không thực hiện bất cứ công việc gì trong nó. Nó uỷ thác công việc cho lớp **implementation** (còn gọi là platform). 

Lưu ý, ở đây ta không nói về *interface* hay lớp trừu tượng trong ngôn ngữ lập trình của bạn. Đây là hai thứ hoàn toàn khác nhau.

Ví dụ một ứng dụng thực tế, abstraction có thể biểu diễn bằng giao diện đồ hoạ người dùng (GUI), và implementation có thể là những đoạn code hệ điều hành cơ bản (API), nơi lớp GUI gọi để phản hồi tương tác người dùng.

Khi bạn mở rộng ứng dụng theo hai hướng độc lập: 
- Có nhiều GUI khác nhau (vd như giao diện cho người dùng hay admin).
- Hỗ trợ nhiều API khác nhau(ví dụ như chạy ứng dụng dưới các hệ điều hành Windows, Linux, MacOS)

Trong trường hợp xấu nhất, ứng dụng này có thể trông giống như một tô mì spaghetti khổng lồ, nơi hàng trăm điều kiện kết nối các loại GUI khác nhau với các API khác nhau trên toàn bộ code.

![abstraction](./assets/abstraction.png)

Bạn có thể làm cho mọi thứ ổn định hơn bằng cách trích xuất code liên quan đến interface-platform thành các lớp riêng biệt. Tuy nhiên, sẽ có rất nhiều lớp trong đấy. Hệ thống phân cấp lớp sẽ phát triển theo cấp số mũ khi thêm một GUI hay hỗ trợ một API khác, vì sẽ yêu cầu tạo thêm nhiều và nhiều hơn các lớp nữa.

Vấn đề này sẽ được giải quyết bằng Bridge, khi ta chia các lớp thành hai hệ thống phân cấp lớp: 
- Abstraction: lớp GUI của ứng dụng.
- Implementation: các API của hệ điều hành.

![implement](./assets/implement.png)

Đối tượng abstraction điều khiển vẻ ngoài của ứng dụng, uỷ thác các công việc thực cho đối tượng implementation được liên kết. Sự khác nhau của các implementation có thể hoán đổi với nhau miễn là nó theo một interface chung, cho phép cùng một GUI chạy trên cả Windows và Linux.

Kết quả là, bạn có thể thay đổi lớp GUI mà không cần đụng đến lớp API liên quan. Hơn thế nữa khi thêm hỗ trợ cho một hệ điều hành khác chỉ yêu cầu tạo lớp con cho hệ thống phân cấp implementation.

## 🏢 Cấu trúc

![structure](./assets/structure.png)

1. **Abstraction** cung cấp logic điều khiển cấp cao. Nó dựa vào các đối tượng implementation để thực hiện các công việc ở cấp thấp hơn.
2. **Implementation** khai bao interface chung cho tất cả concrete implementations. Abstraction chỉ giao tiếp với đối tượng implementation thông qua phương thức đã khai báo ở đây.
3. **Concrete implementation** bao gồm code platform cụ thể.
4. **Refined Abstractions** cung cấp biến thể cho logic điều khiển. Giống như lớp cha, nó làm việc với implementation thông qua interface implementation chung.
5. Thông thường, **Client** chỉ quan tâm đến việc làm việc với abstraction. Tuy nhiên, nhiệm vụ của client là liên kết đối tượng abstraction với một trong các đối tượng implementation.

## 👨‍💻 Mã giả

Ví dụ minh hoạ cách Bridge phân chia khối code của ứng dụng để quản lý thiết bị và điều khiển từ xa. Lớp `Device` hoạt động như implementation, trong khi `Remote` hoạt động như abstraction.

![pseudocode](./assets/pseudocode.png)

Lớp cơ sở của `Remote` khai báo trường tham chiếu liên kết với đối tượng `Device`. Tất cả điều khiển làm việc với thiết bị thông qua interface `Device` chung, nó giúp cùng một điều khiển hỗ trợ nhiều loại thiết bị.

Bạn có thể phát triển lớp `Remote` độc lập với lớp `Device`. Tất cả những gì cần chỉ là tạo một lớp con remote mới. Ví dụ, điều khiển từ xa đơn gian chỉ có hai nút, bạn có thể mở rộng nó với các tính năng như pin dự phòng hay cảm ứng.

Code client liên kết với remote mong muốn và đối tượng thiết bị cụ thể thông qua hàm khởi tạo của remote.

```c
// "Abstraction" định nghĩa interface cho "control" của
// hai hệ thống phân cấp lớp. Nó duy trì một liên kết đến đối 
// tượng của hệ thống phân cấp "implementation" và uỷ thác
// các công việc thực cho đối tượng đó.
class RemoteControl is
    protected field device: Device
    constructor RemoteControl(device: Device) is
        this.device = device
    method togglePower() is
        if (device.isEnabled()) then
            device.disable()
        else
            device.enable()
    method volumeDown() is
        device.setVolume(device.getVolume() - 10)
    method volumeUp() is
        device.setVolume(device.getVolume() + 10)
    method channelDown() is
        device.setChannel(device.getChannel() - 1)
    method channelUp() is
        device.setChannel(device.getChannel() + 1)


// Bạn có thể mở rộng lớp từ hệ thống phân cấp abstraction
// độc lập với lớp device.
class AdvancedRemoteControl extends RemoteControl is
    method mute() is
        device.setVolume(0)


// Interface "implementation" khai báo phương thức chung cho 
// tất cả lớp implementation cụ thể. Nó không cần ứng với
// interface abstraction. Sự thật là hai interface có thể
// khác nhau toàn bộ. Tiêu biểu như interface implementation
// chỉ cung cấp toán tử nguyên thuỷ, trong khi abstraction
// khai báo các toán tử cấp cao dựa trên các nguyên thuỷ đó.
interface Device is
    method isEnabled()
    method enable()
    method disable()
    method getVolume()
    method setVolume(percent)
    method getChannel()
    method setChannel(channel)


// Tất cả thiết bị theo cùng một interface.
class Tv implements Device is
    // ...

class Radio implements Device is
    // ...


// Đâu đó trong code client.
tv = new Tv()
remote = new RemoteControl(tv)
remote.togglePower()

radio = new Radio()
remote = new AdvancedRemoteControl(radio)
```

## 💡 Ứng dụng

**🐞 Sử dụng Bridge khi bạn muốn phân chia và tổ chức khối lớp của bạn thành các phần biến thể cho một số chức năng**

⚡ Ví dụ như khi bạn làm việc với server của các cơ sở dữ liệu khác nhau. Lớp có thể trở nên quá to và khó khăn để tìm hiểu cách nó hoạt động, và khó hơn nữa để thay đổi nó. Các thay đổi với một biến thể của chức năng có thể yêu cầu thay đổi lên toàn bộ lớp, kết quả có thể tạo ra lỗi hoặc các tác dụng phụ nghiệm trọng.

Bridge giúp bạn tách khối lớp thành các hệ thống phân cấp lớp. Sau đó bạn có thể thay đổi lớp của một hệ thống phân cấp độc lập với các lớp khác. Cách tiếp cận này giúp code dễ bảo trì và tối thiểu nguy cơ code đang có bị ảnh hưởng.

**🐞 Sử dụng Bridge nếu bạn muốn mở rộng các lớp độc lập với nhau**

⚡ Bridge giúp bạn trích xuất một hệ thống phân cấp lớp riêng biệt cho từng phần. Lớp ban đầu ủy thác công việc liên quan cho các đối tượng thuộc các phân cấp đó thay vì tự làm mọi thứ. 

**🐞 Sử dụng Bridge nếu bạn cần chuyển đổi các implementation trong thời gian chạy**

⚡ Mặc dù là tùy chọn, nhưng Bridge cho phép bạn thay thế đối tượng implementation bên trong phần abstraction. Nó dễ dàng như việc gán một giá trị mới cho một trường.

Nhân tiện, mục cuối cùng này là lý do chính khiến nhiều người nhầm lẫn giữa pattern Bridge với pattern Strategy. Hãy nhớ rằng một pattern không chỉ là cách để cấu trúc các lớp của bạn. Nó cũng có thể là một ý tưởng cho một vấn đề đang được giải quyết.

## 📋 Triển khai

1. Xác định các phần độc lập trong lớp của bạn. Các khái niệm độc lập có thể là: abstraction/platform, domain/infrastructure, front-end/back-end, or interface/implementation.

2. Xem các hoạt động mà client cần và định nghĩa chúng ở lớp abstraction cơ sở.
3. Xác định các hoạt động có sẵn trên tất cả nền tảng. Khai báo những cái mà abstraction cần trong interface implementation chung.
4. Với tất cả nền tảng trong miền của bạn, tạo các lớp concrete implementation, đảm bảo rằng tất cả chúng theo interface implementation.
5. Trong lớp abstraction, thêm trường tham chiếu cho kiểu implementation. Abstraction uỷ quyền hầu hất công việc cho đối tượng implementation có liên kết với trường đó.
6. Nếu bạn có các logic cấp cao khác nhau, tạo refined abstraction cho từng biến thể được mở rộng bằng lớp abstraction cơ sở.
7. Code client nên truyền đối tượng implementation vào hàm khởi tạo abstraction để liên kết một đối tượng này với đối tượng kia. Sau đó, client có thể quên đi implementation và chỉ làm việc với đối tượng abstraction.

## ⚖️ Ưu nhược điểm

### Ưu điểm

✔️ Bạn có thể tạo các lớp và ứng dụng độc lập với nền tảng.

✔️ Code client hoạt động với abstraction cấp cao. Nó không hiển thị với các nền tảng chi tiết.

✔️ *Open/Closed Principle* Bạn có thể giới thiệu abstraction và implementation mới một cách độc lập với nhau.

✔️ *Single Responsibility Principle* Bạn có thể tập trung vào logic cấp cao trong phần abstraction và chi tiết nền tảng trong quá trình implementation. 

### Nhược điểm

❌ Bạn có thể làm cho code phức tạp hơn bằng cách áp dụng pattern cho một lớp có tính dính kết cao.

## 🔁 Quan hệ với các pattern khác

**Bridge** thường được thiết kế từ trước, cho phép bạn phát triển các phần của ứng dụng một cách độc lập với nhau. Mặt khác, **Adapter** thường được sử dụng với một ứng dụng hiện có để  một số lớp không tương thích hoạt động với nhau.

**Bridge**, **State**, **Strategy** (và ở một mức độ nào đó là **Adapter**) có cấu trúc rất giống nhau. Thật vậy, tất cả các pattern này đều dựa trên nguyên tắc là ủy thác công việc cho các đối tượng khác. Tuy nhiên, chúng giải quyết các vấn đề khác nhau. Một pattern không chỉ là một công thức để cấu trúc code của bạn theo một cách cụ thể. Nó còn có thể giao tiếp với các nhà phát triển khác về vấn đề mà pattern giải quyết.

Bạn có thể sử dụng **Abstract Factory** cùng với **Bridge**. Việc ghép nối này rất hữu ích khi một số abstract được xác định bởi **Bridge** chỉ có thể hoạt động với các implementation cụ thể. Trong trường hợp này, **Abstract Factory** có thể đóng gói các quan hệ này và ẩn sự phức tạp khỏi code client.

Bạn có thể kết hợp **Builder** với **Bridge**: lớp director đóng vai trò abstraction, trong khi các builder khác đóng vai trò implementation.

# Nguồn

[**refactoring**](https://refactoring.guru/design-patterns/bridge)