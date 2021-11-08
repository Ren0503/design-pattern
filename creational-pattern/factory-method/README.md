# Factory Method

## Mục đích

**Factory method** là một design pattern thuộc nhóm Creational, nó cung cấp một interface để tạo đối tượng cho lớp cha (superclass), nhưng cũng cho phép các lớp con (subclass) thay đổi đối tượng sẽ được tạo.

![intent](./assets/intent.png)

## Vấn đề

Tưởng tượng bạn đang tạo một ứng dụng quản lý chuỗi cung ứng. Phiên bản đầu tiên của ứng dụng chỉ quản lý vận chuyển cho các xe tải, thế nên phần lớn code của bạn sẽ nằm trong lớp `Truck`. 

Sau đó ứng dụng của bạn ngày càng phổ biến và bạn nhận được yêu cầu từ các công ty hàng hải để hợp nhất chuỗi cung ứng qua đường biển vào ứng dụng. Đấy là một thông tin tuyệt vời! Nhưng còn code thì sao?

![problem](./assets/problem.png)

*Việc thêm một lớp mới vào ứng dụng không hề đơn giản nếu phần lớn code đã được kết nối với các lớp hiện có.*

Hiện tại hầu hết code của bạn đã được ghép với clas `Truck`. Việc thêm `Ship` vào ứng dụng sẽ yêu cầu các thay đổi với toàn bộ codebase. Và nếu bạn thêm một phương tiện vận tải nào nữa vào ứng dụng, thì bạn sẽ thay đổi code lần nữa.

Kết quả là bạn có một đống code tạp nham với rất nhiều điều kiện thay đổi của ứng dụng tùy thuộc vào loại đối tượng vận chuyển.

## Giải pháp

Pattern Factory Method gợi ý giải pháp là thay vì tạo đối tượng qua các lệnh khởi tạo trực tiếp (sử dụng toán tử `new`) thì hãy tạo bằng cách gọi phường thức *factory*. Lưu ý là đối tượng vẫn được tạo thông qua toán tử `new`, nhưng nó sẽ được gọi từ trong phương thức *factory*. Các đối tượng được trả về theo phương thức factory thường được gọi là **products**.

![solution1](./assets/solution1.png)

*Các lớp con có thể chỉnh sửa đối tượng trả về từ phương thức factory*

Thoạt nhìn, thay đổi này có vẻ vô nghĩa: chúng ta chỉ chuyển lệnh gọi *constructor* từ phần này sang phần khác của chương trình. Tuy nhiên, hãy xem xét thật kỹ lưỡng : bây giờ bạn có thể ghi đè(override) phương thức factory trong một lớp con và thay đổi `product` đang được tạo bởi phương thức này.

Song, nó vẫn có một hạn chế nhỏ: các lớp con có thể trả về các kiểu `product` khác nhau chỉ khi các `product` này có lớp cơ sở hoặc interface chung. Ngoài ra, phương thức factory trong lớp cơ sở nên có kiểu trả về được khai báo là interface này. 

![solution2](./assets/solution2.png)

Ví dụ, cả hai lớp `Truck` và `Ship` đều được triển khai từ interface `Transport`, interface này khai báo một phương thức là `deliver`. Mỗi lớp sẽ triển khai phương thức này theo cách khác nhau, xe tải (truck) sẽ phân phối (deliver) hàng hoá theo đường bộ, còn tàu(ship) sẽ phân phối theo đường biển. Phương thức factory `RoadLogistics` sẽ trả về đối tượng `Truck`, còn `SeaLogistics` sẽ trả về đối tượng `Ship`.

![solution3](./assets/solution3.png)

Đoạn code sử dụng phương thức factory (thường được gọi là *client code*), không nhìn thấy sự khác biệt giữa những `product` trả về bởi các lớp con khác nhau. Client coi tất cả `product` là lớp trừu tượng **Transport**, đồng thời nó cũng biết các đối tượng transport phải có phương thức deliver. Nhưng chi tiết cách hoạt động thì nó không cần quan tâm.

## Cấu trúc

![structure](./assets/structure.png)

1. **Product** là interface chung cho tất cả đối tượng có thể được tạo ra bởi creator hay các lớp con của nó.
2. **Concrete Product** là các triển khai khác nhau từ interface **Product**. Tạm hiểu là product con.
3. **Creator** lớp này khai báo một phương thức factory trả về đối tượng product mới. Kiểu trả về của phương thức này phải tương ứng với interface **Product**.

Bạn có thể định nghĩa phương thức factory là trừu tượng để tất cả lớp con triển khai phiên bản riêng của chúng. Và phương thức factory cơ sở sẽ trả về các kiểu product mặc định.

