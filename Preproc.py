import itertools

tissue='Liver'
X1=['N','T']
X2=['EE','DQ']
X3=['FFL','WFV']
X4=['F','I']
X5=['V','T']
A1 = ['NRRGLDLL']
A2=['A']
A3 = ['GGLC']
A4=['EEECC']
A5 = ['Y']
A6=['NQT']
pp = list(itertools.product(A1,X1,A2,X2,A3,X3,A4,X4,A5,X5,A6))
f = open('ISD.txt', 'w')
for p in pp:
	f.write(''.join(p) + '\t' + 'id' + '\t' + tissue + '\n')
f.close()
tissue='Kidney'
X1=['A','V']
X2=['AE','FD']
X3=['V','L']
X4=['F','V']
X5=['I','L','F']
X6=['QVV','TVY']
X7=['V','A']
X8=['D','E']
A1 = ['NRL']
A2=['LDYLLA']
A3 = ['GG']
A4=['CGK']
A5 = ['NLTNCCLQ']
A6=['DDQG']
A7=['ENI']
A8=['R']
A9=['M']
pp = list(itertools.product(A1,X1,A2,X2,A3,X3,A4,X4,A5,X5,A6,X6,A7,X7,A8,X8,A9))
f = open('ISD.txt', 'a')
for p in pp:
	f.write(''.join(p) + '\t' + 'id' + '\t' + tissue + '\n')
f.close()
tissue='Lung'
X1=['R','W']
X2=['G','V']
X3=['AET','TEK']
X4=['L','T']
X5=['F','Y','N','Q']
X6=['E','Q']
X7=['V','F']
X8=['Q','E','T']
A1 = ['N']
A2=['R']
A3 = ['LDLLT']
A4=['GG']
A5 = ['CI']
A6=['L']
A7=['EECCFC']
A8=['N']
A9=['S']
pp = list(itertools.product(A1,X1,A2,X2,A3,X3,A4,X4,A5,X5,A6,X6,A7,X7,A8,X8,A9))
f = open('ISD.txt', 'a')
for p in pp:
	f.write(''.join(p) + '\t' + 'id' + '\t' + tissue + '\n')
f.close()



tissue='Brain'
X1=['W','R']
X2=['KA','RG']
X3=['N','D']
X4=['RS','TG']
X5=['T','L']
X6=['L','I']
X7=['G','E','D']
X8=['YF','FD']
X9=['T','S']
A1 = ['N']
A2=['L']
A3 = ['LLTAE']
A4=['G']
A5 = ['C']
A6=['FL']
A7=['EECC']
A8=['HNQ']
pp = list(itertools.product(A1,X1,X2,A2,X3,A3,X4,A4,X5,A5,X6,A6,X7,A7,X8,A8,X9))
f = open('ISD.txt', 'a')
for p in pp:
	f.write(''.join(p) + '\t' + 'id' + '\t' + tissue + '\n')
f.close()





tissue='Thalamus'
X1=['N','D']
X2=['R','T']
X3=['G','E','D']
X4=['T','S']
A1 = ['NRRGL']
A2=['LLTAE']
A3 = ['GGLCIFL']
A4=['EECCFDHNQ']
pp = list(itertools.product(A1,X1,A2,X2,A3,X3,A4,X4))
f = open('ISD.txt', 'a')
for p in pp:
	f.write(''.join(p) + '\t' + 'id' + '\t' + tissue + '\n')
f.close()




tissue='Eye'
X1=['W','R']
X2=['E','T']
X3=['Q','K']
X4=['F','A']
X5=['Y','T','Q']
X6=['Q','T','N']
A1 = ['N']
A2=['RAL']
A3 = ['LLTAE']
A4=['GGTCL']
A5 = ['LQEECC']
A6=['YLN']
A7=['S']
pp = list(itertools.product(A1,X1,A2,X2,A3,X3,A4,X4,A5,X5,A6,X6,A7))
f = open('ISD.txt', 'a')
for p in pp:
	f.write(''.join(p) + '\t' + 'id' + '\t' + tissue + '\n')
f.close()






tissue='Colon'
X1=['R','H']
X2=['L','F']
X3=['GL','VE']
X4=['L','F','I']
X5=['E','D']
A1 = ['N']
A2=['RG']
A3 = ['DLLTAEKG']
A4=['CIF']
A5 = ['N']
A6=['ECCFYLNQS']
pp = list(itertools.product(A1,X1,A2,X2,A3,X3,A4,X4,A5,X5,A6))
f = open('ISD.txt', 'a')
for p in pp:
	f.write(''.join(p) + '\t' + 'id' + '\t' + tissue + '\n')
