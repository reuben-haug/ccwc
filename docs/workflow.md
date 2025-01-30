# Template Workflow Guide

## Table of Contents
1. [Overview](#overview)
2. [Workflow Steps](#workflow-steps)
  1. [Define Done](#define-done)
  2. [Create Feature Descriptions](#create-feature-descriptions)
  3. [Create Step Definitions](#create-step-definitions)
  4. [Run Initial Tests](#run-initial-tests)
  5. [Implement Solution](#implement-solution)
  6. [Documentation](#documentation)
3. [Committing Changes](#committing-changes)
4. [Dependency Managements](#dependency-managements)
5. [Available Make Commands](#available-make-commands)
6. [Directory Structure](#directory-structure)
7. [Best Practices](#best-practices)

## Overview
This guide explains the workflow for test-driven development. This guide assumes you have already cloned and configured the template.

## Workflow Steps

1. **Define Done**
  - Define the project requirements and acceptance criteria.  Use the [docs/overview.rst](/docs/overview.rst) file to document the project requirements.
  - Update the [docs/README.md](/docs/README.md) file with the project overview and requirements, as well as to keep todo notes and other information.  You can also replace the template README file in the root directory with your project README.

2. **Create Feature Descriptions**
   - Create a `tests/features/<project_name>.feature` file
   - Write test scenarios with Gherkin. For example:
     ```gherkin
     Feature: <project_name>
         Scenario: Basic Test Case
             Given the input "example"
             When I run the program
             Then I should see "expected output"
     ```

3. **Create Step Definitions**
   - Create a `tests/steps/<project_name>.py` file
   - Write step definitions for each scenario. For example:
     ```python
     from behave import given, when, then

     @given('the input "{input_text}"')
     def step_implement(context, input_text):
         context.input_text = input_text
     
     @when('I run the program')
     def step_impl(context):
         # Add implementation
         pass

     @then('I should see "{expected}"')
     def step_impl(context, expected):
         assert context.input_text == expected
     ```

4. **Run Initial Tests**
   - Run behave to see the failing tests:
     ```bash
     behave tests/features/<project_name>.feature
     ```

5. **Implement Solution**
   - Create solution in `src/<project_name>.py`
   - Run tests frequently:
     ```bash
     make test  # Runs both pytest and behave tests
     ```

6. **Documentation**
   - Update documentation in the `src/docs/index.rst` file
   - Build docs:
     ```bash
     make docs
     ```
## Committing Changes

1. **Run Tests**
  - Ensure all tests pass before committing:
    ```bash
    make test
    ```
2. **Format Code**
  - Format code with black and isort:
    ```bash
    make format
    ```
3. **Lint Code**
  - Run linting checks:
    ```bash
    make lint
    ```
4. **Commit Changes**
  - Add and commit changes:
    ```bash
    git add .
    git commit -m "Commit_message"
    ```

## Dependency Managements
Use the following 'make' commands:
- `make deps-compile` - Generates requirements.txt and requirements-dev.txt from pyproject.toml.
- `make deps-sync` - Sync the environment with the generated requirements files.
- `make deps-update` - Update the dependencies in to their latest versions and regenerate the requirements files.

## Available Make Commands
- `make test` - Run all tests
- `make format` - Format code with black and isort
- `make lint` - Run linting checks
- `make docs` - Build documentation
- `make clean` - Clean build artifacts

## Directory Structure
```text
|-- src/    # Source code
|-- tests/  # Behave and pytest files
    |-- steps/     # Step definitions
    |-- environment.py  # Behave environment setup
|-- docs/   # Documentation and project README.
|-- README.md   # Template README.
```

## Best Practices
- Write feature files first
- Keep scenarios focused and specific
- Use clear, descriptive step definitions
- Run tests frequently
- Document as you go