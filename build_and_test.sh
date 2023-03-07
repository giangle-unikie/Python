#!/bin/bash

# Run tests and export results to report file
pytest --junitxml=test-report.xml

# Exit with status code 0 if tests passed, 1 otherwise
pytest_status=$?
if [ $pytest_status -eq 0 ]
then
  echo "All tests passed! See test-report.xml for details."
  exit 0
else
  echo "Tests failed! See test-report.xml for details."
  exit 1
fi