f.close()




tissue='Skin'
X1=['R','H']
X2=['L','W','F']
X3=['G','V']
X4=['I','L']
X5=['LE','SD']
X6=['F','G','P']
X7=['A','V']
A1 = ['NR']
A2=['G']
A3 = ['DLLTAETG']
A4=['LC']
A5 = ['F']
A6=['EECC']
A7=['D']
A8=['NQS']
pp = list(itertools.product(A1,X1,A2,X2,A3,X3,A4,X4,A5,X5,A6,X6,A7,X7,A8))
f = open('ISD.txt', 'a')
for p in pp:
	f.write(''.join(p) + '\t' + 'id' + '\t' + tissue + '\n')
f.close()






tissue='Testis'
X1=['N','T','A']
X2=['E','T']
X3=['L','I','F']
X4=['Y','D']
X5=['Q','H','K']
X6=['T','S']
A1 = ['NRRGLDLL']
A2=['AE']
A3 = ['GGLC']
A4=['FLEEYCCF']
A5 = ['PN']
pp = list(itertools.product(A1,X1,A2,X2,A3,X3,A4,X4,A5,X5,X6))
f = open('ISD.txt', 'a')
for p in pp:
	f.write(''.join(p) + '\t' + 'id' + '\t' + tissue + '\n')
f.close()




tissue='Cervix'
X1=['L','G']
X2=['Q','Y']
X3=['L','I','F']
X4=['FS','PQ']
X5=['Y','T']
A1 = ['NRRG']
A2=['DLL']
A3 = ['FETGGLC']
A4=['FLEEECC']
A5 = ['VN']
A6=['S']
pp = list(itertools.product(A1,X1,A2,X2,A3,X3,A4,X4,A5,X5,A6))
f = open('ISD.txt', 'a')
for p in pp:
	f.write(''.join(p) + '\t' + 'id' + '\t' + tissue + '\n')
f.close()




tissue='Prostate'
X1=['E','D']
X2=['G','W']
X3=['L','Y']
A1 = ['NHRGLELLTV']
A2=['KR']
A3 = ['LCIFLNEECCAT']
A4=['NQS']
pp = list(itertools.product(A1,X1,A2,X2,A3,X3,A4))
f = open('ISD.txt', 'a')
for p in pp:
	f.write(''.join(p) + '\t' + 'id' + '\t' + tissue + '\n')
f.close()






tissue='Bladder'
X1=['AF','ED']
X2=['L','I','F']
X3=['D','E','Y']
X4=['F','V']
A1 = ['NRQGLDLLN']
A2=['TGPLC']
A3 = ['FLEDECCL']
A4=['NQT']
pp = list(itertools.product(A1,X1,A2,X2,A3,X3,X4,A4))
f = open('ISD.txt', 'a')
for p in pp:
	f.write(''.join(p) + '\t' + 'id' + '\t' + tissue + '\n')
f.close()




tissue='Adipose'
X1=['DNL','ENA']
X2=['GL','FN']
X3=['E','N']
X4=['V','F','G']
X1=['L','G']
X2=['Q','Y']
X3=['L','I','F']
X4=['FS','PQ']
X5=['Y','T']
A1 = ['NHRGL']
A2=['TAETG']
A3 = ['CIFL']
A4=['DQCCWD']
A5 = ['NQS']
pp = list(itertools.product(A1,X1,A2,X2,A3,X3,A4,X4,A5))
f = open('ISD.txt', 'a')
for p in pp:
	f.write(''.join(p) + '\t' + 'id' + '\t' + tissue + '\n')
f.close()



tissue='Stemcells'
X1=['LA','RF']
X2=['V','L']
X3=['IDD','LDE']
X4=['K','H']
X5=['EI','DL']
A1 = ['YQNR']
A2=['LDYLLAEEGA']
A3 = ['CGKFNISNCCLN']
A4=['NG']
A5 = ['AVL']
A5 = ['ASNI']
pp = list(itertools.product(A1,X1,A2,X2,A3,X3,A4,X4,A5,X5,A6))
f = open('ISD.txt', 'a')
for p in pp:
	f.write(''.join(p) + '\t' + 'id' + '\t' + tissue + '\n')
f.close()











