# Further Algorithm Practices

For this exercise you are going to try and write the following algorithms as a flowchart. You can then try and write them using the [Pseudocode Compiler](http://ibcomp.fis.edu/pseudocode/pcode.html). They are listed from easy to hard.

Easier
---
1. ### Change ###
    In the UK money is broken down into the following denominations:
    
    £50, £20, £10, £5, £2, £1, 50p, 20p, 10p, 5p, 2p, 1p

    Your task is to write some code that outputs a list of the optimal change for a transaction. EG: I pay £20 for my purchase of £14.27. The function should return an array of [5, 0.50, 0.20, 0.02, 0.01] as these are the coins that would make up the correct change. The list __should__ contain duplicates if necessary.

2.  ### Sentence search ###
    You should write some code that takes as it's parameters _text_ and _search_term_. The function will then look through the _text_ and find all sentences that contain _search_term_ and return them as a collection.

3.  ### Prime finder ###
    Write code to determine if a number is a prime number. You should take an input and return True if the number is prime and false otherwise. You should also determine what is the big O of this algorithm and try and spot any quick optimisations.

Harder
---
4. ### Number Spiral ###
    Make a number spiral. A number spiral is a 2D array of numbers starting from 1 and spiralling out like this :

    ```python
    17 < 16 < 15 < 14 < 13
     v                  ^
    18   5  <  4 <  3   12
     v   v          ^   ^
    19   6     1 >  2   11
     v   v              ^
    20   7  >  8 >  9 > 10
     v
    21 > 22 > 23 > 24 > 25
    ```

    Your task is to write code that takes a parameter and maps that into a 2D array going to the number squared. You do not have to draw the arrows from above (although if you want a challenge, go for it). So an input of 3 would lead to a number spiral like this:

    ```
    5 4 3
    6 1 2
    7 8 9 
    ```

    Which should be returned as either strings or a 2D array.


5.  ### Rotate array ###
    You should write code that takes a 2D array and rotates it a certain number of _steps_. 

    As an example. The following array is your input 
    ```python
    a    b    c    d 
    e    f    g    h
    i    j    k    l
    m    n    o    p
    q    r    s    t
    ```

    If it is rotated by 2 steps the output would be :
    ```python
    c    d    h    l
    b    k    o    p
    a    g    n    t
    e    f    j    s
    i    m    q    r
    ```

    You should write the code to achieve this.