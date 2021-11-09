# Chapter 2

## List of built-in Data Collections

### Lists
- `list_sample = ['a','b','1','2','@','$']`
- Ordered, mutable collection of objects
- heterogenous
- can be dynamically resized
- List Modifiers - remove, pop, extend and insert

#### list.remove(object) 
- Use it to remove a specific item in a list


```python
>>>list = [1,2,3,4]
>>>list
[1,2,3,4]
>>>list.remove(1)
[2,3,4]
```

#### list.pop(index)
- Use it to remove an item based on index within a list. By default it will remove the last item in the list.

```python
>>>list = [1,2,3,4]
>>>list
[1,2,3,4]
>>>list.pop(1)
[2,3,4]
```

#### list.extend([list])
- Takes a new list and appends it to the current list.

```python
>>>list = [1,2,3,4]
>>>list
[1,2,3,4]
>>>list.extend([5])
[1,2,3,4,5]
```

#### list.insert(index,object)
- Takes an index and an object, and inserts the object at the specified index.

```python
>>>list = [1,2,3,4]
>>>list
[1,2,3,4]
>>>list.insert(0,0)
[0,1,2,3,4]
```

