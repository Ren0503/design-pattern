# Command

## 📜 Mục đích

**Command** là một design pattern thuộc nhóm behavioral, nó biến một yêu cầu thành một đối tượng độc lập bao gồm tất cả thông tin của yêu cầu. Chuyển đổi này giúp bạn truyền các yêu cầu dưới dạng đối số của phương thức, trì hoãn hoặc chờ đợi việc thực thi một yêu cầu và hỗ trợ các hoạt động hoàn tác. 

![intent](./assets/intent.png)

## 😟 Vấn đề

Tưởng tượng bạn đang làm việc với một ứng dụng soạn thảo văn bản. Công việc hiện tại của bạn là tạo một thanh công cụ với nhóm button cho các thao tác khác nhau của editor. Bạn đã tạo một lớp `Button` gọn gàng để có thể dùng cho các button khác của thanh công cụ, cũng như cho các button chung ở các cửa sổ khác.

![problem1](./assets/problem1.png)

Trong khi tất cả button này trông giống nhau, thì chúng lại hỗ trợ những công việc khác nhau. 

Vậy bạn sẽ đặt code cho các xử lý thao tác click khác nhau của chúng ở đâu ? Giải pháp đơn giản nhất là tạo hàng nghìn lớp con cho từng nơi mà button được sử dụng. Các lớp con này sẽ bao gồm code cho thực thi thao tác click.

![problem2](./assets/problem2.png)

Rất nhanh chóng, bạn nhận ra cách tiếp cận này có rất nhiều thiếu sót. Đầu tiên, bạn sẽ có một số lượng rất lớn lớp con, và nó sẽ không ổn khi bạn sửa đổi lớp `Button` cơ sở vì bạn phải thay đổi tất cả các lớp con của nó. Nói một cách đơn giản, code GUI của bạn đã trở nên phụ thuộc một cách khó hiểu vào những đoạn code dễ thay đổi của logic nghiệp vụ. 

![problem3](./assets/problem3.png)

Và phần tồi tệ hơn ở đây. Một vài thao tác như copy/paste, sẽ cần được gọi từ rất nhiều nơi. Ví dụ, người dùng có thể click vào button "Copy" trên thanh công cụ, hoặc thực hiện thông quan menu hay chỉ đơn giản là Ctrl+C trên bàn phím.

Ban đầu, khi ứng dụng của bạn chỉ có một thanh công cụ, có thể đặt việc triển khai các hoạt động khác nhau vào các lớp con của button. Nói cách khác, ta có code để sao chép văn bản bên trong lớp con `CopyButton`. Nhưng sau đó, khi bạn triển khai menu, lối tắt và những thứ khác, bạn phải sao chép code của thao tác trong nhiều lớp hoặc làm cho menu phụ thuộc vào các button, mọi thứ sẽ trở nên tệ hoặc tệ hơn nữa.

## 😊 Giải pháp

Một thiết kế phần mềm tốt thường dựa trên *nguyên tắc tách biệt các mối quan tâm*, điều này thường dẫn đến việc chia ứng dụng thành nhiều lớp. Ví dụ phổ biến nhất: một lớp cho giao diện người dùng đồ họa và một lớp khác cho logic nghiệp vụ. Lớp GUI chịu trách nhiệm hiển thị hình ảnh đẹp mắt trên màn hình, thu nhận bất kỳ đầu vào nào và hiển thị kết quả về những gì người dùng và ứng dụng đang làm. Tuy nhiên, khi cần làm điều gì đó quan trọng, như tính toán quỹ đạo của mặt trăng hoặc soạn báo cáo hàng năm, lớp GUI sẽ ủy quyền công việc cho lớp logic nghiệp vụ cơ bản.

Trong đoạn code, nó có thể trông như thế này: một đối tượng GUI gọi một phương thức của đối tượng logic nghiệp vụ, truyền cho nó một số đối số. Quá trình này thường được mô tả là một đối tượng gửi một yêu cầu khác.

![solution1](./assets/solution1.png)

Command gợi ý rằng các đối tượng GUI không nên gửi trực tiếp các yêu cầu này. Thay vào đó, bạn nên trích xuất tất cả các chi tiết yêu cầu, chẳng hạn như đối tượng được gọi, tên của phương thức và danh sách các đối số vào một lớp command riêng biệt với một phương thức kích hoạt yêu cầu này.

Các đối tượng command đóng vai trò là liên kết giữa các đối tượng GUI và logic nghiệp vụ khác nhau. Từ bây giờ, đối tượng GUI không cần biết đối tượng logic nghiệp vụ nào sẽ nhận được yêu cầu và cách xử lý yêu cầu. Đối tượng GUI chỉ cần kích hoạt command, nó sẽ xử lý tất cả các chi tiết.

![solution2](./assets/solution2.png)

Bước tiếp theo là làm cho các command của bạn triển khai cùng một interface. Thông thường nó chỉ có một phương thức thực thi duy nhất mà không cần tham số. Interface này cho phép bạn sử dụng các command khác nhau với cùng một người gửi yêu cầu mà không cần kết hợp nó với các lớp command cụ thể. Như vậy, giờ đây bạn có thể chuyển đổi các đối tượng command được liên kết với người gửi, hay thay đổi một cách hiệu quả hành vi của người gửi trong thời gian chạy.

