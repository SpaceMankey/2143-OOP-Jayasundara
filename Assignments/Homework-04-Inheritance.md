# Inheritance
10/23/2016

###Answer 1
```python
class Cat(Pet):
    def __init__(self, name, owner, lives=9):
    	Pet.__init__(self,name,owner)
    	self.lives = lives

    def talk(self):
        """A cat says meow! when asked to talk."""
        print('meow!')

    def lose_life(self):
        """A cat can only lose a life if they have at least
        one life. When lives reach zero, the ’is_alive’
        variable becomes False.
        """
        if (self.lives >= 1):
        	self.lives = self.lives - 1
        else:
        	self.is_alive = False
```

###Answer 2
```python
#Line 1 prints
4
#Line 2 prints
3
#Line 3 prints
AttributeError: 'Foo' object has no attribute 'baz'
#Line 4 prints
3
#Line 5 prints
9
#Line 6 prints
16
```
