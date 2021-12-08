# Template Method

## 📜 Mục đích

**Template Method** là một design pattern thuộc nhóm behavioral giúp định nghĩa bộ khung của thuật toán ở lớp cha (superclass) nhưng các lớp con (subsclasses) có thể ghi đè lên các bước cụ thể của thuật toán mà không làm thay đổi cấu trúc của nó.

![intent](./assets/intent.png)

## 😟 Vấn đề

Tưởng tượng bạn đang tạo một ứng dụng khai thác dữ liệu để phân tích tài liệu của công ty. Người dùng cung cấp các tài liệu cho ứng dụng với các định dạng khác nhau (PDF, DOC, CSV), ứng dụng sẽ trích xuất dữ liệu có ích từ các tài liệu này ở một định dạng thống nhất.

Phiên bản đầu tiên của ứng dụng chỉ làm việc với file DOC. Trong phiên bản tiếp theo nó hỗ trợ file CSV. Và một tháng sau, nó trích xuất cả dữ liệu từ file PDF.

![problem](./assets/problem.png)

Vào một thời điểm nào đó, bạn nhận thấy rằng cả code ở cả ba lớp có rất nhiều điểm tương đồng nhau. Mặc dù code để xử lý các định dạng dữ liệu khác nhau hoàn toàn khác nhau ở tất cả các lớp, nhưng code để xử lý và phân tích dữ liệu gần như giống hệt nhau. Sẽ rất tuyệt vời nếu ta có thể loại bỏ sự trùng lặp code nhưng vẫn giữ nguyên được cấu trúc của thuật toán.

Và một vấn đề khác nữa liên quan đến code client, nơi sử dụng các lớp này, là nó có rất nhiều điều kiện để chọn quá trình hành động thích hợp tùy thuộc vào lớp của đối tượng xử lý. Nếu cả ba lớp xử lý đều có một interface chung hoặc một lớp cơ sở, bạn có thể loại bỏ các điều kiện trong code client và sử dụng tính đa hình khi gọi các phương thức trên một đối tượng xử lý.

## 😊 Giải pháp

Template Method gợi ý rằng bạn nên chia nhỏ thuật toán thành một chuỗi các bước, biến các bước này thành các phương thức và đặt một loạt lệnh gọi đến các phương thức này bên trong một phương thức template duy nhất. Các bước có thể là `abstract` (trừu tượng) hoặc có một số triển khai mặc định. Để sử dụng thuật toán, client phải cung cấp lớp con của chính nó, thực hiện tất cả các bước trừu tượng và ghi đè một số bước tùy chọn nếu cần (nhưng không được ghi lên phương thức template).

Hãy xem cách nó làm việc trong ứng dụng khai thác dữ liệu. Ta có thể tạo một lớp cơ sở cho cả ba thuật toán phân tích. Lớp này định nghĩa một phương thức template bao gồm một loạt các lệnh gọi đến các bước xử lý tài liệu khác nhau.

![solution](./assets/solution.png)

Lúc đầu, ta có thể khai báo tất cả các bước là `abstract`, buộc các lớp con cung cấp các triển khai riêng của chúng cho các phương thức này. Trong trường hợp này, các lớp con đã có tất cả các triển khai cần thiết, vì vậy điều duy nhất ta cần làm là điều chỉnh signature của các phương thức để phù hợp với các phương thức của lớp cha.

Bây giờ, hãy xem cách để có thể loại bỏ code trùng lặp. Có thể thấy code để mở/đóng file và trích xuất/phân tích dữ liệu là khác nhau đối với các định dạng dữ liệu khác nhau, vì vậy bạn không cần phải đụng đến các phương pháp đó. Tuy nhiên, việc thực hiện các bước khác, chẳng hạn như phân tích dữ liệu raw và soạn báo cáo, rất giống nhau, vì vậy nó có thể được kéo lên lớp cơ sở, nơi các lớp con có thể chia sẻ code đó.

Như bạn có thể thấy, ta có hai loại bước:

- các bước trừu tượng phải được thực hiện bởi mọi lớp con.
- các bước tùy chọn đã có một số triển khai mặc định, nhưng vẫn có thể bị ghi đè nếu cần.

