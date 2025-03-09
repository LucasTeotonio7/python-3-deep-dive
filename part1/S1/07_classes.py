# Custom Classes



def run_all_code_or_last_code():
    while True:
        resp = input('You wish run all code ? (y/n): ')
        value = resp.lower()
        if value == 'y':
            return True
        elif value == 'n':
            return False
        else:
            print("Respond with 'y' or 'n'")

run_all = run_all_code_or_last_code()


if run_all:

    # To create a custom class we use the class keyword, and we can initialize class attributes in the special method __init__.
    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height

    r1 = Rectangle(10, 20)
    r2 = Rectangle(3, 5)

    print(r1.width, r1.height) # 10 20
    print(r2.width, r2.height) # 3 5


    """"
    width and height are attributes of the Rectangle class. But since they are just values (not callables), we call them properties.
    Attributes that are callables are called methods.
    You'll note that we were able to retrieve the width and height attributes (properties) using a dot notation, where we specify the object we are interested in, then a dot, then the attribute we are interested in.
    We can add callable attributes to our class (methods), that will also be referenced using the dot notation.
    Again, we will create instance methods, which means the method will require the first argument to be the object being used when the method is called.
    """
    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height
        
        def area(self):
            return self.width * self.height
        
        def perimeter(self):
            return 2 * (self.width + self.height)
        
    r1 = Rectangle(20, 30)
    area = r1.area()
    perimeter = r1.perimeter()

    print(f"area is {area} and perimeter is {perimeter}")


    """
    Python defines a bunch of special methods that we can use to give our classes functionality that resembles functionality of built-in and standard library objects.
    Many people refer to them as magic methods, but there's nothing magical about them - unlike magic, they are well documented and understood!!
    These special methods provide us an easy way to overload operators in Python.
    For example, we can obtain the string representation of an integer using the built-in str function:
    """

    print(str(10))

    # What happens if we try this with our Rectangle object?

    print(r1) # '<__main__.Rectangle object at 0x103561af0>'


    """
    When we call str(r1), Python will first look to see if our class (Rectangle) has a special method called __str__.
    If the __str__ method is present, then Python will call it and return that value.
    There's actually another one called __repr__ which is related, but we'll just focus on __str__ for now.
    """
    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height
            
        def area(self):
            return self.width * self.height
        
        def perimeter(self):
            return 2 * (self.width + self.height)
        
        def __str__(self):
            return f"<Rectangle (width={self.width}, height={self.height})>"
        
        def __repr__(self):
            return 'Rectangle({0}, {1})'.format(self.width, self.height)

    r1 = Rectangle(10, 20)

    print(r1)
    print(str(r1))
    print(repr(r1))


    # How about the comparison operators, such as == or < ?
    r1 = Rectangle(10, 20)
    r2 = Rectangle(10, 20)

    print(r1 == r2)

    """
    As you can see, Python does not consider r1 and r2 as equal (using the == operator). 
    Again, how is Python supposed to know that two Rectangle objects with the same height and width should be considered equal?
    """

    # We just need to tell Python how to do it, using the special method __eq__.


    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height
            
        def area(self):
            return self.width * self.height
        
        def perimeter(self):
            return 2 * (self.width + self.height)
        
        def __str__(self):
            return f"<Rectangle (width={self.width}, height={self.height})>"
        
        def __repr__(self):
            return 'Rectangle({0}, {1})'.format(self.width, self.height)
        
        def __eq__(self, other):
            same_width = self.width == other.width
            same_height = self.height == other.height
            return same_width and same_height

    r1 = Rectangle(10, 20)
    r2 = Rectangle(10, 20)

    print(r1 is r2)

    # And if we try to compare our Rectangle to a different type:
    print(r1 == 100)

    """
    result:

    Traceback (most recent call last):
    File "/home/lucas/workspace/courses/python-3-deep-dive/part1/S1/07_classes.py", line 146, in <module>
        print(r1 == 100)
    File "/home/lucas/workspace/courses/python-3-deep-dive/part1/S1/07_classes.py", line 134, in __eq__
        same_width = self.width == other.width
    AttributeError: 'int' object has no attribute 'width'
    """


    # It must be validated whether the other comparison object is of the same type
    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height
            
        def area(self):
            return self.width * self.height
        
        def perimeter(self):
            return 2 * (self.width + self.height)
        
        def __str__(self):
            return f"<Rectangle (width={self.width}, height={self.height})>"
        
        def __repr__(self):
            return 'Rectangle({0}, {1})'.format(self.width, self.height)
        
        def __eq__(self, other):
            if isinstance(other, Rectangle):
                same_width = self.width == other.width
                same_height = self.height == other.height
                return same_width and same_height
            return False


    r1 = Rectangle(10, 20)
    r2 = Rectangle(10, 20)

    print(r1 == r2)
    print(r1 == 100)

    """
    What about <, >, <=, etc.?
    Again, Python has special methods we can use to provide that functionality.

    These are methods such as __lt__, __gt__, __le__, etc.
    """
    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height
            
        def area(self):
            return self.width * self.height
        
        def perimeter(self):
            return 2 * (self.width + self.height)
        
        def __str__(self):
            return f"<Rectangle (width={self.width}, height={self.height})>"
        
        def __repr__(self):
            return 'Rectangle({0}, {1})'.format(self.width, self.height)
        
        def __eq__(self, other):
            if isinstance(other, Rectangle):
                same_width = self.width == other.width
                same_height = self.height == other.height
                return same_width and same_height
            return False

        def __lt__(self, other):
            if isinstance(other, Rectangle):
                return self.area() < other.area()
            else:
                return NotImplemented

    r1 = Rectangle(100, 200)
    r2 = Rectangle(10, 20)

    print(r1 < r2)


    # What about >?
    print(r1 > r2) # True

    """
    How did that work? We did not define a __gt__ method.
    Well, Python cleverly decided that since r1 > r2 was not implemented, it would give

    r2 < r1

    a try. And since, __lt__ is defined, it worked!
    Of course, <= is not going to magically work!
    """
    r1 <= r2 # TypeError: '<=' not supported between instances of 'Rectangle' and 'Rectangle'


    """
    If you come from a Java background, you are probably thinking that using "bare" properties (direct access), such as height and width is a terrible design idea.
    It is for Java, but not for Python.

    Although you can use bare properties in Java, if you ever need to intercept the getting or setting of a property, 
    you will need to write a method (such as getWidth and setWidth. The problem is that if you used a bare width property for example, 
    a lot of your code might be using obj.width (as we have been doing here). The instant you make the width private and instead implement getters and setters, you break your code. 
    Hence one of the reasons why in Java we just write getters and setters for properties from the beginning.
    With Python this is not the case - we can change any bare property into getters and setters without breaking the code that uses that bare property.

    I'll show you a quick example here, but we'll come back to this topic in much more detail later.

    Let's take our Rectangle class once again. I'll use a simplified version to keep the code short.
    """

    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height
        
        def __repr__(self):
            return 'Rectangle({0}, {1})'.format(self.width, self.height)
        
    r1 = Rectangle(10, 20)
    print(r1.width)
    r1.width = 100
    print(r1.width)


class Rectangle:
    def __init__(self, width, height):
        self._width = None
        self._height = None
        # now we call our accessor methods to set the width and height
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError('Width must be positive.')
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError('height must be positive.')
        self._height = height

    def area(self):
        return self._width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return f"<Rectangle (width={self.width}, height={self.height})>"
    
    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)
    
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            same_width = self.width == other.width
            same_height = self.height == other.height
            return same_width and same_height
        return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented
        

r1 = Rectangle(-10, 20)
print(r1.width)
print(r1.height)
# r1.width = -100
print(r1.width)
