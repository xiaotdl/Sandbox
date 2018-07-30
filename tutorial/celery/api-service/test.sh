#!/bin/bash

echo "============================"
echo "Running a simple add task..."
python test/schedule_test_task.py
rc=$?; if [[ $rc != 0 ]]; then exit $rc; fi

echo "============================"
echo "Running a simple code-coverage task..."
python test/schedule_code_coverage_task.py 10.192.10.243 check
rc=$?; if [[ $rc != 0 ]]; then exit $rc; fi
