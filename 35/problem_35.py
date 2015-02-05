#!/usr/bin/env python
# encoding: utf-8
"""
problem_35.py

Created by James Jones on 2015-02-04.

Problem 35 from https://projecteuler.net/problem=35

Description:

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

Sample Output: 

	testing  999931
	testing  999953
	testing  999959
	testing  999979
	Total circular primes found 55 [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 311, 197, 971, 719, 199, 991, 919, 337, 373, 733, 1193, 1931, 9311, 3119, 3779, 7793, 7937, 9377, 11939, 19391, 93911, 39119, 91193, 19937, 99371, 93719, 37199, 71993, 193939, 939391, 393919, 939193, 391939, 919393, 199933, 999331, 993319, 933199, 331999, 319993]


Reason for picking problem: I thought it would be intresting

References: https://docs.python.org/2/library/math.html

Time took: 3 hours (wanted to make sure my functions were optimized)


"""
import math

#Simple Prime number detector Number
def isPrime(n):
	for x in range(2,int(math.floor(math.sqrt(n)))):
		if n % x == 0:
			return False
	return True

#Function for geting the amount of digits in a int.
def digits(n):
	if n == 0:
		#0 is only 1 digit long
	    return 1
	else:
		#using log10 since we counting in base 10
	    return int(math.log10(abs(n)))+1
	

#get Circulars of number	
def getCirculars(n):
	if digits(n) != 1:
		num = list(str(n))
		circulars = []
		#don't need to do the first on since we already have it. Keep popping the top number until you have gone through all the digits
		x = 1
		while x < digits(n):
			num.append(num.pop(0))
			r = int("".join(num))
			#if the new rotation is same as the original there are no possible rotations
			if r == n:
				return []
			circulars.append(r)
			x += 1

		return circulars
	
	return []
		
			
	
	
def main():
	#adding the circular primes we already know.
	circularPrimes = [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79,97]
	#Since the circular primes we already are below 100 and we don't want numbers with 0's starting at 111
	for x in range(111,1000000):
		#check if it has already been calculated
		if x not in circularPrimes:
			#if there is 0,2,4,6,8 in the number full rotation won't work since one of the numbers in rotation will be even
			curX=list(str(x))
			if "0" not in curX and "2" not in curX and "4" not in curX and "6" not in curX and "8" not in curX:
				if isPrime(x):
					print "testing ",x
					#get Circulars if prime	
					c = getCirculars(x)
					#if there no additional circular it is automatically a positive
					if len(c) == 0:
						circularPrimes.append(x)
					else:
						#check if each circular prime
						p = True 
						for y in c:
							p = isPrime(y)
							if not p:
								break
						if p:
							circularPrimes.append(x)
							circularPrimes += c
	print "Total circular primes found %d" % len(circularPrimes), circularPrimes

if __name__ == '__main__':
	main()