4. **Concreta Creator** sẽ ghi đè (override) phương thức factory cơ sở để trả về một kiểu product mới. Không phải lúc nào phương thức factory cũng tạo ra một đối tượng mới, nó có thể trả về đối tượng đã tồn tại từ cache, object pool hay từ một nguồn nào đó.

## Mã giả

Ví dụ này minh hoạ cách phương thức Factory có thể sử dụng để tạo phần tử UI đa nền tảng mà không cần ghép clietn coide với lớp UI cụ thể.

![pseudocode](./assets/pseudocode.png)

Lớp dialog cơ sở dùng hiển thị các phần tử UI khác nhau cho hiển thị cửa sổ. Dưới các hệ điều hành khác nhau, các phần tử này có thể có vài khác biệt nhỏ, song nó vẫn phải đồng nhất. Button trên Window vẫn là button trên Linux.

Khi sử dụng phương thức factory, bạn không cần viết lại các logic cho dialog vớI từng hệ điều hành. Nếu ta khai báo phương thức factory để tạo button trong lớp dialog, sau này ta có thể tạo các lớp con trả về button Windows-styled từ phương thức factory. Lớp con sau khi kế thừa phần lớn code dialog từ lớp cơ sở, nhưng nhờ vào phương thức factory ta có thể hiện thị các button trông giống như window trên màn hình.

Với pattern này khi làm việc, các lớp cơ sở dialog phải làm việc với button trừu tượng: lớp trừu tượng hoặc interface cho tất cả concrete button. Với cách này, đoạn code còn lại của dialog vẫn hoạt động, dù phải làm việc với bất kỳ kiểu button nào.

Tất nhiên, bạn có thể dùng cách này cho các phần tử UI khác. Tuy nhiên, với mỗi phương thức factory mà bạn thêm vào diago, ta sẽ dần tiến đến Abstract Factory pattern. Ta sẽ nói về pattern này ở các bài viết sau.

```c
// Lớp creator khai báo phương thức factory phải trả về
// đối tượng của lớp product. Lớp con của creator tạo
// các triển khai khác của phương thức.

// Creator có thể tạo các triển khai mặc định cho
// phương thức factory.
class Dialog is

    abstract method createButton():Button

    // Lưu ý, dù tên là creator, song đấy không phải nhiệm vụ chính
    // có nó là tạo product. Nó được dùng để chứa nhưng logic 
    // business cốt lõi dựa trên đối tượng product trả về từ phương
    // thức factory. Các lớp con có thể gián tiếp thay đổi logic
    // bằng cách override lên phương thức factory và trả về kiểu 
    // product khác từ nó.
    method render() is
        // Gọi phương thức factory để tạo đối tượng product.
        Button okButton = createButton()
        // Sử dụng product.
        okButton.onClick(closeDialog)
        okButton.render()


// Concrete creator ghi đè lên phương thức factory để 
// thay đổi kiểu product trả về.
class WindowsDialog extends Dialog is
    method createButton():Button is
        return new WindowsButton()

class WebDialog extends Dialog is
    method createButton():Button is
        return new HTMLButton()

// Interface product khai báo phương thức cho tất cả 
/// concrete product cần triển khai.
interface Button is
    method render()
    method onClick(f)

// Concrete product tạo ra các triển khai với interface product.
class WindowsButton implements Button is
    method render(a, b) is
        // Render a button in Windows style.
    method onClick(f) is
        // Bind a native OS click event.

class HTMLButton implements Button is
    method render(a, b) is
        // Return an HTML representation of a button.
    method onClick(f) is
        // Bind a web browser click event.


class Application is
    field dialog: Dialog

    // Ứng dụng chon kiểu creator dựa trên cấu hình 
    // hiện tại hoặc môi trường thiết lập.
    method initialize() is
        config = readApplicationConfigFile()

        if (config.OS == "Windows") then
            dialog = new WindowsDialog()
        else if (config.OS == "Web") then
            dialog = new WebDialog()
        else
            throw new Exception("Error! Unknown operating system.")

    // Client code làm việc với thực thể của concrete creator,
    // dù thông qua interface cơ sở. Miễn là client vẫn làm việc
    // create thông qua interface, bạn có thể chuyển nó vào bất
    // kù lớp con nào của creator.
    method main() is
        this.initialize()
        dialog.render()
```

## Ứng dụng

**Sử dụng phương thức Factory khi bạn không biết chính xác kiểu và dependencies của đối tượng mà code bạn sẽ làm việc**

Phương pháp Factory phân tách code khởi tạo product với code sử dụng lại product. Do đó việc mở rộng code khởi tạo product với phần code còn lại sẽ dễ dàng hơn.