problem_name=$1
problem_path=$2
which_python=$3
test_dir=test/${problem_name}
base_url=${problem_name%_*}

# make test directory
if [ ! -e ${test_dir} ]; then
    oj dl -d test/${problem_name} https://atcoder.jp/contests/${base_url}/tasks/${problem_name}
fi

echo ${which_python}
echo pypy3

if [${which_python} == "python3"] ; then
    oj test -c "python3 ${problem_path}/${problem_name}.py" -d test/${problem_name}
elif [${which_python} == pypy3] ; then
    oj test -c "pypy3 ${problem_path}/${problem_name}.py" -d test/${problem_name}
else
    echo None
fi