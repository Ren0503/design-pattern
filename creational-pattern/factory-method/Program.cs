// EN: Factory Method Design Pattern
//
// Intent: Provides an interface for creating objects in a superclass, but
// allows subclasses to alter the type of objects that will be created.

using System;

namespace RefactoringGuru.DesignPatterns.FactoryMethod.Conceptual
{
    // EN: The Creator class declares the factory method that is supposed to
    // return an object of a Product class. The Creator's subclasses usually
    // provide the implementation of this method.
    {
        // EN: Note that the Creator may also provide some default
        // implementation of the factory method.
        public abstract IProduct FactoryMethod();

        // EN: Also note that, despite its name, the Creator's primary
        // responsibility is not creating products. Usually, it contains some
        // core business logic that relies on Product objects, returned by the
        // factory method. Subclasses can indirectly change that business logic
        // by overriding the factory method and returning a different type of
        // product from it.
        public string SomeOperation()
        {
            // EN: Call the factory method to create a Product object.
            var product = FactoryMethod();
            // EN: Now, use the product.
            var result = "Creator: The same creator's code has just worked with "
                + product.Operation();

            return result;
        }
    }

    // EN: Concrete Creators override the factory method in order to change the
    // resulting product's type.
    class ConcreteCreator1 : Creator
    {
        // EN: Note that the signature of the method still uses the abstract
        // product type, even though the concrete product is actually returned
        // from the method. This way the Creator can stay independent of
        // concrete product classes.
        public override IProduct FactoryMethod()
        {
            return new ConcreteProduct1();
        }
    }

    class ConcreteCreator2 : Creator
    {
        public override IProduct FactoryMethod()
        {
            return new ConcreteProduct2();
        }
    }

    // EN: The Product interface declares the operations that all concrete
    // products must implement.
    public interface IProduct
    {
        string Operation();
    }

    // EN: Concrete Products provide various implementations of the Product
    // interface.
    class ConcreteProduct1 : IProduct
    {
        public string Operation()
        {
            return "{Result of ConcreteProduct1}";
        }
    }

    class ConcreteProduct2 : IProduct
    {
        public string Operation()
        {
            return "{Result of ConcreteProduct2}";
        }
    }

    class Client
    {
        public void Main()
        {
            Console.WriteLine("App: Launched with the ConcreteCreator1.");
            ClientCode(new ConcreteCreator1());
            
            Console.WriteLine("");

            Console.WriteLine("App: Launched with the ConcreteCreator2.");
            ClientCode(new ConcreteCreator2());
        }

        // EN: The client code works with an instance of a concrete creator,
        // albeit through its base interface. As long as the client keeps
        // working with the creator via the base interface, you can pass it any
        // creator's subclass.
        public void ClientCode(Creator creator)
        {
            // ...
            Console.WriteLine("Client: I'm not aware of the creator's class," +
                "but it still works.\n" + creator.SomeOperation());
            // ...
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            new Client().Main();
        }
    }
}