print("Analyse les plaques d'Europe")
nbrPlaque=26*26*26*26*999
print("nombre de plaque %d" % nbrPlaque)
print("affichage de la plaque mediane")
mediane=nbrPlaque/2
print(mediane)
 #228 488 000
 #676 676 999

def z(x):
 return chr((x/26)+65) + chr((x%26)+65)

def s(x):
 m=(x%999)+1
 d=(x/999)%676
 g=(x/999/676)%676
 return (z(g),m,z(d))

def o(d):
 return ((ord(d[0])-65)*26) + (ord(d[1])-65)

def t(x):
 (g,m,d) = x.split(":")
 print("g=%s;d=%s" %(g,d))
 d=o(d)
 g=o(g)
 m=int(m)-1 
 return m+(999*d)+(999*676*g)
 
for a in xrange(mediane/2/2/2, mediane/2/2/2+999):
 print(("%s:%03d:%s->" % s(a)) + str(a))

print("NA:010:AA->%d" % (t("NA:010:AA")))

