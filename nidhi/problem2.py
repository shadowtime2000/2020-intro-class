f = open('/share/SARS/SARS-2020.fasta', 'r')
s = f.readlines()
finalstr = ''
for p in range(1, len(s)):
	finalstr = finalstr + s[p].rstrip("\n")
#print(finalstr)
a = []
b = []
c = []
p ={'TTT':'F','TTC':'F','TTA':'F','TTG':'F','CTT':'L','CTC':'L','CTA':'L','CTG':'L','ATT':'I','ATC':'I','ATA':'I','ATG':'M','GTT':'V','GTC':'V','GTA':'V','GTG':'V','TCT':'S','TCC':'S','TCA':'S','TCG':'S','CCT':'P','CCC':'P','CCA':'P','CCG':'P','ACT':'T','ACC':'T','ACA':'T','ACG':'T','GCT':'A','GCC':'A','GCA':'A','GCG':'A','TAT':'Y','TAC':'T','TAA':'','TAG':'','CAT':'H','CAC':'H','CAA':'Q','CAG':'Q','AAT':'N','AAC':'N','AAA':'K','AAG':'K','GAT':'D','GAC':'D','GAA':'E','GAG':'E','TGT':'C','TGC':'C','TGA':'*','TGG':'W','CGT':'R','CGC':'R','CGA':'R','CGG':'R','AGT':'S','AGC':'S','AGA':'R','AGG':'R','GGT':'G','GGC':'G','GGA':'G','GGG':'G'}
for i in range(0, len(finalstr), 3):
	#print(finalstr[i:i+3])
	if ((len(finalstr[i:i+3])) == 3):
		a.append(p[finalstr[i:i+3]])
print (''.join(a))
for i in range(1, len(finalstr), 3):
	if ((len(finalstr[i:i+3]))==3):
		b.append(p[finalstr[i:i+3]])
print (''.join(b))
for i in range(2, len(finalstr), 3):
	if ((len(finalstr[i:i+3]))==3):
		c.append(p[finalstr[i:i+3]])
print (''.join(c))
