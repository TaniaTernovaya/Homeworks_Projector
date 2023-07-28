# Homework 8 - Cats with Hats :cat:

## Task Description

In this assignment, you are given 100 cats arranged in a giant circle. Initially, none of the cats have any hats on. You will walk around the circle 100 times, always starting at the same spot with the first cat (cat #1). Every time you stop at a cat, you will either put a hat on it if it doesn't have one on or take its hat off if it has one on.

Your task is to implement a Python function called `cats(number_cats, number_round)` that simulates this process and returns a list of cat indices that have hats at the end of the 100 rounds.

## Implementation

You can use the provided Python function `cats(number_cats, number_round)` to solve this problem. The function takes two arguments: `number_cats`, which represents the total number of cats (in this case, 100), and `number_round`, which represents the number of rounds to walk around the circle (also 100).

The function creates a list `cats` representing the cats, where each element is initially set to 1, indicating that no cat has a hat. It then iterates through each round from 2 to `number_round` (inclusive) and flips the status of the cats' hats based on the round number.

At the end of the process, the function returns a list `result` containing the indices of cats that have hats (1-based index).

## Usage

To find out which cats have hats at the end of the 100 rounds, you can call the `cats(number_cats, number_round)` function and print the result. For example:

```python
result = cats(100, 100)
print(result) 
```
Running the above code will output a list of cat indices that have hats after the 100 rounds.