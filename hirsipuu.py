from printer import tulosta_naytto, tyhjenna_naytto

def load():
	from parser import arvo_sana
	from random import choice

	return choice(arvo_sana())

def main():
	sana = load()
	arvatut = ''
	voitto = False
	tappio = False
	tulosta_naytto(sana, arvatut)

	while not voitto and not tappio:
		arvaus = input("Arvaa kirjain: ")
		if len(arvaus) > 1 or len(arvaus) == 0:
			tyhjenna_naytto()
			print("Anna yksi kirjain!")
			continue
		if arvaus in arvatut:
			print("Olet jo arvannut tämän kirjaimen!")
			continue
		arvatut += arvaus.lower()
		if arvaus not in sana:
			if len([kirjain for kirjain in arvatut if kirjain not in sana]) > 6:
				tappio = True
		else:
			jatkuu = False
			for kirjain in sana:
				if kirjain not in arvatut:
					jatkuu = True
			if not jatkuu:
				voitto = True
		tulosta_naytto(sana, arvatut)
	print(f"Pelin tulos: {'Voitto' if voitto else 'Tappio'}")
	print(f"Oikea sana oli: {sana}")

if __name__ == "__main__":
	main()
