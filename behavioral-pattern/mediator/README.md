# Mediator

## 📜 Mục đích

Mediator là một desgin pattern dạng behavioral giúp bạn giảm các phụ thuộc hỗn tạp giữa các đối tượng. Pattern hạn chế các giao tiếp trực tiếp giữa các đối tượng và buộc nó giao tiếp thông qua đối tượng mediator.

![intent](,/assets/intent.png)

## 😟 Vấn đề

Giả sử bạn có một dialog cho tạo và chỉnh sửa thông tin khách hàng. Nó bạn gồm các form khác nhau như text input, checkbox, button, ...

![problem1](./assets/problem1.png)

Một số phần tử trong form có thể tương tác với nhau. Ví dự, khi chọn "I have a dog" ở một chechbox có thể sẽ dẫn đến hiện đến một input ẩn cho nhập tên chú chó đó. Hay  khi submit một button sẽ phải xác thực các giá trị hợp lệ ở tất cả trường trước khi lưu dữ liệu.

![problem2](./assets/problem2.png)

*Các phần tử có quan hệ với nhau, nên thay đổi một phần tử có thể ảnh hưởng đến những cái khác*

By having this logic implemented directly inside the code of the form elements you make these elements’ classes much harder to reuse in other forms of the app. For example, you won’t be able to use that checkbox class inside another form, because it’s coupled to the dog’s text field. You can use either all the classes involved in rendering the profile form, or none at all.

Bằng cách triển khai trực tiếp logic bên trong code của phần tử form bạn sẽ làm cho lớp phần tử khó tái sử dụng ở các form khác trong ứng dụng. Ví dụ bạn không thể dùng lớp chechbox này cho các form khác vì nó đã được kết nối với input "tên chó". Bạn có thể sử dụng tất cả các lớp liên quan đến việc hiển thị form người dùng, hoặc không có lớp nào cả.

![problem2](./assets/problem2.png)

## 😊 Giải pháp

Mediator đề nghị giải pháp là bạn nên dừng việc kết nối trực tiếp giữa các thành phần mà bạn muốn nó trở nên độc lập. Thay vào đó, các thành phần này sẽ phải cộng tác gián tiếp qua việc gọi một đối tượng mediator đặc biệt, đối tượng này mới là thứ gọi trực tiếp đến các thành phần thích hợp. Kết quả các thành phần chỉ phụ thuộc vào lớp mediator đơn nhất thay vì được ghép nối với hàng chục  thành phần khác.

In our example with the profile editing form, the dialog class itself may act as the mediator. Most likely, the dialog class is already aware of all of its sub-elements, so you won’t even need to introduce new dependencies into this class.

Trong ví dụ với form hồ sơ người dùng, lớp diago sẽ hành động như một mediator. Rất có thể, lớp dialog đã nhận thức được các phần tử con của nó, thế nên bạn không cần thêm phụ thuộc mới vào lớp.

![solution1](./assets/solution1.png)

Đây là một thay đổi có ý nghĩa to lớn với các phần tử trong form. Như với button submit. Trước đây mỗi lần người dùng click vào button, nó phải xác thực giá trị hợp lệ của tất cả phần tử riêng biệt trong form. Giờ đây nó chỉ có một công việc là thông báo cho dialog về thao tác click. Khi nhận được thông báo, dialog thực hiện xác thực bản thân nó hoặc truyền công việc cho các phần tử riêng biệt. Do đó thay vì bị ràng buộc với hàng tá phần tử trong form, button chỉ phụ thuộc vào dialog.

Bạn có thể làm nhiều là nới lỏng các ràng buộc bằng việc trích xuất interface chung cho tất cả kiểu dialog. Interface sẽ khai báo phương thức thông báo cho tất cả phần tử của form để thông báo đến dialog mỗi khi có sự kiện gì diễn ra với bọn chúng. Do đó, button submit của ta bây giờ có thể làm việc với bất kỳ dialog nào triển khai interface này.

Cách này, Mediator giúp bạn gói một trang web phức tạp với các đối tượng có quan hệ khác nhau vào trong một đối tượng mediator đơn giản. Ít ràng buộc và phụ thuộc hơn, sẽ giúp nó dễ thay đổi, mở rộng và tái sử dụng hơn.

## 🚗 Thế Giới Thực

![analogy](./assets/analogy.png)

Các phi công của máy bay tiếp cận hoặc rời khỏi khu vực kiểm soát của sân bay không phải liên lạc trực tiếp với nhau. Thay vào đó, họ nói chuyện với một nhân viên kiểm soát không lưu, người ngồi trong một tòa tháp cao ở đâu đó gần đường băng. Nếu không có kiểm soát viên không lưu, các phi công sẽ cần phải biết về mọi máy bay trong khu vực lân cận sân bay, thảo luận về các ưu tiên hạ cánh với một ủy ban gồm hàng chục phi công khác. Điều đó có thể sẽ làm tăng vọt số liệu thống kê về các vụ tai nạn máy bay.

