echo "ARCのコンテスト番号を入力してください"
read contest_num
cd problems/ARC
mkdir ARC${contest_num}
cd ARC${contest_num}
for diff in a b c d e f
do
    touch arc${contest_num}_${diff}.py
done