Bạn có thể nhận thấy một phần còn thiếu của vấn đề, đó là các tham số yêu cầu. Một đối tượng GUI có thể đã cung cấp cho đối tượng lớp nghiệp vụ một số tham số. Vì phương thức thực thi của command không có bất kỳ tham số nào, như vậy chúng ta sẽ chuyển các chi tiết yêu cầu đến người nhận như thế nào? Hóa ra command phải được cấu hình trước với dữ liệu này hoặc có khả năng tự lấy nó.

![solution3](./assets/solution3.png)

Hãy quay lại trình soạn thảo văn bản. Sau khi áp dụng Command, ta không còn cần đến tất cả các lớp con của button đó để thực hiện các hành vi click chuột khác nhau. Chỉ cần đặt một trường vào lớp `Button` cơ sở là đủ để lưu trữ tham chiếu đến đối tượng command và làm cho button thực hiện command đó khi click chuột.

Bạn sẽ triển khai một loạt các lớp command cho mọi hoạt động có thể và liên kết chúng với các button cụ thể, tùy thuộc vào hành vi dự kiến của các button.

Các phần tử GUI khác, chẳng hạn như menu, lối tắt hoặc toàn bộ hộp thoại, có thể được thực hiện theo cách tương tự. Chúng sẽ được liên kết với một command được thực thi khi người dùng tương tác với phần tử GUI. Như bạn có thể đoán bây giờ, các phần tử liên quan đến các hoạt động giống nhau sẽ được liên kết với các command giống nhau, ngăn chặn bất kỳ sự trùng lặp code nào.

Kết quả là, các command trở thành một lớp trung gian thuận tiện giúp giảm sự ghép nối giữa GUI và các lớp logic nghiệp vụ. Và đó chỉ là một phần nhỏ trong số những lợi ích mà Command có thể mang lại!

## 🚗 Thế Giới Thực

![analogy](./assets/analogy.png)

Sau khi đi bộ qua thành phố, bạn đến một nhà hàng sang trọng và ngồi vào bàn bên cửa sổ. Một người phục vụ thân thiện tiếp cận bạn và nhận đơn đặt hàng của bạn, viết nó ra một tờ giấy. Người phục vụ đi vào bếp và dán thứ tự lên tường. Sau một thời gian, đơn đặt hàng được chuyển đến đầu bếp, người sẽ đọc và nấu bữa ăn cho phù hợp. Người đầu bếp đặt bữa ăn vào khay cùng với thứ tự. Người phục vụ lấy khay, kiểm tra thứ tự để đảm bảo mọi thứ đều như bạn muốn và mang mọi thứ đến bàn của bạn.

Trật tự trên giấy dùng như một command. Nó vẫn còn trong hàng đợi cho đến khi đầu bếp sẵn sàng phục vụ nó. Đơn đặt hàng chứa tất cả các thông tin liên quan cần thiết để nấu bữa ăn. Nó cho phép đầu bếp bắt đầu nấu ăn ngay lập tức thay vì chạy xung quanh để làm rõ chi tiết đơn đặt hàng trực tiếp từ bạn.

## 🏢 Cấu trúc

![structure](./assets/structure.png)

1. **Sender** (hay còn gọi là invoker) là lớp chịu trách nhiệm khởi tạo các yêu cầu. Lớp này phải có một trường để lưu trữ một tham chiếu đến một đối tượng command. Sender(người gửi) kích hoạt command đó thay vì gửi yêu cầu trực tiếp đến receiver(người nhận). Lưu ý rằng sender không chịu trách nhiệm tạo đối tượng command. Thông thường, nó nhận một command được tạo trước từ client thông qua phương thức khởi tạo.
2. **Command** là interface, thường khai báo một phương thức đơn nhất để thực hiện lệnh.
3. **Concrete Command** thực hiện nhiều loại yêu cầu khác nhau. Một command cụ thể không được phép tự thực hiện công việc, mà chỉ chuyển lệnh gọi đến một trong các đối tượng logic nghiệp vụ. Tuy nhiên, để đơn giản hóa code, các lớp này có thể được hợp nhất.
Các tham số cần thiết để thực thi một phương thức trên một đối tượng nhận có thể được khai báo dưới dạng các trường trong command cụ thể. Bạn có thể làm cho các đối tượng command trở nên bất biến bằng cách chỉ cho phép khởi tạo các trường này thông qua phương thức khởi tạo.
4. **Receiver** là lớp chứa một số logic nghiệp vụ. Hầu như bất kỳ đối tượng nào cũng có thể hoạt động như một receiver. Hầu hết các command chỉ xử lý các chi tiết về cách một yêu cầu được chuyển đến receiver, trong khi receiver phải tự thực hiện công việc thực tế.
5. **Client** tạo và cấu hình các đối tượng command cụ thể. Client phải chuyển tất cả các tham số yêu cầu, bao gồm cả sender, vào phương thức khởi tạo của command. Sau đó, command kết quả có thể được liên kết với một hoặc nhiều receiver.

