# Visitor

## 📜 Mục đích

**Visitor** là một design pattern dạng behavioral giúp bạn tách các thuật toán khỏi đối tượng mà chúng đang hoạt động trên đó.

![intent](./assets/intent.png)

## 😟 Vấn đề

Tưởng tượng team bạn đang phát triển một ứng dụng làm việc với thông tin địa lý được cấu trúc dưới dạng một biểu đồ khổng lồ. Mỗi nút trong đồ thị có thể biểu diễn một thực thể phức tạp như một thành phố, nhưng chi tiết hơn như các nhà máy, khu tham quan, .... Các nút được kết nối với nhau nếu có một con đường giữa các đối tượng thực mà nó biểu diễn. Hiểu sâu hơn, mỗi loại nút được biểu diễn bởi lớp riêng của nó, trong khi mỗi nút cụ thể là một đối tượng.

![problem](./assets/problem1.png)

Tại một thời điểm nào đó, bạn có nhiệm vụ triển khai xuất biểu đồ sang định dạng XML. Lúc đầu, công việc có vẻ khá đơn giản. Bạn đã lên kế hoạch thêm một phương thức xuất vào từng lớp nút và sau đó tận dụng đệ quy để đi qua từng nút của biểu đồ, thực hiện phương thức xuất. Giải pháp rất đơn giản và thanh lịch: nhờ tính đa hình, bạn không phải ghép đoạn code được gọi là phương thức xuất với các lớp nút cụ thể.

Thật không may, kỹ sư hệ thống đã từ chối cho phép bạn thay đổi các lớp nút hiện có. Anh ấy nói rằng code đã được tạot và anh ấy không muốn mạo hiểm phá vỡ nó vì một lỗi tiềm ẩn trong các thay đổi của bạn.

![problem](./assets/problem2.png)

Bên cạnh đó, anh ấy đặt câu hỏi liệu có hợp lý khi có code xuất XML trong các lớp nút hay không. Công việc chính của các lớp này là làm việc với dữ liệu địa lý. Hành vi xuất XML sẽ có vẻ khác lạ ở đó.

Có một lý do khác cho việc từ chối. Rất có thể sau khi tính năng này được triển khai, một người nào đó từ bộ phận tiếp thị sẽ yêu cầu bạn cung cấp khả năng xuất sang một định dạng khác hoặc yêu cầu một số thứ kỳ lạ khác. Điều này sẽ buộc bạn phải thay đổi những lớp quý giá và mỏng manh đó một lần nữa.

## 😊 Giải pháp

Visitor gợi ý rằng bạn nên đặt hành vi mới vào một lớp riêng biệt được gọi là visitor, thay vì cố gắng tích hợp nó vào các lớp hiện có. Đối tượng ban đầu phải thực hiện hành vi hiện được chuyển cho một trong các phương thức của visitor truy cập dưới dạng tham số, cung cấp cho phương thức này quyền truy cập vào tất cả dữ liệu cần thiết có trong đối tượng.

Bây giờ, điều gì sẽ xảy ra nếu hành vi đó có thể được thực thi trên các đối tượng của các lớp khác nhau? Ví dụ, trong trường hợp này với xuất XML, việc triển khai thực tế có thể sẽ khác một chút trên các lớp nút khác nhau. Do đó, lớp visitor có thể xác định không phải một, mà là một tập hợp các phương thức, mỗi phương thức có thể nhận các đối số thuộc các kiểu khác nhau, như thế này:

```c
class ExportVisitor implements Visitor is
    method doForCity(City c) { ... }
    method doForIndustry(Industry f) { ... }
    method doForSightSeeing(SightSeeing ss) { ... }
    // ...
```

Nhưng chính xác thì chúng ta sẽ gọi những phương pháp này như thế nào, đặc biệt là khi xử lý toàn bộ đồ thị? Các phương pháp này có các chữ ký khác nhau, vì vậy chúng tôi không thể sử dụng tính đa hình. Để chọn một phương thức visitor truy cập thích hợp có thể xử lý một đối tượng nhất định, chúng tôi cần kiểm tra lớp của nó. Nghe có vẻ như một cơn ác mộng?

