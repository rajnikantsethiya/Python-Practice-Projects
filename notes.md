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

##
