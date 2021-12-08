# Facade

## 📜 Mục đích

**Facade** là design pattern thuộc nhóm structural cung cấp interface đơn giản cho thư viện, framework hoặc bất kỳ tập hợp lớp phức tạp nào khác.

![intent](./assets/intent.png)

## 😟 Vấn đề

Hãy tưởng tượng rằng bạn phải sử dụng code của mình để làm việc với một loạt các đối tượng thuộc về một thư viện hoặc framework phức tạp. Thông thường, bạn cần khởi tạo tất cả các đối tượng đó, theo dõi các phụ thuộc, thực thi các phương thức theo đúng thứ tự, ...

Do đó, logic nghiệp vụ trong các lớp của bạn sẽ trở nên lệ thuộc chặt chẽ với các chi tiết triển khai của các lớp bên thứ ba, khiến cho việc hiểu rõ và bảo trì trở nên khó khăn.

## 😊 Giải pháp

Facade là một lớp cung cấp interface đơn giản cho cho một hệ thống con phức tạp chứa nhiều bộ phận chuyển động. Một facade có thể cung cấp chức năng hạn chế so với làm việc trực tiếp qua hệ thống con. Tuy nhiên, nó sẽ bao gồm những tính năng mà client thực sự quan tâm.

Có một facade rất tiện lợi khi bạn cần tích hợp ứng dụng của mình với một thư viện phức tạp có hàng tá tính năng, nhưng bạn chỉ cần một vài chức năng trong đó

Ví dụ: một ứng dụng tải video ngắn hài hước về mèo lên mạng xã hội có thể sử dụng thư viện chuyển đổi video chuyên nghiệp. Tuy nhiên, tất cả những gì bạn thực sự cần là một lớp với một phương thức duy nhất `encode(filename, format)`. Sau khi tạo một lớp như vậy và kết nối nó với thư viện chuyển đổi video, bạn sẽ có facade đầu tiên của mình..

## 🚗 Thế Giới Thực

![analogy](./assets/analogy.png)

Khi bạn gọi đến một cửa hàng để đặt hàng qua điện thoại, nhân viên tổng đài sẽ là facade của bạn đối với tất cả các dịch vụ và bộ phận của cửa hàng. Nhà điều hành cung cấp cho bạn một  interface giọng nói đơn giản với hệ thống đặt hàng, cổng thanh toán và các dịch vụ giao hàng khác nhau.

## 🏢 Cấu trúc

![structure](./assets/structure.png)

1. **Facade** cung cấp khả năng truy cập thuận tiện vào một phần cụ thể của chức năng trong hệ thống con. Nó biết nơi định hướng yêu cầu của client và cách vận hành tất cả các bộ phận hoạt động.
2. **Additional Facade**, lớp bổ sung có thể được tạo để ngăn chặn việc làm hỏng một facede đơn lẻ với các tính năng không liên quan khiến nó trở thành một cấu trúc phức tạp. Additional Facade có thể được sử dụng bởi client và facade khác.
3. **Complex Subsystem** bao gồm hàng chục đối tượng khác nhau. Để tất cả bọn chúng làm điều gì đó có ý nghĩa, bạn phải đi sâu vào chi tiết triển khai của hệ thống con, chẳng hạn như khởi tạo các đối tượng theo đúng thứ tự và cung cấp cho chúng dữ liệu ở định dạng thích hợp.
Các lớp hệ thống con không biết về sự tồn tại của facade. Chúng hoạt động trong hệ thống và làm việc trực tiếp với nhau.
4. **Client** sử dụng facade thay vì gọi trực tiếp đến hệ thống con.

## 👨‍💻 Mã giả

Trong ví dụ này, Facade đơn giản hóa việc tương tác với một framework chuyển đổi video phức tạp.

![pseudocode](./assets/pseudocode.png)

Thay vì sử dụng code của bạn làm việc trực tiếp với hàng chục lớp framework, bạn tạo một lớp facade đóng gói chức năng đó và ẩn nó khỏi phần code còn lại. Cấu trúc này cũng giúp bạn giảm thiểu việc nâng cấp lên các phiên bản trong tương lai của framework hoặc thay thế nó bằng một framework khác. Điều duy nhất bạn cần thay đổi trong ứng dụng của mình sẽ là triển khai các phương pháp của facade.

```c
// Đây là một số lớp phức tạp của framework chuyển đổi video
// bên thứ 3. Ta không kiểm soát code này nên không đơn 
// giản nó được.

class VideoFile
// ...

class OggCompressionCodec
// ...

class MPEG4CompressionCodec
// ...

class CodecFactory
// ...

class BitrateReader
// ...

class AudioMixer
// ...


// Ta tạo lớp facade để ẩn framework phức tạp sau interface
// đơn giản. Nó là đánh đổi giữa đầy đủ chức năng và tính 
// đơn giản.
class VideoConverter is
    method convert(filename, format):File is
        file = new VideoFile(filename)
        sourceCodec = new CodecFactory.extract(file)
        if (format == "mp4")
            destinationCodec = new MPEG4CompressionCodec()
        else
            destinationCodec = new OggCompressionCodec()
        buffer = BitrateReader.read(filename, sourceCodec)
        result = BitrateReader.convert(buffer, destinationCodec)
        result = (new AudioMixer()).fix(result)
        return new File(result)

// Lớp ứng dụng không phụ thuộc vào hàng tỉ lớp được cung cấp
// bởi framework phức tạp. Nếu bạn muốn đổi framework, bạn chỉ
// cần viết lại lớp facade.
class Application is
    method main() is
        convertor = new VideoConverter()
        mp4 = convertor.convert("funny-cats-video.ogg", "mp4")
        mp4.save()
```

