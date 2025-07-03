
# COMP 170 SU25 WEEK 06

This assignment has two parts: a coding part based on current material we discuss in class and a reflection part to evaluate work you have already submitted.





## Finals week policy

There is no final exam for the course. There will be a final assignemnt that will be published the week before finals and will be due the week of finals. Additionally, 8 students in the course will be invited randomly to a brief meeting with the instructor during the course's final exam slot. The final exam slot for this course is on Tuesday, August 5, 2025 from 11 AM to 1 PM. If you are selected for a brief meeting, we'll spend about 15 minutes during the final exam slot to review your work. This interview will cover coding practices based on your past assignments. It is meant as a checkpoint to ensure that you have internalized the work you submitted.


## Code

This assignment will give you practice with reading data from files, performing basic numerical analysis, and applying simple text-based markup transformations. You will complete three tasks, each involving file input, processing, and output using Python.

Write your code in file `week06.py`. The file comes with a bit of testing code. Do not modify the testing code. Write your methods *above* the testing code. If your methods are correct, running the testing code will show that you passed the tests. In addition to correct logic, your methods must have **one and only one** return statement each. Useful comments are required.


## Code requirements
* Methods that return a value should have one and only one `return` statement. Multiple `return` statements are not allowed.
* Methods with `print` statements should not have a `return` statement.
* The following commands should **not** be used: `import`, `break`, `continue`.


### Load and Analyze Temperature Data

You are given a file called `temperatures.txt` in folder `data`, which contains one temperature per line. Write a function that reads all the temperature values from the file into a list of floating-point numbers. The header of your method must be:
```python
def load_to_list(filepath: str) -> list[float]:
```

Then write another method with header
```python
def descriptive_statistics(source_data: list[float]) -> None:
```
that computes and prints:

* The total number of temperatures
* The average temperature (rounded to two decimal places)
* The minimum and maximum temperatures

When testing your code with the input in `data/temperatures.txt` the output should be
```text
There are 19 values in the data source.
The average value is 70.26
The highest value is 81.0 and the smallest value is 5.0.
```


### Apply Simple Markup to Text

You are also given a file called `markup.txt`, which contains a short passage using a basic markup syntax. A word in the text may be prefixed by:

* a dot (.) to indicate that it should be printed in UPPERCASE.
* an underscore (_) to indicate that it should be printed in expanded form, with spaces between its letters.

Write a function that reads this file line by line, applies the formatting rules described above, and prints the resulting formatted text to the screen.

Use the function header:

```python
def apply_markup(filepath: str) -> None:
```

Here are some basic input/output examples:

| Input | Output |
|-------|--------|
| `In a hole in the ground there lived a hobbit` | `In a hole in the ground there lived a hobbit` |
| `In a hole in the .ground there lived a hobbit` | `In a hole in the GROUND there lived a hobbit` |
| `In a _hole in the ground there lived a hobbit` | `In a  h o l e  in the ground there lived a hobbit`|

When testing your code with the input in `data/markup.txt`, the output should be:
```text
Markup is a technique where FORMAT INSTRUCTIONS are inserted as part of a 
text file. In this file, a word precedeed by a DOT should be printed in 
upper case. And a word precedeed by an UNDERSCORE should be typed in expanded 
form, with spaces between its letters. Such formatting brings attention 
to KEY elements of a text, through  c l a r i t y  and  f o c u s 
```

## Reflect

Review the posted [solutions from the previous assignment](./solutions_week04.py). Compare the posted solutions with your solutions. Notice the differences between your code and the solutions code and describe them. Trivial differences like the names of variables are not that important.

### Frequent mistakes expected at this point

* **If you did not request the testing code from Leo** your assignemnt is incomplete.

* **Your methods have multiple return.** This usually happens with AI-generated code or with code found online. There is nothing wrong with using these resoruces *as long as you study the code you find, understand how it works, and adjust it to meet the assignemnt specifications.*

* **Code fails one or more tests**. EXCEPT HELLO/HELO

* **Code has no comments** to demonstrate mastery of the program.

* **Code does not produce correct outputs** because it was not tested after completed.

* **Code uses excessive logic** which may be the sign of AI-generated programs.

* **Code does not include type hints (annotations).** This is also typical with solutions found online or are AI-generated.


### Read more about:

* [Type hints in Python](https://docs.python.org/3/library/typing.html); also useful [cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html#functions)
* [f-strings in Python](https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings)
* [lists in Python](https://docs.python.org/3/tutorial/datastructures.html). Also chapters 7.1 and 7.2 of the textbook.
* [the for statement](https://docs.python.org/3/reference/compound_stmts.html#for) and [for loop over a list in Python](https://docs.python.org/3/tutorial/controlflow.html#for-statements). Also chapter 2.3 and 7.1 of the textbook.
