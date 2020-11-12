# Lesson 4

## Exercise 1

### Description

Last lesson we learned that it takes time and can be hard to write test for existing code. This lesson we will refactor the code so we can test it.

### Steps

1. Update your branch with the latest updates in master branch.

2. The cloud_sdk.py is delivered by a 3rd party, so you can't test it with unit tests. You should make the usage replaceable in api.py. Either by adding it as a default argument or rewriting it as a class. Then you can easily replace it with a "dummy" function in the code.
OR solve it with a mock <https://docs.python.org/3/library/unittest.mock.html>

3. Implement the restart feature, also write tests.

4. Run tox and make sure you have good coverage.

5. Create a Pull Request to hand in your assignment.
