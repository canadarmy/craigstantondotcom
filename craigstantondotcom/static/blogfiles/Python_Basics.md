# Python Fundamentals Critical for Django



## Class vs Object vs vs Attribute vs Method

* **Class** = set of instructions or blueprint for how to build many objects that share characteristics
* **Object** = data type built according to specifications provided by the class definition
* **Attribute** = feature/value/characteristic. In other words, its a variable that is stored within an object.
  * Anything bound to an object
* **Method** = set of instructions; functions associated with an object
  * Differs from a *function* only because it is associated with an instance or object




## What happens when you create an object?

Think **namespace**:

- The *linkage* of the name of an object in python and the actual object

- Currently set as a dictionary `{name_of_object: object}`

- No relationship between names in different namespaces

- - Can have 2 functions named `maximize()` - you just have to prefix with the module



## What is an attribute?

* Fundamental part of everything in Python
* Every object has an attribute
  * Run the `dir()` function on any object to get a list of attributes
* When you hear people say *instance variables*, they mean *attributes*

### So what is the deal with the dot notation?

You have seen the dot notation as `objectinstance.attribute` but what is the significance?

- This is the short form of `getattr()` and `setattr()` functions

- Basically, this easily allows you to create, set, and override object attributes easily:

  - ```python
    >>> f = Foo()
    >>> setattr(f, 'x', 5)
    >>> getattr(f, 'x')
    5
    >>> f.x
    5
    >>> f.x = 100
    >>> f.x
    100
    ```

    - Note that it didn't matter if `x` existed beforehand. By simply assigning a value to it, the attribute was created

### How do you create attributes for instances?

There are two ways:

1. In the `__init__` of each instance
2. "Adhoc" assignment (`f.bar = 100` where f is the instance of Foo class, and bar is the new attribute)

### Can you assign an attribute to *any* object?

What a weird question...but yes you can. Functions are objects, therefore below is perfectly valid

```python
def hello():
    return "Hello"

>>> hello.abc_def = 'hi there!'

>>> hello.abc_def
'hi there!'
```

### Great, so I can create attributes anywhere I want!

Not quite - just because you can, doesn't mean you *should*.

What we are doing above is creating an attribute *inside* of `__init__`

```python
class Foo(object):
    def __init__(self, x):
      self.x = 5
```

This is the equivalent:

```python
Foo.x = 5
```

Therefore, it is *cleaner* but slower to create and assign attributes inside the `__init__`

<u>Rule of thumb</u>: create object (ie. instance) attributes inside `__init__` even if it is to just assign a `None` value - it is just cleaner for everyone

### If classes are also objects, can we assign attributes to them?

Yes.

```python
>>> Foo.bar = 100
>>> Foo.bar
100
```

So how is this different than sticking an attribute in the `__init__` of each instance, or creating the instance attributes adhoc (ie. `f.bar = 100` where f is the instance of Foo class, and bar is the new attribute)?

### So if attributes can be assigned to any objects (classes and their instances), how do we know which one Python processes first?

Remember that attributes can be assigned to classes in a number of ways:

* Via the `__init__` method

  * ```python
    class Foo(object):
        def __init__(self, x):
          self.x = 5
    ```

* Via direct instance assignment

  * `f.bar = 5`

* Via class assignment

  * ```python
    class Foo(object):
    	x = 5
    ```

There is a difference between the body of a function definition (the block under `def` statement: `self.x = 5` above) and the body of a class definition (the block under the `class` statement: `x=5` above)

* Function body is only executed when we *invoke* the function
* Class definition is executed *immediately* and only once - when we define the function

**The point of the above**: *none of these assignments are variables*, regardless of whether they're assigned to classes or instances. These are all ***attributes*** of each object, regardless of the object type

​	<u>The result</u>: by creating a new function with `def` inside of a class definition, you are really **creating a new attribute with that name on the class**.

​	In other words, **instance methods sit on a ___class___ in Python, <u>not on an instance</u>**

​		Say you have the following:

