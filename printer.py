import os

def tyhjenna_naytto():
	for i in range(os.get_terminal_size().lines):
		print("\n")

def tulosta_naytto(sana, arvatut):
	v = len([kirjain for kirjain in arvatut if kirjain not in sana])
	for i in range(os.get_terminal_size().lines):
		if i == 1:
			if v > 2:
				print(" ====")
			else:
				print("")
		if i == 2:
			if v > 3:
				print(" |  |")
			elif v > 1:
				print(" |")
			else:
				print("")
		if i == 3:
			if v > 4:
				print(" |  O")
			elif v > 1:
				print(" |")
			else:
				print("")
		if i == 4:
			if v > 5:
				print(" |  T")
			elif v > 1:
				print(" |")
			else:
				print("")
		if i == 5:
			if v > 6:
				print(" |  A")
			elif v > 1:
				print(" |")
			else:
				print("")
		if i == 6:
			if v > 1:
				print(" |")
			else:
				print("")
		if i == 7:
			if v > 0:
				print(" =====")
			else:
				print("")
		if i == 8:
			if v > 0:
				print(" |    |")
			else:
				print("")
		if i in [0,9,10]:
			print("")
		if i == 11:
			tuloste = ''
			for k in sana:
				if k in arvatut:
					tuloste += k
				else:
					tuloste += '*'
			print(tuloste)
		if i == 12:
			print('-'*len(sana))
		if i > 12:
			print("")
