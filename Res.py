import sys
import copy

fa_file = sys.argv[1]
isd_file = sys.argv[2]
filt_file = sys.argv[3]
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

f_in = open(fa_file, 'r')
f_isd = open(isd_file, 'r')
f_out = open(filt_file, 'w')



fa = {
'seq': '',
'tissue': '',
'id': '',
'i': ''
}
isd = {
'prot':'',
'id':'',
'tissue':''
}

fa_d = {}
isd_d = {}
synt_isd_d = {}
cur_isd = copy.copy(isd)
for line in f_isd:

	cur_isd['prot'] = line[:-1].split('\t')[0]
	cur_isd['id'] = line[:-1].split('\t')[1]
	cur_isd['tissue'] = line[:-1].split('\t')[2]
	isd_d[cur_isd['id']] = copy.copy(cur_isd)


cur_fa = copy.copy(fa)
for line in f_in:

	if (('>' in line) == True):
		cur_fa['tissue'] = line[1:-1].split('|')[0]
		cur_fa['id'] = line[1:-1].split('|')[1]
		cur_fa['i'] = int(line[1:-1].split('|')[2])
	else:
		cur_fa['seq'] = line[:-1]
		if (fa_d.has_key(cur_fa['id']) == False):
			fa_d[cur_fa['id']] = {}
		fa_d[cur_fa['id']][cur_fa['i']] = copy.copy(cur_fa)

#print fa_d.keys()

for idd in fa_d.keys():
	cur_isd = copy.copy(isd)
	iis = sorted(fa_d[idd].keys())
	for i in iis:
		cur_isd['prot'] = cur_isd['prot'] + fa_d[idd][i]['seq']
		cur_isd['id'] = idd
		cur_isd['tissue'] = fa_d[idd][i]['tissue']
	synt_isd_d[cur_isd['id']] = copy.copy(cur_isd)
#	print len(synt_isd_d[cur_isd['id']]['prot'])


for idd in synt_isd_d.keys():
	coding_dna = Seq(synt_isd_d[idd]['prot'], generic_dna)
	#print len(coding_dna.translate())
	if (coding_dna.translate() == isd_d[idd]['prot']):
		f_out.write('>' + idd + '|' + synt_isd_d[idd]['tissue'] + '\n')
		f_out.write(synt_isd_d[idd]['prot'] + '\n')


f_in.close()
f_isd.close()
f_out.close()



