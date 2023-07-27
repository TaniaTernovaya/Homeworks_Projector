<!-- Add CSS style for color customization -->
<style>
/* Header 1 style */
h1 {
  color: #2ecc71; /* Green color */
}

/* Header 2 style */
h2 {
  color: #3498db; /* Blue color */
}

/* Header 3 style */
h3 {
  color: #f39c12; /* Orange color */
}

/* Code block style */
pre {
  background-color: #f0f0f0; /* Light gray background */
  padding: 10px;
  border-radius: 5px;
  font-family: "Courier New", monospace;
}
</style>

This repository contains my completed homework assignments, each organized into separate folders based on the assignment number. Each folder (e.g., "Homework_8") contains Python files that correspond to the solved tasks on various topics.

## Table of Contents

1. [Introduction](#introduction)
2. [Homework Assignments](#homework-assignments)
3. [How to Use](#how-to-use)
4. [Contributing](#contributing)
5. [License](#license)

## <span style="color:#2ecc71">Introduction</span>

Welcome to the Homework Projector repository! This collection of homework assignments showcases my problem-solving and coding skills. Each folder represents a specific homework assignment, and within each folder, you'll find Python files that demonstrate my solutions to the given tasks.

As I progress through my academic journey, I will continuously add new completed homework assignments to this repository. Feel free to explore the folders and code files to get a sense of the topics covered and the complexity of the problems solved.

## <span style="color:#3498db">Homework Assignments</span>

The repository currently includes the following homework assignments:

1. [Homework 8](./Homework_8) - Complexity.Algorithms
2. [Homework 9](./Homework_9) - Modules
3. [Homework 10](./Homework_10) - Context Manager. Files
3. [Homework 11](./Homework_11) - Network.Requests


As I complete more homework assignments, this list will expand to cover a wide range of programming concepts and problem-solving techniques.

## <span style="color:#f39c12">How to Use</span>

To explore the code and solutions for each homework assignment, navigate to the corresponding folder of interest. Inside each folder, you will find Python files with filenames that reflect the specific tasks addressed in the assignment. Feel free to examine the code, comments, and any accompanying documentation to understand my approach to each problem.

# <span style="color:#2ecc71"> Homework 8 - Cats with Hats

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
