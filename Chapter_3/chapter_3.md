# Chapter 3

## List of built-in Data Collections

1. Dictionaries
2. Tuples
3. Sets

### Dictionaries
- `dict_sample = {'a':'1','b':'2','c':'3'}`
- Unordered set of key-value pairs
- Allows you to store collection of key-value pairs that are unique 
- Can be dynamically reszied
- Unordered and mutable
- Like a 2 cloumned multi-row data structure
- Sample - dict = {'key':'value'} / person_details = {'Name':'Harish'}
- Retrive a value - dict['key'] / person_details['Name']
- Curly brackets to manipulate / square brackets to retrieve
- To add a new key-value pair - dict['new_key'] = 'value'
- `setdefault` method takes care of initialization.



### Tuples
- `sample_tuple = ('a','b','c','d')`
- Ordered, immutable collection of objects
- heterogenous
- cannot be dynamically resized. Once defined, cannot be modified.
- supports the suqare bracket notations like lists - `sample_tuple[1]`



### Sets
- `set_sample = {'a','e','i','o','u'}`
- Unordered set of unique objects. Insertion order is never maintained.
- Allows to perform mathematical Unions, Intersections and Differences
- Like Lists and Dictionaries, can be resized dynamically.
- `set.union(object)` -Union method Takes unique values from two sets and combines them
- `set.difference(object)` -Difference method Takes unique values not in either of the two sets and combines them
- `set.intersection(object)` - Intersection method takes the common unique values between the two sets