Tháp không cần điều khiển toàn bộ chuyến bay. Nó chỉ tồn tại để thực thi các ràng buộc trong khu vực cuối vì số lượng các máy bay ở đó có thể quá tải đối với một phi công.

## 🏢 Cấu trúc

![structure](./assets/structure.png)

1. **Component** là các lớp khác nhau bao gồm các logic nghiệp vụ. Mỗi component có một tham chiếu đến một mediator, khai báo kiểu của interface mediator. Component không cần biết về lớp thực sự của mediator, nên bạn có thể sử dụng lại component cho các chương trình khác bằng cách liên kết nó với một mediator khác.
2. **Mediator** là interface khai báo phương thức giao tiếp giữa các component, nó thường khai báo một phương thức thông báo duy nhất. Component có thể truyền bất kỳ ngữ cảnh nào như các tham số của phương thức này bao gồm cả đối tượng của chúng, nhưng chỉ trong trường hợp không diễn ra kết ghép giữa component nhận và lớp của người gửi.
3. *Concrete Mediator** đóng gói quan hệ giữa các component khác nhau. Concrete mediator thường giữ tham chiếu để tất cả component nó quản lý và thỉnh thoảng quản lý cả vòng đời của chúng.
4. Component không phải biết về các component khác. Nếu một điều gì quan trọng diễn ra với một component, nó chỉ việc thông báo đến mediator. Khi mediator nhận thông báo nó có thể xác định người gửi dễ dàng, chỉ như vậy là đủ để quyết định component nào sẽ được kích hoạt khi trả về.

    Từ góc nhìn của một component, tất cả trông giống như một hộp đen. Người gửi không biết ai sẽ xử lý yêu cầu của mình và người nhận không biết ai đã gửi yêu cầu ngay từ đầu.


## 👨‍💻 Mã giả

Trong ví dụ này, Mediator  giúp bạn loại bỏ sự phụ thuộc lẫn nhau giữa các lớp UI khác nhau: button, checkbox và text labels.

![pseudocode](./assets/pseudocode.png)

Một phần tử được kích hoạt bởi người dùng, không cần giao tiếp trực tiếp với các phần tử khác. Thay vào đó, các phần tử chỉ cần cho mediator của chúng biết khi có sự kiện diễn ra, truyền thông tin ngữ cảnh cùng với thông báo.

Trong ví dụ này, các dialog hành động như một mediator. Nó biết làm thế nào để các phần tử cụ thể cộng tác với nhau và tạo điều kiến cho chúng kết nối gián tiếp với nhau. Mỗi khi nhận thông báo về một sự kiện, dialog quyết định phần tử nào sẽ giải quyết và chuyền hướng lệnh gọi phù hợp.

```c
// Interface mediator khai báo một phương thức được dùng bởi
// các component để thông báo cho mediator về các sự kiện khác
// nhau. Mediator sẽ phản ứng với sự kiện và truyền thực thi
// cho các component khác.
interface Mediator is
    method notify(sender: Component, event: string)


// The concrete mediator class. The intertwined web of
// connections between individual components has been untangled
// and moved into the mediator.
class AuthenticationDialog implements Mediator is
    private field title: string
    private field loginOrRegisterChkBx: Checkbox
    private field loginUsername, loginPassword: Textbox
    private field registrationUsername, registrationPassword,
                  registrationEmail: Textbox
    private field okBtn, cancelBtn: Button

    constructor AuthenticationDialog() is
        // Create all component objects and pass the current
        // mediator into their constructors to establish links.

    // When something happens with a component, it notifies the
    // mediator. Upon receiving a notification, the mediator may
    // do something on its own or pass the request to another
    // component.
    method notify(sender, event) is
        if (sender == loginOrRegisterChkBx and event == "check")
            if (loginOrRegisterChkBx.checked)
                title = "Log in"
                // 1. Show login form components.
                // 2. Hide registration form components.
            else
                title = "Register"
                // 1. Show registration form components.
                // 2. Hide login form components

        if (sender == okBtn && event == "click")
            if (loginOrRegister.checked)
                // Try to find a user using login credentials.
                if (!found)
                    // Show an error message above the login
                    // field.
            else
                // 1. Create a user account using data from the
                // registration fields.
                // 2. Log that user in.
                // ...


// Components communicate with a mediator using the mediator
// interface. Thanks to that, you can use the same components in
// other contexts by linking them with different mediator
// objects.
class Component is
    field dialog: Mediator

    constructor Component(dialog) is
        this.dialog = dialog

    method click() is
        dialog.notify(this, "click")

    method keypress() is
        dialog.notify(this, "keypress")

// Concrete components don't talk to each other. They have only
// one communication channel, which is sending notifications to
// the mediator.
class Button extends Component is
    // ...

class Textbox extends Component is
    // ...

class Checkbox extends Component is
    method check() is
        dialog.notify(this, "check")
    // ...
```