## 👨‍💻 Mã giả

Trong ví dụ này, Command giúp bạn theo dõi lịch sử các thao tác thực thi và hoàn tác nó nếu cần thiết.

![pseudocode](./assets/pseudocode.png)

Command dẫn đến các thay đổi trạng thái của editor (sao chép, cắt, dán) và sao lưu bản dự phòng trạng thái của editor trước khi thực thi một thao tác liên kết với command. Sau khi command thực thi, nó lưu vào lịch sử command(một ngăn xếp các đối tượng command) cùng với bản sao lưu trạng thái của editor tại thời điểm đó. Sau đó, nếu người dùng cần hoàn tác một hành động, ứng dụng có thể lấy command gần nhất từ lịch sử, đọc bản sao liên kết với trạng thái của editor và phục hồi nó.

Code client (phần tử GUI, lịch sử command) không phải ghép với lớp command cụ thể bởi vì nó hoạt động với command thông qua interface command. Cách tiếp cận này giúp bạn thêm command mới vào ứng dụng mà không ảnh hưởng đến code hiện có.

```c
// Lớp command cơ sở xác định interface chung cho tất cả
// concrete command.
abstract class Command is
    protected field app: Application
    protected field editor: Editor
    protected field backup: text

    constructor Command(app: Application, editor: Editor) is
        this.app = app
        this.editor = editor

    // Tạo một bản sao lưu trạng thái editor.
    method saveBackup() is
        backup = editor.text

    // Phục hồi trạng thái editor.
    method undo() is
        editor.text = backup

    // Phương thức thực thi khai báo trừu tượng cho tất cả
    // concrete command cung cấp các triển khai của riêng nó.
    // Phương thức trả về true hoặc false tuỳ thuộc vào command
    // có thay đổi trạng thái editor hay không.
    abstract method execute()


// Concrete command ở đây.
class CopyCommand extends Command is
    // Bản sao command không được lưu vào lịch sử vì nó
    // không thay đổi trạng thái editor.
    method execute() is
        app.clipboard = editor.getSelection()
        return false

class CutCommand extends Command is
    // Command cut thay đổi trạng thái editor, do đó nó phải
    // được lưu vào lịch sử. Và nó sẽ được lưu miễn là 
    // phương thức trả về true.
    method execute() is
        saveBackup()
        app.clipboard = editor.getSelection()
        editor.deleteSelection()
        return true

class PasteCommand extends Command is
    method execute() is
        saveBackup()
        editor.replaceSelection(app.clipboard)
        return true

// Thao tác undo cũng là command.
class UndoCommand extends Command is
    method execute() is
        app.undo()
        return false


// Lịch sử command chỉ là một ngăn xếp.
class CommandHistory is
    private field history: array of Command

    // Last in...
    method push(c: Command) is
        // Thêm command vào cuối của mảng lịch sử.

    // ...first out
    method pop():Command is
        // Lấy command gần nhất khỏi lịch sử.


// Lớp editor thực hiện các thao tác thực. Nó hoạt động như
// một receiver: tất cả command uỷ thác thực thi cho phương
// thức của editor.
class Editor is
    field text: string

    method getSelection() is
        // Trả về văn bản được chon.

    method deleteSelection() is
        // Xoá văn bản được chon.

    method replaceSelection(text) is
        // Chèn nội dung của clipboard vào vị trí hiện tại.

// Lóp ứng dụng thiết lập quan hệ đối tượng. Nó hành động như 
// một sender: khi điều gì đó cần hoàn thành, nó tạo đối tượng
// command và thực thi nó.
class Application is
    field clipboard: string
    field editors: array of Editors
    field activeEditor: Editor
    field history: CommandHistory

    // Đoạn code gán command cho các đối tượng UI 
    // có thể trông như thế này.
    method createUI() is
        // ...
        copy = function() { executeCommand(
            new CopyCommand(this, activeEditor)) }
        copyButton.setCommand(copy)
        shortcuts.onKeyPress("Ctrl+C", copy)

        cut = function() { executeCommand(
            new CutCommand(this, activeEditor)) }
        cutButton.setCommand(cut)
        shortcuts.onKeyPress("Ctrl+X", cut)

        paste = function() { executeCommand(
            new PasteCommand(this, activeEditor)) }
        pasteButton.setCommand(paste)
        shortcuts.onKeyPress("Ctrl+V", paste)

        undo = function() { executeCommand(
            new UndoCommand(this, activeEditor)) }
        undoButton.setCommand(undo)
        shortcuts.onKeyPress("Ctrl+Z", undo)

    // Thực thi command và kiểm tra xem nó có phải thêm vào lịch sử
    // hay không.
    method executeCommand(command) is
        if (command.execute)
            history.push(command)

    // Lấy command gần nhất khởi lịch sử và chạy phương thức undo.
    // Lưu ý ta không biết lớp của command này. Nhưng ta không cần
    // phải biết, vì command biết cách phải thực hiện hành động undo.
    method undo() is
        command = history.pop()
        if (command != null)
            command.undo()
```

