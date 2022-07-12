import os

def tyhjenna_naytto():
	for i in range(os.get_terminal_size().lines - 16):
		print("\n")

def tulosta_naytto(sana, arvatut, vaarat):
	for i in range(os.get_terminal_size().lines - 16):
		v = vaarat
		i = int(i)
		if i == 1:
			if v > 2:
				print(" ====")
			else:
				print("\n")
		if i == 2:
			if v > 3:
				print(" |  |")
			elif v > 1:
				print(" |")
			else:
				print("\n")
		if i == 3:
			if v > 4:
				print(" |  O")
			elif v > 1:
				print(" |")
			else:
				print("\n")
		if i == 4:
			if v > 5:
				print(" |  T")
			elif v > 1:
				print(" |")
			else:
				print("\n")
		if i == 5:
			if v > 6:
				print(" |  A")
			elif v > 1:
				print(" |")
			else:
				print("\n")
		if i == 6:
			if v > 1:
				print(" |")
			else:
				print("\n")
		if i == 7:
			if v > 0:
				print(" =====")
			else:
				print("\n")
		if i == 8:
			if v > 0:
				print(" |    |")
			else:
				print("\n")
		if i == 9 or i == 10:
			print("\n")
		if i == 11:
			tuloste = ''
			for k in sana:
				if k in arvatut:
					tuloste += k
				else:
					tuloste += '*'
			print(tuloste)
		if i == 12:
			for _ in range(len(sana)):
				print('-', end='')
		if i > 12:
			print("\n")
