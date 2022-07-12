#!/bin/python3

import xml.etree.ElementTree as ET

ALPHAS = 'abcdefghijklmnopqrstuvwxyzåäABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ'


def evaluate(text):
	for c in text:
		if not c in ALPHAS:
			return False
	return True

def parser(filename="kotus-sanalista_v1.xml"):
	tree = ET.parse(filename)
	root = tree.getroot()
	for cur in root:
		text = cur[0].text
		if evaluate(text):
			yield text

def arvo_sana():
	return [p for p in parser()]

def main():
	for i in parser():
		print(i)

if __name__ == "__main__":
	main()
