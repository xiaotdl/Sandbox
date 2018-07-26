echo "============================"
echo "Running a code-coverage start task..."
python test/schedule_code_coverage_task.py 10.192.10.243 start
rc=$?; if [[ $rc != 0 ]]; then exit $rc; fi

echo "============================"
echo "Running a code-coverage end task..."
python test/schedule_code_coverage_task.py 10.192.10.243 end
rc=$?; if [[ $rc != 0 ]]; then exit $rc; fi
