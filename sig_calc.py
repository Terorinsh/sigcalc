# funkcijas minimala apjoma palielinasanai lidz 5 un 10.
#aprekina pedejo skaitli
def ped(x):
	ga = len(str(x))
	ped = int(str(x)[ga-1])
	return ped

# palielina lidz demsitiem
def ped0(x):
	while True:
		if ped(x) != 0:
			x = int(x) + 1
		else:
			x = int(x)
			break
	return x
	
# palielina lidz pieciem
def ped05(x):
	while True:
		if ped(x) == 0 or ped(x) == 5:
			x = int(x)
			break
		else:
			x = int(x) + 1
			
	return x
	
# Definejam speiseri... ieliek atstarpes formatejot
def spcr(x):
	x = str(x)
	if len(x) == 1:
		x = x + "  "
	if len(x) == 2:
		x = x + " "
	else:
		x = x
	return x
# Veicam summas aprekinu. 
# atnemam bazes pakas apjomu 
# un reizinam atlikuso ar cenu
def aprekins(x,y,c):
	cc = float(x) - float(y)
	if cc > 0:
		cc = cc * c
	else:
		cc = 0
	return cc
# pvn kalkulators
def pvn(x):
	x = (float(x) * 0.21) + x
	return x

def help():
	print "\n\n\n\n\n\n\n" 
	print "--------------Nepareiza ievade---------------"
	print "ievadiet pakalpojuma kodu, un skaitu:"
	print "Piemeram: >_2 40"
	print "---------------------------------------------"
def komandas():
	print "----------------=paku kodi=------------------"
	print "----alfa--beta--gamma--paka4--paka5--paka6 --"
	print "----3.50--7.05--11.75--14.10--17.60--24.70---"
	print "---------------------------------------------"
	print "---exit----------help----cits---------quit---"
	print "---------------------------------------------"
	
# definejam mainigos
summa = 0
x = 0
y = 0
ix1 = 0
ix2 = 0
ix3 = 0
ix4 = 0
paka = '--nav noradits--'
pakalp = [0,0,0,0,0]

# pakalpojumu apjomi un pakas cena
pak1 = [1,10,50,2,3.50]
pak2 = [2,20,100,4,7.05]
pak3 = [4,30,150,6,11.75]
pak4 = [10,30,150,6,14.10]
pak5 = [20,30,150,10,17.60]
pak6 = [20,50,250,10,24.70]
# pakalpojumu cenas gab
cen = [0.6,0.06,0.082,1.7]

while True:
	# Rekinam cenas un summu
	ex1 = aprekins(ix1,pakalp[0],cen[0])
	ex2 = aprekins(ix2,pakalp[1],cen[1])
	ex3 = aprekins(ix3,pakalp[2],cen[2])
	ex4 = aprekins(ix4,pakalp[3],cen[3])
	summa = ex1 + ex2 + ex3 + ex4 + pakalp[4]
	
	# rekinam e-pastu lielumus, 
	# try - except jo bija errors... nez kapec
	try:
		ep_gb = float(ix3) / float(ix2)
	except:
		ep_gb = 0
	ep_gb = "gb gabalaa: " + str(ep_gb)
		
	vel_gb = ix2 * 5
	vel_gb = "velamie gb: " + str(vel_gb)
	
	# Drukaajam UI!
	print "\n\n\n\n\n\n\n" 
	komandas()
	print "\n\n\n\n\n\n\n" 
	print "---------------------------------------------"
	print "1) Apjoms lapai   gb :", spcr(ix1),"Eur:", ex1
	print "2) E-pastu skaits gab:", spcr(ix2),"Eur:", ex2, vel_gb
	print "3) E-pastu gb/kop gb :", spcr(ix3),"Eur:", ex3, ep_gb
	print "4) Datu Bazes     gab:", spcr(ix4),"Eur:", ex4
	print "---------------------------------------------"
	print "   Bazes paka    :", paka
	print "---------------------------------------------"
	print "   Summa EUR :",summa,"Ar PVN:", pvn(summa)
	print "---------------------------------------------"
	
	# ievade
	ieksa = raw_input("kods skaits >_")
	
	# Sagremojam komandu
	try:
		if ieksa == "quit" or ieksa == "exit":
			break
		elif ieksa == "alfa":
			pakalp = pak1
			paka = ieksa
		elif ieksa == "beta":
			pakalp = pak2
			paka = ieksa
		elif ieksa == "gamma":
			pakalp = pak3
			paka = ieksa
		elif ieksa == "paka4":
			paka = ieksa
			pakalp = pak4
		elif ieksa == "paka5":
			paka = ieksa
			pakalp = pak5
		elif ieksa == "paka6":
			paka = ieksa
			pakalp = pak6
		elif ieksa == "help":
			help()
			komandas()
			raw_input("Spiediet Enter to lai turpinatu")
		else:
			x = int(ieksa[:1])
			y = int(ieksa[1:])
			if x == 1:
				ix1 = y
			elif x == 2:
				ix2 = ped0(y)
			elif x == 3:
				ix3 = ped05(y)
			elif x == 4:
				ix4 = y
				
	# Drukajam Error!
	except:
		help()
		komandas()
		raw_input("Spiediet Enter to lai turpinatu")
		
	
print "  -- Uzredzi! --  "
	
