# Lesson 2

## Setup

```bash
pip install -r requirements.txt
```

## Unit tests

Test run a specific test:

```bash
python -m unittest -v tests/lesson_2/test_multiply.py
```

## Exercise 1

### Exercise 1 - Description

When multiple developers work on a project, sometimes they need to modify the same file. This exercise will simulate that scenario.

### Exercise 1 - Steps

1. Create a new repository with README.md in your own github named `merge_conflict`
2. Clone the repository
3. Create and checkout a branch named `ISSUE-1`
4. Add following lines of text to README.md, commit and push

    ```markdown
   # merge_conflict

    1. some text
    2. some text
    3. some text
    4. some text
    ```

5. Checkout `master`
6. Create and checkout a branch named `ISSUE-2`
7. Add following lines of text to README.md, commit and push

    ```markdown
    # merge_conflict

    1. another text
    2. another text
    3. another text
    ```

8. Open and merge PR from `ISSUE-1` to `master`
9. Open a PR from `ISSUE-2` to `master`
10. What happens? Solve the merge conflict.

## Exercise 2

### Exercise 2 - Description

Use the (Red - Green - Refactor) mentality to solve this exercise.

Write a function that returns the sum of x, y and adds 5. i.e

* x = 5, y=1 should return 11
* x = -5, y=1 should return 1

### Exercise 2 - Steps

1. Add a new test file to the tests/lesson_2 folder (make sure to name it according to the default discovery pattern test*.py)
2. Add a file with the function to test in lesson_2 (see utils.py as an example)
3. Run the test with vscode make sure it fails (Red)
4. Run the test through the terminal, make sure it fails (optional)
5. Write the function so the test passes
6. Run the test again and make sure it's (Green)
7. Refactor if something is not up to standard
8. Repeat step 3 - 7 and add tests for negative values, wrongful type i.e x = "hello", y = "world"
9. When you are done, create a PR against master (DON'T MERGE IT)

## Links

- [Read more about tox config](https://tox.readthedocs.io/en/latest/config.html)
- [Read more about flake8 options](https://flake8.pycqa.org/en/latest/user/options.html)
- [Read more about vscode and Python testing](https://code.visualstudio.com/docs/python/testing)
- [Plugin that show coverage in vscode](https://marketplace.visualstudio.com/items?itemName=ryanluker.vscode-coverage-gutters)
- [Read more about builtin unittest](https://docs.python.org/3/library/unittest.html)
- [Read more about pytest a popular alternative to the builtin unittest](https://docs.pytest.org/en/stable/)