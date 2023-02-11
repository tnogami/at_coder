args1=$@
for a1 in ${args1[@]};do
    python main.py < in/${a1}.txt > out.txt
    cargo run --release --bin vis in/${a1}.txt out.txt >> tmp_out.txt
done