""" 
A simple script computationally confirming the practical accuracy
of an algorithm. Authors: Jose Luna, John Schneider
copyright UC Berkeley 09/10/2017
"""

import random

random.seed(10)

def gamma(lst):
	tmp = lst[len(lst)-1]
	i = len(lst) - 1
	while i > 0:
		lst[i] = lst[i-1]
		i-=1
	lst[0] = tmp

def tau_01(lst):
	tmp = lst[0]
	lst[0] = lst[1]
	lst[1] = tmp

def beta(lst):
	tau_01(lst)
	gamma(lst)

def comp(f, n, lst):
	while n > 0:
		f(lst)
		n -= 1
	
def tau(i, k, lst):
	n = len(lst)
	comp(gamma, (n-i+1)%n, lst)

	comp(beta, (n+i-k-1)%n, lst)

	tau_01(lst)

	comp(beta, k-i, lst)

	comp(gamma, (i-1)%n, lst)

def check(lst, i, k):
	bl = True
	for j in range(len(lst)-1):
		if j == i:
			bl = (lst[j] == k)
		elif j == k:
			bl = (lst[j] == i)
		else:
			bl = (lst[j] == j)
	return bl
			
	

def main():
	bl = True
	N = 1000
	for l in range(2, N):
		lst = [i for i in range(l)]
		r = r2 = 0
		while r2 <= r:
			r = random.randint(0, l-1)
			r2 = random.randint(0, l-1)
		tau(r, r2, lst)
		if not check(lst, r, r2):
			print("Error: tau ({0}, {1}) did not work correctly on list of length {2}".format(r, r2, l))
			bl = False
	if bl:
		print("Result has been confirmed for n <= {}".format(N))


main()
