#!/bin/bash

# Run tests and generate coverage report
pytest --cov --cov-report=html

# Exit with status code 0 if tests passed, 1 otherwise
pytest_status=$?
if [ $pytest_status -eq 0 ]
then
  echo "All tests passed! See test coverage html file in folder htmlcov for details."
  exit 0
else
  echo "Tests failed! See test coverage html file in folder htmlcov for details."
  exit 1
fi