## 💡 Ứng dụng

**🐞 Sử dụng Facade khi bạn cần có một interface hạn chế nhưng đơn giản cho một hệ thống con phức tạp**

⚡ Thông thường, các hệ thống con trở nên phức tạp hơn theo thời gian. Ngay cả việc áp dụng các design pattern thường dẫn đến việc tạo ra nhiều lớp hơn. Một hệ thống con có thể trở nên linh hoạt hơn và dễ dàng sử dụng lại trong các ngữ cảnh khác nhau, nhưng số lượng cấu hình và code có sẵn mà nó yêu cầu từ client ngày càng lớn hơn. Facade cố gắng khắc phục sự cố này bằng cách cung cấp một lối tắt đến các tính năng được sử dụng nhiều nhất của hệ thống con phù hợp với hầu hết các yêu cầu của client.

**🐞 Sử dụng Facade khi bạn muốn cấu trúc một hệ thống con thành các lớp**

⚡ Tạo các facade để xác định các điểm vào cho mỗi cấp của một hệ thống con. Bạn có thể giảm sự ghép nối giữa nhiều hệ thống con bằng cách yêu cầu chúng chỉ giao tiếp thông qua các facade.

Ví dụ: hãy quay lại framework chuyển đổi video. Nó có thể được chia thành hai lớp: liên quan đến video và âm thanh. Đối với mỗi lớp, bạn có thể tạo một facade và sau đó làm cho các lớp của mỗi lớp giao tiếp với nhau thông qua các facade. Cách tiếp cận này trông rất giống với **Mediator**.

## 📋 Triển khai

1. Kiểm tra xem liệu có thể cung cấp interface đơn giản hơn những gì hệ thống con hiện tại đã cung cấp hay không. Bạn đang đi đúng hướng nếu interface này làm cho code client độc lập với nhiều lớp của hệ thống con.
2. Khai báo và triển khai interface này trong một lớp facade mới. Facade phải chuyển hướng các cuộc gọi từ code client đến các đối tượng thích hợp của hệ thống con. Facade phải chịu trách nhiệm khởi tạo hệ thống con và quản lý vòng đời tiếp theo của nó trừ khi code client đã thực hiện điều này.
3. Để có được toàn bộ lợi ích từ thiết kế, hãy làm cho tất cả code client chỉ giao tiếp với hệ thống con thông qua facade. Bây giờ code client được bảo vệ khỏi bất kỳ thay đổi nào trong code hệ thống con. Ví dụ: khi một hệ thống con được nâng cấp lên phiên bản mới, bạn sẽ chỉ cần sửa đổi code trong facade.
4. Nếu facade trở nên quá lớn, hãy xem xét trích xuất một phần hành vi của nó sang một lớp facade mới.

## ⚖️ Ưu nhược điểm

### Ưu điểm

✔️ Bạn có thể tách code của mình khỏi sự phức tạp của một hệ thống con.

### Nhược điểm

❌ Một facade có thể trở thành một đối tượng thần thánh cùng với tất cả các lớp của một ứng dụng. 

## 🔁 Quan hệ với các pattern khác

**Facade** định nghĩa một interface mới cho các đối tượng hiện có, trong khi **Adapter** cố gắng làm cho interface hiện có có thể sử dụng được. **Adapter** thường chỉ bọc một đối tượng, trong khi **Facade** hoạt động với toàn bộ hệ thống con của các đối tượng.

**Abstract Factory** có thể dùng như một giải pháp thay thế cho **Facade** khi bạn chỉ muốn ẩn cách các đối tượng hệ thống con được tạo ra khỏi code client.

**Flyweight** cho thấy cách tạo nhiều đối tượng nhỏ, trong khi **Facade** cho thấy cách tạo một đối tượng duy nhất đại diện cho toàn bộ hệ thống con.

**Facade** và **Mediator** có những công việc tương tự nhau: cố gắng tổ chức sự hợp tác giữa nhiều lớp được kết hợp chặt chẽ với nhau.

- **Facade** xác định một interface đơn giản cho một hệ thống con của các đối tượng, nhưng nó không giới thiệu bất kỳ chức năng mới nào. Bản thân hệ thống con không biết về facade. Các đối tượng trong hệ thống con có thể giao tiếp trực tiếp.
- **Mediator** tập trung giao tiếp giữa các thành phần của hệ thống. Các thành phần chỉ biết về đối tượng mediator và không giao tiếp trực tiếp.

Một lớp **Facade** thường có thể được chuyển đổi thành **Singleton** vì một đối tượng facade duy nhất là đủ trong hầu hết các trường hợp.

**Facade** tương tự như **Proxy** ở chỗ cả hai đều đệm một thực thể phức tạp và tự khởi tạo nó. Không giống như **Facade**, **Proxy** có interface giống với đối tượng dịch vụ của nó, điều này làm cho chúng có thể hoán đổi cho nhau.

# Nguồn

[**refactoring**](https://refactoring.guru/design-patterns/facade)
