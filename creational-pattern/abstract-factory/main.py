from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    """
    Abstract Factory, interface khai báo một tập hợp phương thức trả về các sản
    phẩm trừu tượng khác nhau. Các sản phẩm này được gọi là một nhóm và có quan
    hệ cấp cao về chủ đề hay khái niệm. Sản phẩm của một nhóm thường có thể cộng
    tác lại với nhau. Một nhóm sản phẩm thường có nhiều biến thể, nhưng các sản 
    phẩm của một biến thể không tương thích với sản phẩm của những biến thể khác.
    """
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class ConcreteFactory1(AbstractFactory):
    """
    Concrete Factories tạo một nhóm sản phẩm thuộc về một biến thể. Factory
    đảm bảo kết quả sản phẩm luôn tương thích. Lưu ý, chữ ký số của phương
    thức Concrete Factory trả về một sản phẩm trừu tượng, trong khi bên trong
    phương thức một sản phẩm cụ thể được tạo.
    """

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    """
    Mỗi Concrete Factory có một biến thể sản phẩm phù hợp.
    """

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()


class AbstractProductA(ABC):
    """
    Mỗi sản phẩm riêng biệt của nhóm sản phẩm có một interface cơ sở. Tất cả
    biến thể của sản phẩm phải triển khai interface này.
    """

    @abstractmethod
    def useful_function_a(self) -> str:
        pass


"""
Concrete Products được tạo bởi Concrete Factories phù hợp.
"""


class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product A1."


class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product A2."


class AbstractProductB(ABC):
    """
    Here's the the base interface of another product. All products can interact
    with each other, but proper interaction is possible only between products of
    the same concrete variant.
    Đây là interface cơ sở của các sản phẩm khác. Tất cả sản phẩm có thể tương
    tác với mỗi 
    """
    @abstractmethod
    def useful_function_b(self) -> None:
        """
        Product B is able to do its own thing...
        """
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        """
        ...but it also can collaborate with the ProductA.

        The Abstract Factory makes sure that all products it creates are of the
        same variant and thus, compatible.
        """
        pass


"""
Concrete Products are created by corresponding Concrete Factories.
"""


class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B1."

    """
    The variant, Product B1, is only able to work correctly with the variant,
    Product A1. Nevertheless, it accepts any instance of AbstractProductA as an
    argument.
    """

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f"The result of the B1 collaborating with the ({result})"


class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B2."

    def another_useful_function_b(self, collaborator: AbstractProductA):
        """
        The variant, Product B2, is only able to work correctly with the
        variant, Product A2. Nevertheless, it accepts any instance of
        AbstractProductA as an argument.
        """
        result = collaborator.useful_function_a()
        return f"The result of the B2 collaborating with the ({result})"


def client_code(factory: AbstractFactory) -> None:
    """
    The client code works with factories and products only through abstract
    types: AbstractFactory and AbstractProduct. This lets you pass any factory
    or product subclass to the client code without breaking it.
    """
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")


if __name__ == "__main__":
    """
    The client code can work with any concrete factory class.
    """
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory1())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreteFactory2())