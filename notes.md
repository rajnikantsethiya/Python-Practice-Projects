## There are four collection data types in the Python programming language:

- List is a collection which is ordered and changeable. Allows duplicate members.
- Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
- Set is a collection which is unordered, unchangeable\*, and unindexed. No duplicate members.
- Dictionary is a collection which is ordered\*\* and changeable. No duplicate members.

## Ordered

    When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

    If you add new items to a list, the new items will be placed at the end of the list.

## unchangeable

    When the collection is unchangeable means the values are created and memory has been allocated you can't update that memory by updating the value. if We add or remove items from collection it ll create new memory location.

## Sets & frozensets

- In sets, True and 1 , False and 0 are considered duplicated and throws error as Sets doesn't allow duplicate values.
- Union method in Sets allowed other data collection types to be added like set and a tuple.
- frozenset is considered as immuatable data types which doesnt allow to add or remove the items. frozensets are unique, unordered, unchangeable.

## Dictionaries

    Dict values are ordered, changeable and doesn't allow duplicates.

## Data type methhods

## Methods of List

- append() Adds an element at the end of the list
- clear() Removes all the elements from the list
- copy() Returns a copy of the list
- count() Returns the number of elements with the specified value
- extend() Add the elements of a list (or any iterable), to the end of the current list
- index() Returns the index of the first element with the specified value
- insert() Adds an element at the specified position
- pop() Removes the element at the specified position
- remove() Removes the item with the specified value
- reverse() Reverses the order of the list
- sort() Sorts the list

## Methods of Tuple

- count() Returns the number of times a specified value occurs in a tuple
- index() Searches the tuple for a specified value and returns the position of where it was found

## Methods of Sets

- add() Adds an element to the set
- clear() Removes all the elements from the set
- copy() Returns a copy of the set
- difference() - Returns a set containing the difference between two or more sets
- difference_update() -= Removes the items in this set that are also included in another, specified set
- discard() Remove the specified item
- intersection() & Returns a set, that is the intersection of two other sets
- intersection_update() &= Removes the items in this set that are not present in other, specified set(s)
- isdisjoint() Returns whether two sets have a intersection or not
- issubset() <= Returns True if all items of this set is present in another set
  < Returns True if all items of this set is present in another, larger set
- issuperset() >= Returns True if all items of another set is present in this set > Returns True if all items of another, smaller set is present in this set
- pop() Removes an element from the set
- remove() Removes the specified element
- symmetric_difference() ^ Returns a set with the symmetric differences of two sets
- symmetric_difference_update() ^= Inserts the symmetric differences from this set and another
- union() | Return a set containing the union of sets
- update() |= Update the set with the union of this set and others

## Methods of Frozenset

- copy() Returns a shallow copy
- difference() - Returns a new frozenset with the difference
- intersection() & Returns a new frozenset with the intersection
- isdisjoint() Returns whether two frozensets have an intersection
- issubset() <= / < Returns True if this frozenset is a (proper) subset of another
- issuperset() >= / > Returns True if this frozenset is a (proper) superset of another
- symmetric_difference() ^ Returns a new frozenset with the symmetric differences
- union() | Returns a new frozenset containing the union

## Methods of Dictionary

- clear() Removes all the elements from the dictionary
- copy() Returns a copy of the dictionary
- fromkeys() Returns a dictionary with the specified keys and value
- get() Returns the value of the specified key
- items() Returns a list containing a tuple for each key value pair
- keys() Returns a list containing the dictionary's keys
- pop() Removes the element with the specified key
- popitem() Removes the last inserted key-value pair
- setdefault() Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
- update() Updates the dictionary with the specified key-value pairs
- values() Returns a list of all the values in the dictionary

## Functions

- Functions works in same way as every other language uses, like avoiding the repetition, defining wit "def". can have named and anonymous (lambda) functions
- function has 4 type of scope
  - Local - Inside the current function
  - Enclosing - Inside enclosing functions (from inner to outer)
  - Global - At the top level of the module
  - Built-in - In Python's built-in namespace
- functions have different type of arguments
  - positioned arguments
  - named arguments
  - keyword arguments
  - dictionary arguments
- For positioned-only arguments use , /
- For keyword only arguments use \*, should use before the arguments

  By using above syntax in function porameters, it ll throw error if we send other type or args.