Có một loại bước khác, được gọi là hook. Hook là một bước tùy chọn với phần thân trống. Phương thức template sẽ hoạt động ngay cả khi hook không bị ghi đè. Thông thường, các hook được đặt trước và sau các bước quan trọng của thuật toán, cung cấp các lớp con với các điểm mở rộng bổ sung cho một thuật toán.

## 🚗 Thế Giới Thực

![analogy](./assets/analogy.png)

Phương pháp template có thể được sử dụng trong xây dựng hàng loạt ngôi nhà. Kế hoạch kiến trúc để xây dựng một ngôi nhà tiêu chuẩn có thể chứa một số điểm mở rộng cho phép người chủ sở hữu có tiềm năng điều chỉnh một số chi tiết của ngôi nhà.

Mỗi công đoạn xây dựng như đổ móng, đóng khung, xây tường, lắp đặt hệ thống ống nước, đi dây điện nước,… đều có thể thay đổi đôi chút để tạo cho ngôi nhà có một chút khác biệt so với những ngôi nhà khác.

## 🏢 Cấu trúc

![structure](./assets/structure.png)

1. **Abstract Class** là lớp trừu tượng khai báo các phương thức hoạt động như các bước của một thuật toán, cũng như phương thức template để gọi các phương thức này theo một thứ tự cụ thể. Các bước có thể được khai báo là trừu tượng hoặc có một số triển khai mặc định.
2. **Concrete Classes** có thể ghi đè tất cả các bước, nhưng không thể ghi đè lên phương thức template.

## 👨‍💻 Mã giả

Trong ví dụ này, phương thức Template cung cấp một "bộ khung" cho các branch khác nhau của trí thông minh nhân tạo trên một trò chơi điện tử mô phỏng đơn giản.

![pseudocode](./assets/pseudocode.png)

Tất cả chủng tộc trong trò chơi gần như giống nhau về kiểu unit và cách xây dựng. Do đó bạn có thể sử dụng lại cùng một cấu trúc AI cho các chủng tộc khác nhau, đồng thời vẫn có thể ghi đè lên một vài chi tiết. Với cách tiếp cận này, bạn có thể ghi đè lên AI của loài orc làm cho chúng hung dữ, làm cho loài người có khả năng phòng thủ và lũ quái vật không thể xây dựng bất kỳ thứ gì. Thêm một chủng tộc mới trong game yêu cầu tạo một lớp con AI mới và ghi đè lên phương thức mặc định đã tạo ở lớp AI cơ sở.

```c
// Lớp abstract định nghĩa một phương thức template bao gồm
// bộ khung của một vài thuật toán được gọi, thông thường là
// các thao tác nguyên thuỷ trừu tượng. Concrete subclass triển
// khai các thao tác này, nhưng vẫn giữ nguyên phương thức
// template.
class GameAI is
    // Phương thức template định nghĩa khung của một thuật toán.
    method turn() is
        collectResources()
        buildStructures()
        buildUnits()
        attack()


    // Một vài bước có thể triển khai ở tại lớp cơ sở.
    method collectResources() is
        foreach (s in this.builtStructures) do
            s.collect()

    // Và một số có thể định nghĩa là trừu tượng.
    abstract method buildStructures()
    abstract method buildUnits()

    // Một lớp có thể có nhiều phương thức template.
    method attack() is
        enemy = closestEnemy()
        if (enemy == null)
            sendScouts(map.center)
        else
            sendWarriors(enemy.position)

    abstract method sendScouts(position)
    abstract method sendWarriors(position)


// Concrete class phải triển khai tất cả thao tác trừu tượng 
// của lớp cơ sở và không được ghi đè lên phương thức template.
class OrcsAI extends GameAI is
    method buildStructures() is
        if (there are some resources) then
            // Xây dựng trang trại, sau đó là doanh trại, sau đó là thành trì.
            
    method buildUnits() is
        if (there are plenty of resources) then
            if (there are no scouts)
                // Xây dựng người liên lạc, thêm nó vào nhóm trinh sát.
            else
                // Xây dựng grunt, thêm nó vào nhóm chiến binh.
                
    // ...

    method sendScouts(position) is
        if (scouts.length > 0) then
            // Cử trinh sát đến vị trí.

    method sendWarriors(position) is
        if (warriors.length > 5) then
            // Đưa chiến binh vào vị trí.


// Lớp con có thể ghi đè một vài thao tác với
// triển khai mặc định.
class MonstersAI extends GameAI is
    method collectResources() is
        // Quái vật không thể thu thập tài nguyên.

    method buildStructures() is
        // Quái vật không thể xây dựng kiến trúc..

    method buildUnits() is
        // Quái vật không thể xây dựng đơn vị.
```

