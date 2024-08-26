---

# 0x03. Unittests and Integration Tests

## Overview

This project focuses on unit testing and integration testing within a Python environment. The main goal is to ensure that individual functions work as expected and that the system as a whole performs correctly when components interact. 

### Key Concepts

- **Unit Testing**: Testing individual functions or methods to ensure they produce the expected results. The aim is to validate the logic within the tested function, using mock objects to isolate the function from external dependencies such as network or database calls.

- **Integration Testing**: Testing the interactions between different parts of the application to ensure that they work together as intended. This involves checking end-to-end functionality and typically involves less mocking compared to unit tests.

## Testing

### Execute Tests

Run your tests using:
```sh
$ python -m unittest path/to/test_file.py
```

### Resources

- [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)
- [unittest.mock — mock object library](https://docs.python.org/3/library/unittest.mock.html)
- [How to mock a readonly property with mock?](https://docs.python.org/3/library/unittest.mock.html#mock-objects)
- [parameterized](https://parameterized.readthedocs.io/en/latest/)

## Learning Objectives

By the end of this project, you should be able to:

- Differentiate between unit and integration tests.
- Understand common testing patterns such as mocking, parameterization, and fixtures.

## Requirements

- Files should be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- All files must end with a new line.
- The first line of all files should be `#!/usr/bin/env python3`.
- Include a `README.md` file at the root of the project folder.
- Adhere to PEP 8 style guidelines using `pycodestyle` version 2.5.
- All files must be executable.
- Modules, classes, and functions should have proper documentation.
- Use type annotations for all functions and coroutines.

## Required Files

- `utils.py`
- `client.py`
- `fixtures.py`

## Tasks

1. **Parameterize a Unit Test**
   - Implement tests for `utils.access_nested_map` using `@parameterized.expand`.
   - Validate that the function returns expected results for given inputs.

2. **Parameterize a Unit Test with Exceptions**
   - Implement tests for exceptions in `utils.access_nested_map`.
   - Ensure `KeyError` is raised for invalid paths and verify exception messages.

3. **Mock HTTP Calls**
   - Test `utils.get_json` by mocking `requests.get`.
   - Ensure that `get_json` returns the expected payloads and verifies that `requests.get` is called correctly.

4. **Parameterize and Patch**
   - Test memoization with a decorator using `@mock.patch`.
   - Verify that a method is called only once despite multiple calls to a memoized property.

5. **Mocking a Property**
   - Test the `_public_repos_url` property of `GithubOrgClient`.
   - Ensure the property returns the expected result based on mocked data.

6. **More Patching**
   - Test `GithubOrgClient.public_repos` with mocked `get_json` and `_public_repos_url`.
   - Ensure correct results are returned and all mocks are called as expected.

7. **Parameterize**
   - Test `GithubOrgClient.has_license` with various inputs.
   - Validate the method’s response for different licenses.

8. **Integration Test: Fixtures**
   - Implement integration tests for `GithubOrgClient.public_repos` using fixtures.
   - Mock `requests.get` and verify the method’s behavior with fixture data.

9. **Advanced Integration Tests**
   - Test `GithubOrgClient.public_repos` and `public_repos` with specific licenses.
   - Ensure results match expected values from fixtures.
