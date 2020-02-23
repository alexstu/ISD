import sys
import subprocess

bg_file = sys.argv[1]
filt_file = sys.argv[2]

f_in = open(bg_file, 'r')
f_out = open(filt_file, 'a')

for line in f_in:
	chrr = line[:-1].split('\t')[0]
	start = int(line[:-1].split()[1])
	end = int(line[:-1].split()[2])

	if((end-start) >= 84):
		f_out.write(chrr + '\t' + str(start) + '\t' + str(end) + '\n')

f_in.close()
f_out.close()



