#!/bin/bash

# coverage run -a <file>            Calculate coverage for a single file
# coverage report                   Show coverage report
# coverage html                     Generate HTML report

# Remove previous coverage data
# to avoid problems with missing source files
echo "coverage erase"
coverage erase

# Run coverage for all test files
for file in $(find ./test -type f -name "test_*.py" -not -path "*/__pycache__/*")
do
    echo "coverage run -a $file"
    coverage run -a $file
done

# Generate coverage report
echo "coverage report"
coverage report

# Generate HTML report
echo "coverage html"
coverage html