```c
foreach (Node node in graph)
    if (node instanceof City)
        exportVisitor.doForCity((City) node)
    if (node instanceof Industry)
        exportVisitor.doForIndustry((Industry) node)
    // ...
}
```

Bạn có thể hỏi, tại sao chúng ta không sử dụng phương thức nạp chồng? Đó là khi bạn đặt cùng một tên cho tất cả các phương thức, ngay cả khi chúng hỗ trợ các bộ tham số khác nhau. Thật không may, ngay cả khi giả sử rằng ngôn ngữ lập trình của chúng tôi hỗ trợ nó (như Java và C #), nó sẽ không giúp ích gì cho chúng tôi. Vì lớp chính xác của đối tượng nút không được biết trước, cơ chế nạp chồng sẽ không thể xác định phương thức chính xác để thực thi. Nó sẽ mặc định là phương thức nhận một đối tượng của lớp `Node` cơ sở.

Tuy nhiên, kiểu visitor giải quyết vấn đề này. Nó sử dụng một kỹ thuật gọi là **Double Dispatch**, giúp thực thi phương thức thích hợp trên một đối tượng mà không cần các điều kiện rườm rà. Thay vì cho phép client chọn một phiên bản thích hợp của phương thức để gọi, chúng ta ủy thác lựa chọn này cho các đối tượng mà chúng ta đang chuyển cho visitor làm đối số thì sao? Vì các đối tượng biết các lớp riêng của chúng, họ sẽ có thể chọn một phương pháp thích hợp cho visitor một cách ít lúng túng hơn. Họ “chấp nhận” một visitor và cho người đó biết phương thức truy cập nào nên được thực thi.

```c
// Client code
foreach (Node node in graph)
    node.accept(exportVisitor)

// City
class City is
    method accept(Visitor v) is
        v.doForCity(this)
    // ...

// Industry
class Industry is
    method accept(Visitor v) is
        v.doForIndustry(this)
    // ...
```

Tôi thú nhận. Rốt cuộc, chúng tôi đã phải thay đổi các lớp nút. Nhưng ít nhất sự thay đổi là nhỏ và nó cho phép chúng tôi thêm các hành vi khác mà không phải thay đổi code một lần nữa.

Bây giờ, nếu chúng tôi trích xuất một interface chung cho tất cả visitor, thì tất cả các nút hiện có có thể hoạt động với bất kỳ visitor nào mà bạn thêm vào ứng dụng. Nếu bạn thấy mình đang giới thiệu một hành vi mới liên quan đến các nút, tất cả những gì bạn phải làm là triển khai một lớp visitor mới.

## 🚗 Thế Giới Thực

![analogy](./assets/analogy.png)

Hãy tưởng tượng một đại lý bảo hiểm dày dạn kinh nghiệm đang mong muốn có được khách hàng mới. Anh ta có thể đến thăm mọi tòa nhà trong khu phố, cố gắng bán bảo hiểm cho mọi người anh ta gặp. Tùy thuộc vào loại hình tổ chức chiếm giữ tòa nhà, anh ta có thể đưa ra các chính sách bảo hiểm chuyên biệt:

- Nếu đó là một tòa nhà dân cư, anh ta bán bảo hiểm y tế.
- Nếu đó là một ngân hàng, anh ta bán bảo hiểm trộm cắp.
- Nếu đó là một quán cà phê, anh ấy bán bảo hiểm cháy nổ và thiên tai.

## 🏢 Cấu trúc

![structure](./assets/structure.png)

1. **Visitor** là interface khai báo một tập hợp các phương thức truy cập có thể lấy các phần tử cụ thể của cấu trúc đối tượng làm tham số. Các phương thức này có thể trùng tên nếu chương trình được viết bằng ngôn ngữ hỗ trợ overloading, nhưng kiểu tham số của chúng phải khác nhau.
2. **Concrete Visitor** thực hiện một số phiên bản của các hành vi giống nhau, được điều chỉnh cho các lớp phần tử cụ thể khác nhau.
3. **Element** là interface khai báo một phương thức để "chấp nhận" visitor. Phương thức này phải có một tham số được khai báo với kiểu interface visitor. 
4. **Concrete Element** thực hiện phương pháp nghiệm thu. Mục đích của phương thức này là chuyển hướng lệnh gọi đến phương thức của visitor thích hợp tương ứng với lớp element hiện tại. Cần biết rằng ngay cả khi một lớp element cơ sở triển khai phương thức này, tất cả các lớp con vẫn phải ghi đè phương thức này trong các lớp của chính chúng và gọi phương thức thích hợp trên đối tượng visitor.
5. **Client** thường đại diện cho một tập hợp hoặc một số đối tượng phức tạp khác (ví dụ, một cây tổng hợp). Thông thường, client không biết tất cả các lớp phần tử cụ thể vì chúng làm việc với các đối tượng từ bộ sưu tập đó thông qua một số interface trừu tượng

## 👨‍💻 Mã giả

Trong ví dụ này, Visitor thêm hỗ trợ xuất XML vào hệ thống phân cấp lớp của các hình dạng hình học.

![pseudocode](./assets/pseudocode.png)

*Xuất nhiều loại đối tượng khác nhau sang định dạng XML thông qua đối tượng visitor.*

```c
// The element interface declares an `accept` method that takes
// the base visitor interface as an argument.
interface Shape is
    method move(x, y)
    method draw()
    method accept(v: Visitor)

// Each concrete element class must implement the `accept`
// method in such a way that it calls the visitor's method that
// corresponds to the element's class.
class Dot implements Shape is
    // ...

    // Note that we're calling `visitDot`, which matches the
    // current class name. This way we let the visitor know the
    // class of the element it works with.
    method accept(v: Visitor) is
        v.visitDot(this)

class Circle implements Shape is
    // ...
    method accept(v: Visitor) is
        v.visitCircle(this)

class Rectangle implements Shape is
    // ...
    method accept(v: Visitor) is
        v.visitRectangle(this)

class CompoundShape implements Shape is
    // ...
    method accept(v: Visitor) is
        v.visitCompoundShape(this)


// The Visitor interface declares a set of visiting methods that
// correspond to element classes. The signature of a visiting
// method lets the visitor identify the exact class of the
// element that it's dealing with.
interface Visitor is
    method visitDot(d: Dot)
    method visitCircle(c: Circle)
    method visitRectangle(r: Rectangle)
    method visitCompoundShape(cs: CompoundShape)

// Concrete visitors implement several versions of the same
// algorithm, which can work with all concrete element classes.
//
// You can experience the biggest benefit of the Visitor pattern
// when using it with a complex object structure such as a
// Composite tree. In this case, it might be helpful to store
// some intermediate state of the algorithm while executing the
// visitor's methods over various objects of the structure.
class XMLExportVisitor implements Visitor is
    method visitDot(d: Dot) is
        // Export the dot's ID and center coordinates.

    method visitCircle(c: Circle) is
        // Export the circle's ID, center coordinates and
        // radius.

    method visitRectangle(r: Rectangle) is
        // Export the rectangle's ID, left-top coordinates,
        // width and height.

    method visitCompoundShape(cs: CompoundShape) is
        // Export the shape's ID as well as the list of its
        // children's IDs.


// The client code can run visitor operations over any set of
// elements without figuring out their concrete classes. The
// accept operation directs a call to the appropriate operation
// in the visitor object.
class Application is
    field allShapes: array of Shapes

    method export() is
        exportVisitor = new XMLExportVisitor()

        foreach (shape in allShapes) do
            shape.accept(exportVisitor)
```

## 💡 Ứng dụng

**Sử dụng Visitor khi bạn cần thực hiện thao tác trên tất cả các phần tử của cấu trúc đối tượng phức tạp (ví dụ: cây đối tượng).**

Pattern Visitor cho phép bạn thực hiện một thao tác trên một tập hợp các đối tượng có các lớp khác nhau bằng cách để một đối tượng visitor triển khai một số biến thể của cùng một thao tác, tương ứng với tất cả các lớp mục tiêu.

**Sử dụng Visitor để làm sạch logic nghiệp vụ của các hành vi phụ trợ.**

Visitor cho phép bạn làm cho các lớp chính của ứng dụng tập trung hơn vào công việc chính của chúng bằng cách trích xuất tất cả các hành vi khác vào một tập hợp các lớp visitor.

**Sử dụng Visitor khi một hành vi chỉ có ý nghĩa trong một số lớp của hệ thống phân cấp lớp, nhưng không có ý nghĩa trong các lớp khác.**

Bạn có thể trích xuất hành vi này thành một lớp visitor riêng biệt và chỉ triển khai những phương thức truy cập chấp nhận các đối tượng của các lớp có liên quan, để trống phần còn lại.

## 📋 Triển khai

1. Khai báo interface visitor với một tập hợp các phương thức “ghé thăm”, một phương thức cho mỗi lớp phần tử cụ thể tồn tại trong chương trình.

2. Khai báo interface phần tử. Nếu bạn đang làm việc với hệ thống phân cấp lớp phần tử hiện có, hãy thêm phương thức trừu tượng "accept" vào lớp cơ sở của hệ thống phân cấp. Phương thức này phải chấp nhận một đối tượng visitor làm tham số.

3. Thực hiện các phương pháp chấp nhận trong tất cả các lớp phần tử cụ thể. Các phương thức này chỉ phải chuyển hướng cuộc gọi đến một phương thức thăm trên đối tượng visitor đến phù hợp với lớp của phần tử hiện tại.

4. Các lớp phần tử chỉ nên hoạt động với visitor thông qua interface visitor. Tuy nhiên, visitor phải biết tất cả các lớp phần tử cụ thể, được tham chiếu như các kiểu tham số của các phương thức truy cập.

5. Đối với mỗi hành vi không thể được triển khai bên trong phân cấp phần tử, hãy tạo một lớp visitor cụ thể mới và triển khai tất cả các phương pháp truy cập.

    Bạn có thể gặp phải tình huống trong đó visitor sẽ cần quyền truy cập vào một số thành viên riêng tư của lớp phần tử. Trong trường hợp này, bạn có thể đặt các trường hoặc phương thức này ở chế độ công khai, vi phạm tính đóng gói của phần tử hoặc lồng lớp visitor vào lớp phần tử. Điều sau chỉ có thể thực hiện được nếu bạn may mắn làm việc với ngôn ngữ lập trình hỗ trợ các lớp lồng nhau.

6. Client phải tạo các đối tượng visitor và chuyển chúng vào các phần tử thông qua các phương thức "accept".

## ⚖️ Ưu nhược điểm

### Ưu điểm

*Open/Closed Principle*. Bạn có thể thêm một hành vi mới có thể hoạt động với các đối tượng của các lớp khác nhau mà không cần thay đổi các lớp này.

*Single Responsibility Principle*. Bạn có thể chuyển nhiều phiên bản của cùng một hành vi vào cùng một lớp.

 Một đối tượng visitor có thể tích lũy một số thông tin hữu ích khi làm việc với nhiều đối tượng khác nhau. Điều này có thể hữu ích khi bạn muốn duyệt qua một số cấu trúc đối tượng phức tạp, chẳng hạn như cây đối tượng và áp dụng visitor vào từng đối tượng của cấu trúc này.

### Nhược điểm

Bạn cần cập nhật tất cả visitor mỗi khi một lớp được thêm vào hoặc xóa khỏi hệ thống phân cấp phần tử.

Visitor có thể thiếu quyền truy cập cần thiết vào các trường riêng tư và phương pháp của các phần tử mà họ phải làm việc với.

## 🔁 Quan hệ với các pattern khác

Bạn có thể coi **Visitor** như một phiên bản mạnh mẽ của **Command**. Các đối tượng của nó có thể thực thi các hoạt động trên các đối tượng khác nhau của các lớp khác nhau.

Bạn có thể sử dụng **Visitor** cùng với **Iterator** để xem qua một cấu trúc dữ liệu phức tạp và thực hiện một số thao tác trên các phần tử của nó, ngay cả khi tất cả chúng đều có các lớp khác nhau

Bạn có thể sử dụng **Visitor** để thực hiện một hoạt động trên toàn bộ cây **Composite**.

# Nguồn

[**refactoring**](https://refactoring.guru/design-patterns/template-method)