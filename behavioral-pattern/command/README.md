# Command

## 📜 Mục đích

**Command** là một design pattern thuộc nhóm behavioral, nó biến một yêu cầu thành một đối tượng độc lập bao gồm tất cả thông tin của yêu cầu. Chuyển đổi này giúp bạn truyền các yêu cầu dưới dạng đối số của phương thức, trì hoãn hoặc xếp hàng đợi việc thực thi một yêu cầu và hỗ trợ các hoạt động hoàn tác. 

![intent](./assets/intent.png)

## 😟 Vấn đề

Tưởng tượng bạn đang làm việc với một ứng dụng soạn thảo văn bản. Công việc hiện tại của bạn là tạo một thanh công cụ với nhóm button cho các thao tác khác nhau của editor. Bạn đã tạo một lớp `Button` gọn gàng để có thể dùng cho các button của thanh công cụ, cũng như cho các button chung ở các cửa sổ khác.

![problem1](./assets/problem1.png)

Trong khi tất cả buttons này trông giống nhau, thì chúng lại hỗ trợ những công việc khác nhau. Bạn sẽ đặt code cho các xử lý click khác nhau của chúng ở đâu ? Giải pháp đơn giản nhất là tạo hàng nghìn lớp con cho từng nơi mà button được sử dụng. Các lớp con này sẽ bao gồm code cho thực thi thao tác click.

![problem2](./assets/problem2.png)

Rất nhanh chóng, bạn nhận ra cách tiếp cận này có rất nhiều thiếu sót. Đầu tiên, bạn sẽ có một số lượng rất lớn lớp con, và nó sẽ không ổn khi bạn sử đổi lớp `Button` cơ sở vì bạn sẽ thay đổi tất cả lớp con của nó. Nói một cách đơn giản, code GUI của bạn đã trở nên phụ thuộc một cách khó hiểu vào code dễ bay hơi của logic nghiệp vụ. 

![problem3](./assets/problem3.png)

Và phần tồi tệ ở đây. Một vài thao tác như copy/paste văn bản, sẽ cần được gọi từ nhiều nơi. Ví dụ, người dùng click vào button "Copy" trên thanh công cụ, hoặc sao chép gì đó thông quan menu hay chỉ Ctrl+C trên bàn phím.

Ban đầu, khi ứng dụng của chỉ có thanh công cụ, có thể đặt việc triển khai các hoạt động khác nhau vào các lớp con của button. Nói cách khác, có code để sao chép văn bản bên trong lớp con `CopyButton` là tốt. Nhưng sau đó, khi bạn triển khai menu, lối tắt và những thứ khác, bạn phải sao chép code của thao tác trong nhiều lớp hoặc làm cho menu phụ thuộc vào các button, đó là một lựa chọn thậm chí còn tệ hơn.

## 😊 Giải pháp

Thiết kế phần mềm tốt thường dựa trên *nguyên tắc tách biệt các mối quan tâm*, điều này thường dẫn đến việc chia ứng dụng thành nhiều lớp. Ví dụ phổ biến nhất: một lớp cho giao diện người dùng đồ họa và một lớp khác cho logic nghiệp vụ. Lớp GUI chịu trách nhiệm hiển thị hình ảnh đẹp trên màn hình, thu nhận bất kỳ đầu vào nào và hiển thị kết quả về những gì người dùng và ứng dụng đang làm. Tuy nhiên, khi cần làm điều gì đó quan trọng, như tính toán quỹ đạo của mặt trăng hoặc soạn báo cáo hàng năm, lớp GUI sẽ ủy quyền công việc cho lớp logic nghiệp vụ cơ bản.

Trong đoạn code, nó có thể trông như thế này: một đối tượng GUI gọi một phương thức của đối tượng logic nghiệp vụ, truyền cho nó một số đối số. Quá trình này thường được mô tả là một đối tượng gửi một yêu cầu khác.

![solution1](./assets/solution1.png)

Command gợi ý rằng các đối tượng GUI không nên gửi trực tiếp các yêu cầu này. Thay vào đó, bạn nên trích xuất tất cả các chi tiết yêu cầu, chẳng hạn như đối tượng được gọi, tên của phương thức và danh sách các đối số vào một lớp lệnh riêng biệt với một phương thức kích hoạt yêu cầu này.

Các đối tượng command đóng vai trò là liên kết giữa các đối tượng GUI và logic nghiệp vụ khác nhau. Từ bây giờ, đối tượng GUI không cần biết đối tượng logic nghiệp vụ nào sẽ nhận được yêu cầu và cách xử lý yêu cầu. Đối tượng GUI chỉ kích hoạt command, nó sẽ xử lý tất cả các chi tiết.

![solution2](./assets/solution2.png)

Bước tiếp theo là làm cho các command của bạn triển khai cùng một interface. Thông thường nó chỉ có một phương thức thực thi duy nhất mà không cần tham số. Interface này cho phép bạn sử dụng các command khác nhau với cùng một người gửi yêu cầu mà không cần kết hợp nó với các lớp command cụ thể. Như một phần thưởng, giờ đây bạn có thể chuyển đổi các đối tượng command được liên kết với người gửi, thay đổi hiệu quả hành vi của người gửi trong thời gian chạy.

