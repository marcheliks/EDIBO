#!/usr/bin/python3.6

print("Ievadiet skaitli")
# a=2**2000000

#te ir trīs darbības - vertības sagadīšana,
# vērtības pārveidošanas piešķiršinas
#argument = input()
#int(arguments)
#a = int(arguments)

#pildot int(input()) "bez izmeiģinājuma" programma var vienkārši izlidot...
# tāpēc, lai "nelidotu" mēs izmantosim try ... except .. finally konstruktoru
paziime = False
while not paziime:
#while paziiime == False:
#while paziime !== True:
	try:
		a= int( input() )
		paziime = True
	except:
		print("Diemžēl, cienijamais lietotāj, to, kas ievadīts nevar",\
		"pārveidot par vesela tipa skaitli")
		print("lūidzu, ievadiet s_k_a_i_t_l_i vēlreiz")
#if (a == int): print("a**100")
if (a ==5):
	print(a ** 100)
	print("Apreiķins ir gatavs")
print("Šis teksts atrodas ārpus darbību bloka - pierakstīts",\
		"atstarpēs priekšā, tāpēc tas paradīsies jebkurā darumā")
#print ("Atstarpes šeit vairs nedrīkst būt")
