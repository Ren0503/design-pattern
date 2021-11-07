# EN: Factory Method Design Pattern
#
# Intent: Provides an interface for creating objects in a superclass, but allows
# subclasses to alter the type of objects that will be created.

# EN: The Creator class declares the factory method that is supposed to return
# an object of a Product class. The Creator's subclasses usually provide the
# implementation of this method.
#
# @abstract
class Creator
    # EN: Note that the Creator may also provide some default implementation
    # of the factory method.
    #
    # @abstract
    def factory_method
      raise NotImplementedError, "#{self.class} has not implemented method '#{__method__}'"
    end
  
    # EN: Also note that, despite its name, the Creator's primary
    # responsibility is not creating products. Usually, it contains some core
    # business logic that relies on Product objects, returned by the factory
    # method. Subclasses can indirectly change that business logic by
    # overriding the factory method and returning a different type of product
    # from it.
    #
    # @return [String]
    def some_operation
      # EN: Call the factory method to create a Product object.

      product = factory_method
  
      # EN: Now, use the product.
      result = "Creator: The same creator's code has just worked with #{product.operation}"
  
      result
    end
  end
  
  # EN: Concrete Creators override the factory method in order to change the
  # resulting product's type.
  class ConcreteCreator1 < Creator
    # EN: Note that the signature of the method still uses the abstract product
    # type, even though the concrete product is actually returned from the method.
    # This way the Creator can stay independent of concrete product classes.
    #
    # @return [ConcreteProduct1]
    def factory_method
      ConcreteProduct1.new
    end
  end
  
  class ConcreteCreator2 < Creator
    # @return [ConcreteProduct2]
    def factory_method
      ConcreteProduct2.new
    end
  end
  
  # EN: The Product interface declares the operations that all concrete products
  # must implement.
  #
  # @abstract
  class Product
    # return [String]
    def operation
      raise NotImplementedError, "#{self.class} has not implemented method '#{__method__}'"
    end
  end
  
  # EN: Concrete Products provide various implementations of the Product interface.
  class ConcreteProduct1 < Product
    # @return [String]
    def operation
      '{Result of the ConcreteProduct1}'
    end
  end
  
  class ConcreteProduct2 < Product
    # @return [String]
    def operation
      '{Result of the ConcreteProduct2}'
    end
  end
  
  # EN: The client code works with an instance of a concrete creator, albeit
  # through its base interface. As long as the client keeps working with the
  # creator via the base interface, you can pass it any creator's subclass.
  #
  # @param [Creator] creator
  def client_code(creator)
    print "Client: I'm not aware of the creator's class, but it still works.\n"\
          "#{creator.some_operation}"
  end
  
  puts 'App: Launched with the ConcreteCreator1.'
  client_code(ConcreteCreator1.new)
  puts "\n\n"
  
  puts 'App: Launched with the ConcreteCreator2.'
  client_code(ConcreteCreator2.new)