- When not sure on the function parameter, use \* with varible for positioned args and \*\* for key-pair args.
- with \* you'll receive a tuple of args
- with \*\* you'll receive a dict of args
- Example of combinations - def Main(title, \*skills, \*\*hobbies)
  - title is a named args
  - skills would be a tuple
  - hobbies would be a dict
- Function decorators are used to decorate the actual function
  def Main(func):
  def inner():
  return(func())
  return inner

  @Main ## this is a decorator here
  def sub():
  return("This is a sub function")

- This can be used with input params as well
- To functions body, there are 2 methods, **name**, **doc**
  - name gives the functions name, for decorator it doesnt return the original function name, hence to fix this use built-in method functools.wraps(func)
  - doc gives the documentation availabe in the functions. ideallt defined with """ and at the top of the function.
- lambda is the anonymous functions which can be used for short span of time.
  - mostly used with map, filter, sort or iteratable options
  - lambda x: x+1
  - with map - list(map(lambda x:x+1, iterable_list))
- Recursion function can be used for recursive operations, default limit is 1000, to increase use sys.getRecursionLimit(num)
- Recursive function has 2 things, base case and recursive case.

## Comprehension

- Compresions are used as an additional methods which can be used to solve the problems with efficient code and single line solution
- it uses for loop under the hood nothing fancy or buit-in methods are also supported

## Generators

- Generators are normal functions which can return of accept values but it has a special quality of resuming back the function execution where it left off.
- yield is reserved keywork which is used for returning values or accepting values.
- Generator can return, accept or reference value from other generators

## OOP / Classes

- Object oriented programming is always about classes and objects only
- In python mostly everything is an Object, even the class in python is object constructor
- it follows oop concepts like same as other programming languages.
- An Object or Instance of an class is an copy of its blueprint which is Class.

  # Namespace

  When a varibale value is changed on instance, if affeces only the context which could be Object/instance of class. Class context will remain as is. This is called as Namespaces which keeps the context as namespace.

  # Shadowing

  When a variable is modified or deleted in object's context, It doesnt impact the class and when the deleted varibale is accessed, it provided the value of class's context. This is called shadowing of variables.
  If the deleted variable was created in Object's context, it will throw an error.

  # Constructor (**init**)

  - In python, **init** function is called as constructor which can be called explicitly or it will be called internally if not called explicitly
  - This constructor function takes care of handling the input parameters and keeping them as a blueprint reference for internal methods.

  # Inheritance and Composition

  - Inheritance is a way of accessing the properties and attributes of base class in a new class. which helps in reducing the redundant codebase and can re use the existing base class methods and other things.
  - Nested inheritance is possible to any extent, there is no limit on this.
  - For inheriting the class to another class, just pass the classname to other class where it need to be inherited.
  - class Main() -> class Extend(Main) - Its done !
  - Composition is another way of inheriting classes, The major difference from the traditional inheritance is it just holds the reference of the base class instead creating a object or creating instance of the base class. This helps in memory effifciently as the base class is not executed in it. It ll be executed later in the class once its instance is created.
  - Base class can be accessed explicitly or with Super keyword
  - When a constructor is created in child class, it no longer inherits the base class property until the Super is added in child class constructor.
  - MRO (Method resolution order is used to multiple inehritance)
  - Multiple inheritance can be identied by the inherited classes order
  - Static methods and Class methods are built in decorators designed to extend the constructor.
  - These decorators doesnt have access to Self in class and Classmethod would have cls access which is a class reference so that it can access and extend

  # Encapsulation with private properties and methods

  - Encapsulation means hiding data from outside world.
  - Hiding comes when we want to keep somwething private or protected. hence We can achive this by creating private methods and properties.
  - We can use \_\_ for creating private properties and methods, this would need a getter and setter for using outside the class.
  - Private methods can only be accessed and used inside the class.
  - We can use \_ for protected properties, this tells developer that this is for internal use , can access directly with an \_ but not recommened.

  # Exception handling

  - This just like try catch but in python we have 4 things.
    - try..except..else..finally
  - you can define and raise multiple exceptions, these can be stored in a separate file and use them like util method.
  - We can create own exceptions as well as utils and use them.