Bạn có thể nhận thấy một phần còn thiếu của câu đố, đó là các thông số yêu cầu. Một đối tượng GUI có thể đã cung cấp cho đối tượng lớp nghiệp vụ một số tham số. Vì phương thức thực thi lệnh không có bất kỳ tham số nào, chúng ta sẽ chuyển các chi tiết yêu cầu đến người nhận như thế nào? Hóa ra command phải được cấu hình trước với dữ liệu này hoặc có khả năng tự lấy nó.

![solution3](./assets/solution3.png)

Hãy quay lại trình soạn thảo văn bản. Sau khi áp dụng Command, ta không còn cần đến tất cả các lớp con của button đó để thực hiện các hành vi click chuột khác nhau. Chỉ cần đặt một trường vào lớp `Button` cơ sở là đủ để lưu trữ tham chiếu đến đối tượng command và làm cho button thực hiện command đó khi click chuột.

Bạn sẽ triển khai một loạt các lớp command cho mọi hoạt động có thể và liên kết chúng với các button cụ thể, tùy thuộc vào hành vi dự kiến của các button.

Các phần tử GUI khác, chẳng hạn như menu, lối tắt hoặc toàn bộ hộp thoại, có thể được thực hiện theo cách tương tự. Chúng sẽ được liên kết với một command được thực thi khi người dùng tương tác với phần tử GUI. Như bạn có thể đoán bây giờ, các phần tử liên quan đến các hoạt động giống nhau sẽ được liên kết với các command giống nhau, ngăn chặn bất kỳ sự trùng lặp code nào.

Kết quả là, các command trở thành một lớp trung gian thuận tiện giúp giảm sự ghép nối giữa GUI và các lớp logic nghiệp vụ. Và đó chỉ là một phần nhỏ trong số những lợi ích mà Command có thể mang lại!

## 🚗 Thế Giới Thực

![analogy](./assets/analogy.png)

Sau khi đi bộ qua thành phố, bạn đến một nhà hàng đẹp và ngồi vào bàn bên cửa sổ. Một người phục vụ thân thiện tiếp cận bạn và nhanh chóng nhận đơn đặt hàng của bạn, viết nó ra một tờ giấy. Người phục vụ đi vào bếp và dán thứ tự lên tường. Sau một thời gian, đơn đặt hàng được chuyển đến đầu bếp, người sẽ đọc và nấu bữa ăn cho phù hợp. Người đầu bếp đặt bữa ăn vào khay cùng với thứ tự. Người phục vụ lấy khay, kiểm tra thứ tự để đảm bảo mọi thứ đều như bạn muốn và mang mọi thứ đến bàn của bạn.

Lệnh trên giấy dùng như một mệnh lệnh. Nó vẫn còn trong hàng đợi cho đến khi đầu bếp sẵn sàng phục vụ nó. Đơn đặt hàng chứa tất cả các thông tin liên quan cần thiết để nấu bữa ăn. Nó cho phép đầu bếp bắt đầu nấu ăn ngay lập tức thay vì chạy xung quanh để làm rõ chi tiết đơn đặt hàng trực tiếp từ bạn.

## 🏢 Cấu trúc

![structure](./assets/structure.png)

1. **Sender** (hay còn gọi là invoker) là lớp chịu trách nhiệm khởi tạo các yêu cầu. Lớp này phải có một trường để lưu trữ một tham chiếu đến một đối tượng command. Người gửi kích hoạt command đó thay vì gửi yêu cầu trực tiếp đến người nhận. Lưu ý rằng người gửi không chịu trách nhiệm tạo đối tượng command. Thông thường, nó nhận một command được tạo trước từ client thông qua phương thức khởi tạo.
2. **Command** là interface khai báo một phương thức đơn nhất để thực hiện lệnh.
3. **Concrete Command** thực hiện nhiều loại yêu cầu khác nhau. Một command cụ thể không được phép tự thực hiện công việc, mà là để chuyển lệnh gọi đến một trong các đối tượng logic nghiệp vụ. Tuy nhiên, để đơn giản hóa mã, các lớp này có thể được hợp nhất.
Các tham số cần thiết để thực thi một phương thức trên một đối tượng nhận có thể được khai báo dưới dạng các trường trong command cụ thể. Bạn có thể làm cho các đối tượng command trở nên bất biến bằng cách chỉ cho phép khởi tạo các trường này thông qua phương thức khởi tạo.
4. **Receiver** là lớp chứa một số logic nghiệp vụ. Hầu như bất kỳ đối tượng nào cũng có thể hoạt động như một người nhận. Hầu hết các command chỉ xử lý các chi tiết về cách một yêu cầu được chuyển đến người nhận, trong khi người nhận tự thực hiện công việc thực tế.
5. **Client** tạo và cấu hình các đối tượng command cụ thể. Client phải chuyển tất cả các tham số yêu cầu, bao gồm cả người gửi, vào phương thức khởi tạo của command. Sau đó, command kết quả có thể được liên kết với một hoặc nhiều người gửi.