## 💡 Ứng dụng

**🐞 Sử dụng phương thức Template khi bạn muốn client chỉ mở rộng các bước cụ thể của thuật toán chứ không phải toàn bộ cấu trúc của nó**

⚡ Phương thức Template giúp bạn chuyển một khối thuật toán thành một loạt các bước riêng rẽ để dễ mở rộng bởi lớp con trong khi vẫn giữ nguyên cấu trúc đã định nghĩa ở lớp cha.

**🐞 Sử dụng template khi bạn có nhiều lớp bao gồm các thuật toán giống nhau chỉ có một ít là khác biệt. Và bạn phải chỉnh sửa tất cả lớp khi thuật toán thay đổi**.

⚡ Khi bạn chuyển một thuật toán thành phương thức template, bạn có thể kéo các bước với triển khai giống nhau lên lớp cha, giảm thiểu code trùng lặp. Code khác nhau ở lớp con có thể được giữ lại ở đấy.

## 📋 Triển khai

1. Phân tích thuật toán mục tiêu để xem liệu bạn có thể chia nó thành các bước hay không. Xem xét bước nào là chung cho tất cả các lớp con và bước nào là duy nhất.
2. Tạo lớp trừu tường (`abstract`) và khai báo phương thức template và một tập hợp của phương thức trừu tượng để biểu diễn các bước của thuật toán. Phác thảo cấu trúc của thuật toán trong phương pháp template bằng cách thực hiện các bước tương ứng. Cân nhắc việc tạo phương thức template cuối cùng để ngăn các lớp con ghi đè nó.
3. Sẽ không sao nếu tất cả các bước đều trừu tượng. Tuy nhiên, một số bước có thể được hưởng lợi từ việc triển khai mặc định. Các lớp con không phải triển khai các phương thức đó.
4. Thêm hook giữa các bước cốt lõi của thuật toán.
5. Đối với mỗi biến thể của thuật toán, hãy tạo một lớp con cụ thể(concrete subclasses) mới. Nó phải triển khai tất cả các bước trừu tượng, nhưng cũng có thể ghi đè một số bước tùy chọn.

## ⚖️ Ưu nhược điểm

### Ưu điểm

✔️ Bạn chỉ cho phép client ghi đè một số phần nhất định của một thuật toán lớn, giúp chúng ít bị ảnh hưởng bởi những thay đổi xảy ra với các phần khác của thuật toán.

✔️ Bạn có thể gom code trùng lặp vào một lớp cha.

### Nhược điểm

❌ Một số client có thể bị giới hạn bởi khung thuật toán được cung cấp.

❌ Bạn có thể vi phạm Nguyên tắc Liskov Substitution, khi chặn triển khai bước mặc định thông qua một lớp con.

❌ Các phương pháp template có xu hướng khó bảo trì hơn khi chúng có nhiều bước hơn.

## 🔁 Quan hệ với các pattern khác

**Factory Method** là một chuyên môn hóa của **Template Method**. Đồng thời, **Factory Method** có thể đóng vai trò là một bước trong một **Template Method** lớn.

**Template Method** dựa trên sự kế thừa: nó cho phép bạn thay đổi các phần của một thuật toán bằng cách mở rộng các phần đó trong các lớp con. **Strategy** dựa trên cấu tạo: bạn có thể thay đổi các phần trong hành vi của đối tượng bằng cách cung cấp cho đối tượng các strategy khác nhau tương ứng với hành vi đó. **Template Method** hoạt động ở cấp độ lớp, vì vậy nó là tĩnh. **Strategy** hoạt động ở cấp độ đối tượng, cho phép bạn chuyển đổi hành vi trong thời gian chạy.

# Nguồn

[**refactoring**](https://refactoring.guru/design-patterns/template-method)