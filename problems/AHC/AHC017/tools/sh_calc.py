import subprocess

subprocess.run(['rm', 'tmp_out.txt'])
space = 5
command = [str(i).zfill(4) for i in range(0, 100, space)]
command = ["sh", 'calc_score.sh'] + command
subprocess.run(command)

with open('tmp_out.txt', 'r') as f:
    scores = f.readlines()
    scores = list(map(lambda x:int(x.split()[-1]), scores))
    print("avg:{:,}, max:{:,}({}), min:{:,}({})".format(sum(scores)//len(scores), max(scores), scores.index(max(scores))*space, min(scores), scores.index(min(scores))*space))