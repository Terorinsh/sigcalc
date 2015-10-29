import math

def keks(keks):
	if keks < 0:
		keks = 0
	else:
		keks = keks
	return keks
	
def spacer(x):
	x = str(x)
	if len(x) == 1:
		x = x + "  "
	if len(x) == 2:
		x = x + " "
	else:
		x = x
	return x

summa = 0
x = 0
y = 0

gb_apjoms = 0
ep_skaits = 0
ep_apjoms = 0
db_skaits = 0
paka = '???'
gb_paka = 0
ep_paka = 0
ep_gb_paka = 0
db_paka = 0
naudinas = 0

pak1 = [1,10,50,2,3.50]
pak2 = [2,20,100,2,7.05]
pak3 = [4,30,150,2,11.75]
pakalp = [0,0,0,0,0]

while True:
	
	if paka == "alfa":
		pakalp = pak1
	elif paka == "beta":
		pakalp = pak2
	elif paka == "gamma":
		pakalp = pak3
	
#	if paka == "alfa":
#		gb_paka = 1
#		ep_paka =  10
#		ep_gb_paka = 50
#		db_paka = 2
#		naudinas = 3.50
#	if paka == "beta":
#		gb_paka = 2
#		ep_paka = 20
#		ep_gb_paka = 100
#		db_paka = 4
#		naudinas = 7.05
#	if paka == "gamma":
#		gb_paka = 4
#		ep_paka = 30
#		ep_gb_paka = 150
#		db_paka = 6
#		naudinas = 11.75
		
	gb_cena = float(gb_apjoms) - pakalp[0]
	if gb_cena > 0:
		gb_cena = gb_cena * 0.6
	else:
		gb_cena = 0
		
	ep_cena = float(ep_skaits) - pakalp[1]
	print "-->", ep_cena
	if ep_cena > 0:
		print "-->", ep_cena
		ep_cena = ep_cena * 0.06
		print "-->", ep_cena
	else:
		ep_cena = 0
		print "-->", ep_cena
		
	ep_gb_cena = float(ep_apjoms) - pakalp[2]
	if ep_gb_cena > 0:
		ep_gb_cena = ep_gb_cena * 0.082
	else:
		ep_gb_cena = 0
		
	db_cena = float(db_skaits) - pakalp[3]
	if db_cena > 0:
		db_cena = db_cena * 1.7
	else:
		db_cena = 0
		
	summa = gb_cena + ep_cena + ep_gb_cena + db_cena + pakalp[4]
	summa_pvn = (float(summa) * 0.21) + float(summa)
	try:
		ep_gb = float(ep_apjoms) / float(ep_skaits)
	except:
		ep_gb = 0
# Drukajam!!!
	print "\n\n\n---------------------------------"
	print "1) Apjoms lapai  :", spacer(gb_apjoms),"Eur:", gb_cena
	print "2) E-pastu skaits:", spacer(ep_skaits),"Eur:", ep_cena
	print "3) E-pastu gb/kop:", spacer(ep_apjoms),"Eur:", ep_gb_cena, "GB/GAB", ep_gb
	print "4) Datu Bazes    :", spacer(db_skaits),"Eur:", db_cena
	print "---------------------------------"
	print "   Bazes paka    :", paka
	print "---------------------------------"
	print "   Summa EUR :",summa,"Ar PVN:", summa_pvn
	print "---------------------------------"
	ieksa = raw_input(">_")
	try:
		if ieksa == "quit" or ieksa == "exit":
			break
		elif ieksa == "alfa":
			paka = ieksa
		elif ieksa == "beta":
			paka = ieksa
		elif ieksa == "gamma":
			paka = ieksa
		elif ieksa == "print":
			print "gb_apjoms", gb_apjoms
			print "ep_skaits", ep_skaits
			print "ep_apjoms", ep_apjoms 
			print "db_skaits", db_skaits 
			print "paka", paka 
			print "gb_paka", gb_paka 
			print "ep_paka", ep_paka
			print "ep_gb_paka", ep_gb_paka
			print "db_paka", db_paka
			print "summa", summa
		else:
			x = int(ieksa[:1])
			y = int(ieksa[1:])
			if x == 1:
				gb_apjoms = y
			elif x == 2:
				ep_skaits = y
			elif x == 3:
				ep_apjoms = y
			elif x == 4:
				db_skaits = y
	except:
		print " "
		print "----------------------------------------------------"
		print "ERROR:"
		print "----------------------------------------------------"
		print "ievadiet pakalpojuma kodu, atstarpi, jauno skaitli."
		print "Piemeram: >_2 40"
		print "----------------------------------------------------"
		print "Papild komandas:"
		print "alfa, beta, gamma, exit, quit"
		print "----------------------------------------------------"
		raw_input("Spiediet Enter to lai turpinatu")
		
	
print "Uzredzi!"
	
