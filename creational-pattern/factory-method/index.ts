/**
 * EN: Factory Method Design Pattern
 *
 * Intent: Provides an interface for creating objects in a superclass, but
 * allows subclasses to alter the type of objects that will be created.
 */

/**
 * EN: The Creator class declares the factory method that is supposed to return
 * an object of a Product class. The Creator's subclasses usually provide the
 * implementation of this method.
 */
 abstract class Creator {
    /**
     * EN: Note that the Creator may also provide some default implementation of
     * the factory method.
     */
    public abstract factoryMethod(): Product;

    /**
     * EN: Also note that, despite its name, the Creator's primary
     * responsibility is not creating products. Usually, it contains some core
     * business logic that relies on Product objects, returned by the factory
     * method. Subclasses can indirectly change that business logic by
     * overriding the factory method and returning a different type of product
     * from it.
     */
    public someOperation(): string {
        // EN: Call the factory method to create a Product object.
        const product = this.factoryMethod();
        // EN: Now, use the product.
        return `Creator: The same creator's code has just worked with ${product.operation()}`;
    }
}

/**
 * EN: Concrete Creators override the factory method in order to change the
 * resulting product's type.
 */
class ConcreteCreator1 extends Creator {
    /**
     * EN: Note that the signature of the method still uses the abstract product
     * type, even though the concrete product is actually returned from the
     * method. This way the Creator can stay independent of concrete product
     * classes.
     */
    public factoryMethod(): Product {
        return new ConcreteProduct1();
    }
}

class ConcreteCreator2 extends Creator {
    public factoryMethod(): Product {
        return new ConcreteProduct2();
    }
}

/**
 * EN: The Product interface declares the operations that all concrete products
 * must implement.
 */
interface Product {
    operation(): string;
}

/**
 * EN: Concrete Products provide various implementations of the Product
 * interface.
 */
class ConcreteProduct1 implements Product {
    public operation(): string {
        return '{Result of the ConcreteProduct1}';
    }
}

class ConcreteProduct2 implements Product {
    public operation(): string {
        return '{Result of the ConcreteProduct2}';
    }
}

/**
 * EN: The client code works with an instance of a concrete creator, albeit
 * through its base interface. As long as the client keeps working with the
 * creator via the base interface, you can pass it any creator's subclass.
 */
function clientCode(creator: Creator) {
    // ...
    console.log('Client: I\'m not aware of the creator\'s class, but it still works.');
    console.log(creator.someOperation());
    // ...
}

/**
 * EN: The Application picks a creator's type depending on the configuration or
 * environment.
 */
console.log('App: Launched with the ConcreteCreator1.');
clientCode(new ConcreteCreator1());
console.log('');

console.log('App: Launched with the ConcreteCreator2.');
clientCode(new ConcreteCreator2());