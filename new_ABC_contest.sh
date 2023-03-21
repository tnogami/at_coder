echo "ABCのコンテスト番号を入力してください"
read contest_num
cd problems/ABC
mkdir ABC${contest_num}
cd ABC${contest_num}
for diff in a b c d e f g
do
    touch abc${contest_num}_${diff}.py
done