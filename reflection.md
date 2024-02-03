Use this file to record your reflection on this assignment. 

## What worked, what didn't, what advice would you give someone taking this course in the future?

### What worked: 

The initialization of the classes and most of the methods were actually less confusing to implement than I thought they would be. Once I got a feel for when to use *self* (the "when in doubt, use it" mindset worked pretty well), the rest of the code was very similar to other python programs I've written before. 

### What didn't work:

Orignally I tried to check if a computer was in the inventory by creating a logical statement of `self.inventory.index(item)`. My hope was that it would return true if the index existed, and false if it didn't (so I could then use that logical to feed my `if... else`). Unfortunately, I'm not quite sure what it returned if true, and it threw an error when false. I was convinced for a while that I had messed up my syntax, and even had to go back into my `computer.py` file to see if I needed to change the `__str__()` output for it to work. Eventually, I realised that it would be simpiler to use a `if item in self.inventory` statement to check. This DID return `FALSE` when the computer wasn't in the inventory, so that swap solved the issue! 

Also, I was very confused about how to access the classes defined in one `.py` file within a different file. Thanks Jordan for helping me out in office hours with that one! 

I also *definitely* didn't commit frequently enough ... I kept waiting to commit until the next task was completely done and then suddenly the project was finished. I'm gonna try to have better committing practices next time around.

### Advice

I would start this early so that there is enough time to sit with the problem and absorb it, do some work, and then go to office hours when you inevitably hit a wall. 