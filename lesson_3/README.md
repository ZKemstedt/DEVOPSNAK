# Lesson 3

## Tips

To debug a test:

```bash
python -m unittest -v tests.lesson_3.test_utils.UtilsTests
```

To run file in module:

```bash
python -m lesson_3.deploy_cli
```

## Exercise 1

### Exercise 1 - Description

You are as a group tasked to improve the deployment tooling (CLI). A developer who no longer works for company, thought it was a good idea to just start coding. So you already have some code (but without tests). You want to work according to `TDD` so you setup a task force to tackle the bad coverage and make sure the tool work as intended. The team doesn't know how to test all parts by code, so some `manual test cases` need to be written.

There are some requirements specified in a previous meeting:

* We need to write `manual test cases` for the most important use cases.
* We want to improve `unit test coverage`.
* The tool is CLI based and the user should be able to run it with the following arguments:
  * `region` i.e. eu-west-1, us-south-1.
  * `service` i.e. frontend, backend
  * `conf` i.e test (default), production
  * `cluster` i.e `127.0.0.1` or `example.com`
  * `timeout` i.e 1m (default) or 1h
* When a deployment fails the program should exit with code 255.

### Exercise 1 - Steps

1. Always start by reading the code, before you run unknown tooling.
2. You can now run the tool and do `exploratory testing` of `deploy_cli.py`
3. Write at least 10 `manual test cases` for the most common use cases. Write them with this template:

    ```text
    Test-id: CLI-1
    Test-name: CLI option "service"
    Description: When argument service=<component> is provided the deployment tool should deploy given packet.
    Pre-requisites: The packet provided exist
    Test-steps:
      1. Start deploy_cli.py
      2. Use the command `deploy service=frontend`
    Expected-result:
      The CLI tool print correct logs
      The correct package is deployed
    ```

4. Manual testing is time consuming, is it possible to write `unit tests` for parts of the code? Is there any part that are hard to test? why?
5. Start writing unit tests as a team, focus on the most important test cases. Then also take coverage into consideration (you can run `tox`)
6. Everyone should copy the test to their branch, we will use them next lesson.  

## Links

### unittest

* [Read more about unittest methods to use](https://docs.python.org/3.8/library/unittest.html#deprecated-aliases)
* [Read more about vscode and Python testing](https://code.visualstudio.com/docs/python/testing)
* [Plugin that show coverage in vscode](https://marketplace.visualstudio.com/items?itemName=ryanluker.vscode-coverage-gutters)
* [Read more about builtin unittest](https://docs.python.org/3/library/unittest.html)
  
### git

* [Read more about git in vscode](https://code.visualstudio.com/Docs/editor/versioncontrol)
