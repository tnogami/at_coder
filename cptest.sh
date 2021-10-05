problem_name=$1
problem_path=$2
test_dir=test/${problem_name}
base_url=${problem_name%_*}

# make test directory
if [ ! -e ${test_dir} ]; then
    oj dl -d test/${problem_name} https://atcoder.jp/contests/${base_url}/tasks/${problem_name}
fi

oj test -c "python3 ${problem_path}/${problem_name}.py" -d test/${problem_name}