```python
class Foo(object):
	def blah(self):
      return "blah"

f = Foo()

f.blah()
```

 When you call `f.blah()` , Python is invoking the `blah` method on `Foo` and passing `f` as the first argument. There is **no difference** between `f.blah()` and `Foo.blah(f)`. This is the reason we need to catch the object with `self` - self represents instance f when calling Foo.blah



### Wait, how does Python know to invoke Foo.blah when calling f.blah()?

When they are different objects: f is an instance of Foo, and Foo is an instance of type?? Why does Python looking for blah on Foo??

Variable and attribute scoping

 * For variables, Python follows LEGB (Local, Enclosed, Global, Builtin)
* For attributes, the scoping is analyzed in this order:
  1. Looks at object in question (`f` - but Python doesn't find an attribute named blah)
  2. Then at objects class (`Foo` - Python finds the attribute here, thus invokes blah on f)
  3. Then goes up the class inheritance chain until it reaches "object" at the top

**Moral of the story**: Python does not have 'instance variables' or 'class variables'

 * It has *objects with attributes*
    * Some attributes are defined on classes, other attributes are defined on instances



**Do not** create an attribute on an instance that has the same name as an attribute on an object





## Why do you insert object in Class(object):

It is the highest level Class that does this. For classes that inherit from other classes, this





Python Basics for Django

## Class & Instance Attributes

* Class has **instances** of the class object
* You can define attributes at both the *class* and *instance* level



### How do you create a class attribute?

![Class vs. Instance Attributes_1](blog_pics/Python Basics for Django/Class vs. Instance Attributes_1.png)

* Note how class attributes are assigned at the **top** of the class with an **'='**
* Note that **x,y** are *instances* of **class A**
  * `a` is an *attribute* of **class A**
  * Therefore calling `x.a` returns the *class-level attribute* for `x`
    * ***NOTE*** this is not assigning an instance-level attribute, but rather *inheriting* the class attribute



### How do you override a class attribute?

![](blog_pics/Python Basics for DJango/Class vs. Instance Attributes_2.png)

* Notice how `x.a` has been reassigned using the **'='** sign - it is now an *instance attribute*
* No instance attribute has been assigned for `y.a`  so it returns the old class attribute
* ***NOTE*** we can change the value of the class attribute (using the format `Class.Attribute`)
  * When `A.a` is changed, so is `y.a` but `x.a` stays the same since it has the instance attribute



### Technical Reasons for the Above

* Python stores class and instance attributes in **different dictionaries**

![Class vs. Instance Attributes_3](blog_pics/Python Basics for Django/Class vs. Instance Attributes_3.png)

* Empty dict for `y`




## Methods vs Functions

1. Creating code to perform some action:

* Function:

  * ```python
    def example(a, b):
      return a + b
    ```

* Class method

  * ```python
    class Example(object):

      def method(self, a, b):
        self.contents = a + b
        return self.contents
    ```

2. Calling the above:

* Function:

  * ```python
    example(1, 2)
    >>> 3
    ```

* Class method

  * ```python
    instance = Example()

    instance.method(1,2)
    >>> 3
    ```

    * Note you have to **instant**iate the class, to create an **instance**

3. What if you didn't want to instantiate an instance from the class above?

   * Create a ***static method*** - function named in the class namespace
     * Used if you want to include functions only for this particular class but not any one
       particular instance of that class

   ```python
   class Example(object):

   	@staticmethod
   	def method(a, b):
   	return a + b

   Example.method(1,2)
   >>> 3
   ```

   * Note how you do not have to call *self*




## What is \__init__.py?

File (usually empty) that identifies the directory as having python *packages*

Say you have the following:

```python
mydir/spam/__init__.py
midir/spam/module.py
```

Assuming `mydir` is on your path, you can import the code in `module.py` as:

```python
import spam.module

# OR

from spam import module
```

Without `__init__.py` Python will no longer look for subpackages in this directory, so attempts to import`module` will **fail**




## Decorators

* There is still more to be written on this topic

* ​

  ​

  ​
