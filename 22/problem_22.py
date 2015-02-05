#!/usr/bin/env python
# encoding: utf-8
"""
problem_22.py

Created by James Jones on 2015-02-04.

Problem 22 from https://projecteuler.net/problem=22

Description:

Using names.txt, a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

Sample Output: 

	871198282

Reason for picking problem: I have a secret love for data processing.

References: 

Time took: 30 hours

"""
names = []

		
def loadNames():
	global names
	#open file
	f = open("names.txt",'r')
	#split each name off and remove quotes
	for x in f:
		for y in x.split(","):
			y = y.replace('"','')
			names.append(y)
	names.sort()

def main():
	loadNames()
	
	#totol vlaue
	tv = 0
	
	#using enumerate to index number and value
	for i,v in enumerate(names):
		#setting place value
		pv = i + 1
		
		#initializing name value
		nv = 0
		
		#converting name to list for easier calculating
		name = list(v)
		for x in name:
			nv += ord(x) - 64
		
		tv += nv * pv

	print tv
	
if __name__ == '__main__':
	main()

