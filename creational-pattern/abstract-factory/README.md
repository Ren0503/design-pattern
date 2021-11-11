# 📜 Mục đích

**Abstract Factory** là một design pattern thuộc nhóm creational, dùng để tạo ra các đối tượng có quan hệ gần gũi với nhau mà không cần dùng đến concrete class cụ thể.

![intent](./assets/intent.png)

# 😟 Vấn đề

Giả sử bạn đang tạo một trang bán đồ nội thất. Code của bạn bao gồm các lớp sau:
1. Các sản phẩm có quan hệ gần gũi như: `Sofa`, `Chair` và `CoffeTable`.
2. Các biến thể của nhóm sản phẩm đó. Ví dụ như nhóm `Sofa` + `Chair` + `CoffeTable` có các biến thể như `Modern`, `Victorian` và `ArtDeco`.

![problem](./assets/problem.png)

Bạn cần có cách để khi tạo một đồ vật nội thất đơn lẻ, nó phải phù hợp với các đồ vật khác trong nhóm của nó. Khách hàng sẽ khó chịu khi họ nhận về những đồ vật trong nhóm có biến thể khác nhau.

![problem1](./assets/problem1.png)

Bên cạnh đó, bạn không muốn thay đổi code mỗi khi thêm sản phẩm hoặc nhóm sản phẩm trong chương trình. Danh mục nội thất được cập nhật rất thường xuyên, và bạn không muốn thay đổi code mỗi khi nó diễn ra.

# 😊 Giải pháp

Việc đầu tiên cần làm theo thiết kế Abstract Factory là khai báo inteface rõ ràng cho mỗi sản phẩm riêng biệt trong nhóm sản phẩm. Và tạo tất cả biến thể của sản phẩm theo sao inteface đó. Ví dụ tất cả biến thể của ghế được triển khai trong interface `Chair`, tất cả sofa được triển khai trong interface `Sofa` ,...

![solution1](./assets/solution1.png)

Bước tiếp theo là khai báo *Abstract Factory* - là interface chứa tất cả phương thức tạo cho tất cả sản phẩm trong nhóm sản phẩm (vd: `createChair`, `createSofa` và `createCoffeTable`).Các phương thức này trả về một kiểu sản phẩm **abstract** được biểu diễn bởi interface chúng ta trích xuất trước đó: `Chair`, `Sofa`, `CoffeTable`,...

![solution2](./assets/solution2.png)

Vậy còn các biến thể của sản phẩm? Với từng biến thể của nhóm sản phẩm, ta tạo ra một lớp factory riêng biệt dựa trên interface **Abstract Factory**. Factory là lớp trả về kiểu sản phẩm riêng biệt. Ví dụ, `ModernFurnitureFactory` có thể tạo ra các đối tượng `ModernChair`, `ModernSofa` hay `ModernCoffeTable`.

Client code làm việc với factory hay sản phẩm thông qua abstract interface. Thế nên bạn có thể thay đổi kiểu factory hay biến thể của sản phẩm cho client code nhận mà không gây ra bất kỳ lỗi gì.

![solution3](./assets/solution3.png)

Giả sử client muốn một factory để tạo ghế (chair). Nó sẽ không cần quan tâm loại của lớp factory đó, cũng như kiểu ghế nhận về. Dù là Modern hay Victorian, nó cũng sẽ xử lý theo cùng một cách là thông qua abstract interface `Chair`. Với cách tiếp cận này client chỉ cần quan tâm là ghế sẽ triển khai phương thức `sitOn` như thế nào. Bên cạnh đó, bất kỳ biến thể nào trả về từ chair, nó cũng sẽ phù hợp với sofa và coffe table được tạo cùng đối tượng factory.

Nếu bạn thắc mắc: client chỉ làm việc với Abstract interface, vậy thì cái gì sẽ tạo ra factory?. Thông thường ứng dụng sẽ tạo đối tượng concrete factory ở giai đoạn khởi tạo, nhưng trước đó ứng dụng sẽ tạo factory dựa trên kiểu cấu hình hoặc thiết lập môi trường.

🏢 Cấu trúc

![structure](./assets/structure.png)

1. **Abstract Product** khai báo inteface cho các sản phẩn riêng biệt nhưng có quan hệ với nhau tạo nên một nhóm sản phẩm.
2. **Concrete Product** là các triển khai biến thể của abstract product, được gom nhóm theo biến thể. Mỗi abstract product (chair/sofa) sẽ được triển khai tất cả biến thể (modern, victorian).
3. **Abstract Factory** interface khai báo tập hợp phương thức khởi tạo cho từng abstract product.
4. **Concrete Factory** là triển khai phương thức khởi tạo của abstract factory. Mỗi concrete factory tương ứng với biến thể cụ thể của sản phẩm và chỉ tạo sản phẩm theo biến thể đó.
5. Mặc dù concrete factory tạo ra các concrete product, nhưng chữ ký của phương thức khởi tạo trả về sẽ tương ứng với abstract product. Với cách này client code sử dụng factory sẽ không cần quan tâm tới biến thể cụ thể của sản phẩm từ factory. Nó có thể làm việc với bất kỳ biến thể nào miễn là giao tiếp với các đối tượng thông qua abstract interface.

