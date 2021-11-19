# Structural Design Patterns

Structural Pattern giải thích cách tập hợp các đối tượng và lớp thành các cấu trúc lớn hơn, trong khi vẫn giữ cho cấu trúc linh hoạt và hiệu quả.

## Adapter

![adapter-mini](./assets/adapter-mini.png)

Cho phép các đối tượng có interface không tương thích cộng tác với nhau.

## Bridge

![bridge-mini](./assets/bridge-mini.png)

Giúp bạn tách một lớp khổng lồ hoặc một tập hợp lớp có quan hệ gần gũi với nhau thành hai hệ thống phân cấp lớp riêng biệt là - abstraction(trừu tượng) và implementation(triển khai) - có thể phát triển độc lập với nhau.

## Composite

![composite-mini](./assets/composite-mini.png)

Giúp bạn sắp xếp các đối tượng thành cấu trúc cây và sau đó làm việc với các cấu trúc này như thể chúng là các đối tượng riêng lẻ.

## Decorator

![decorator-mini](./assets/decorator-mini.png)

Giúp bạn thêm một hành vi mới vào đối tượng bằng cách đặt đối tượng đó vào trong một đối tượng đặc biệt có chứa hành vi đấy

## Facade

![facade-mini](./assets/facade-mini.png)

Cung cấp interface đơn giản cho thư viện, framework hoặc bất kỳ tập hợp lớp phức tạp nào khác.

## Flyweight

![flyweight-mini](./assets/flyweight-mini.png)

Giúp bạn chỉnh các đối tượng vừa với lượng RAM khả dụng bằng các chia sẻ trạng thái chung giữa các đối tượng thay vì giữ tất cả dữ liệu ở mỗi đối tượng.

## Proxy

![proxy-mini](./assets/proxy-mini.png)

Cho phép bạn cung cấp một vật thay thế hoặc vật giữ chỗ cho một đối tượng khác. Một proxy kiểm soát quyền truy cập đến đối tượng ban đầu, cho phép bạn thực hiện điều gì đó trước hoặc sau khi yêu cầu được chuyển đến đối tượng ban đầu.