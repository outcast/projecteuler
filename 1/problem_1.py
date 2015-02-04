#!/usr/bin/env python
# encoding: utf-8
"""
problem_1.py

Created by James Jones on 2015-02-04.

Problem 1 from https://projecteuler.net/problem=1

Description:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Output: 233168

Reason for picking problem: It was the first one on the list

References: None

Time took: 10 Minutes


"""

def main():
	#Creating a list to keep track of the sum
	mySum = 0
	#Only going for 0 - 999 since we are only looking for numbers below 1000 and there for don't need to add an addtional if statement to check if below 1000
	for x in range(1000):
		# if the modulas of the current number and 3 or 5 is 0 number is muliple of 3 or 5 add it to the current sum.
		if x % 3 == 0 or x % 5 == 0:
			mySum += x
			
	#Output sum
	print mySum

if __name__ == '__main__':
	main()