# 👨‍💻 Mã giả

Ví dụ này minh hoạ cách Abstract Factory có thể sử dụng để tạo các phần tử UI đa nền tảng mà không cần ghép client code với lớp UI cụ thể, đồng thời giữ cho tất cả các phần tử được tạo nhất quán với hệ điều hành đã chọn

![pseudocode](./assets/pseudocode.png)

Các phần tử UI trên các ứng dụng đa nền tảng sẽ được triển khai giống nhau, sẽ có một chút khác biệt trên các hệ điều hành khác nhau. Hơn nữa, nhiệm vụ của bạn là đảm bảo style của các phần tử UI phù hợp với hệ điều hành hiện tại. Bạn sẽ không muốn chương trình hiển thị MacOS control khi được thực thi trên Windows.

Abstract Factory sẽ khai báo tập hợp các phương thức khởi tạo mà client code có thể dùng để tạo các kiểu phần tử UI khác nhau. Concrete factory tương ứng với hệ điều hành cụ thể sẽ tạo ra các phần tử UI phù hợp với hệ điều hành đó.

Nó hoạt động như sau: khi ứng dụng bắt đầu chạy, nó sẽ kiểm tra loại hệ điều hành hiện tại. Ứng dụng sẽ dùng thông tin đó để tạo ra một đối tượng factory từ lớp tương ứng với hệ điều hành. Các phần còn lại sẽ dùng factory để tạo ra phần tử UI. Điều này ngăn việc tạo các phần tử UI sai lệch.

Với cách tiếp cận này, client code không phụ thuộc concrete class của factory hay phần tử UI, miễn là nó làm việc với các đối tượng thông qua abstract factory. Không những thế, client code còn hỗ trợ các factory khác và phần tử UI bạn thêm vào trong tương lai.

Như vậy bạn không cần chỉnh sửa client code mỗi lần thêm biến thể của phần tử UI trong ứng dụng. Bạn chỉ cần tạo một lớp factory mới tạo ra các phần tử này và sửa đổi một chút code khởi tạo để ứng dụng chọn lớp đó khi thích hợp.

```c
// The abstract factory interface declares a set of methods that
// return different abstract products. These products are called
// a family and are related by a high-level theme or concept.
// Products of one family are usually able to collaborate among
// themselves. A family of products may have several variants,
// but the products of one variant are incompatible with the
// products of another variant.
interface GUIFactory is
    method createButton():Button
    method createCheckbox():Checkbox


// Concrete factories produce a family of products that belong
// to a single variant. The factory guarantees that the
// resulting products are compatible. Signatures of the concrete
// factory's methods return an abstract product, while inside
// the method a concrete product is instantiated.
class WinFactory implements GUIFactory is
    method createButton():Button is
        return new WinButton()
    method createCheckbox():Checkbox is
        return new WinCheckbox()

// Each concrete factory has a corresponding product variant.
class MacFactory implements GUIFactory is
    method createButton():Button is
        return new MacButton()
    method createCheckbox():Checkbox is
        return new MacCheckbox()


// Each distinct product of a product family should have a base
// interface. All variants of the product must implement this
// interface.
interface Button is
    method paint()

// Concrete products are created by corresponding concrete
// factories.
class WinButton implements Button is
    method paint() is
        // Render a button in Windows style.

class MacButton implements Button is
    method paint() is
        // Render a button in macOS style.

// Here's the base interface of another product. All products
// can interact with each other, but proper interaction is
// possible only between products of the same concrete variant.
interface Checkbox is
    method paint()

class WinCheckbox implements Checkbox is
    method paint() is
        // Render a checkbox in Windows style.

class MacCheckbox implements Checkbox is
    method paint() is
        // Render a checkbox in macOS style.


// The client code works with factories and products only
// through abstract types: GUIFactory, Button and Checkbox. This
// lets you pass any factory or product subclass to the client
// code without breaking it.
class Application is
    private field factory: GUIFactory
    private field button: Button
    constructor Application(factory: GUIFactory) is
        this.factory = factory
    method createUI() is
        this.button = factory.createButton()
    method paint() is
        button.paint()


// The application picks the factory type depending on the
// current configuration or environment settings and creates it
// at runtime (usually at the initialization stage).
class ApplicationConfigurator is
    method main() is
        config = readApplicationConfigFile()

        if (config.OS == "Windows") then
            factory = new WinFactory()
        else if (config.OS == "Mac") then
            factory = new MacFactory()
        else
            throw new Exception("Error! Unknown operating system.")

        Application app = new Application(factory)
```

# 💡 Ứng dụng

**🐞 Sử dụng Abstract Factory khi bạn cần làm việc với nhiều biến thể của một nhóm sản phẩm, mà bạn không muốn phụ thuộc vào concrete class của sản phẩm đó - chúng có thể chưa biết trước hoặc đơn giản là bạn muốn mở rộng trong tương lai.**

⚡  Abstract Factory cung cấp cho bạn interface để tạo các đối tượng từ mỗi lớp trong nhóm sản phầm miễn là code của bạn tạo đối tượng thông qua interface, bạn sẽ không phải lo lắng các vấn để tạo sai biến thể của sản phẩm hay không phù hợp với sản phẩm đã tạo trong ứng dụng.

📋 Triển khai