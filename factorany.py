# # Python program to print prime factors

# import math

# # A function to print all prime factors of
# # a given number n
# def primeFactors(n):
	
# 	# Print the number of two's that divide n
# 	while n % 2 == 0:
# 		print(2)
# 		n = n // 2
		
# 	# n must be odd at this point
# 	# so a skip of 2 ( i = i + 2) can be used
# 	for i in range(3,int(math.sqrt(n))+1,2):
		
# 		# while i divides n , print i ad divide n
# 		while n % i== 0:
# 			print(i)
# 			n = n // i
			
# 	# Condition if n is a prime
# 	# number greater than 2
# 	if n > 2:
# 		print(n)
		
# # Driver Program to test above function

# n = 1200
# primeFactors(n)

# # This code is contributed by Harshit Agrawal 
# #Code Improved by Sarthak Shrivastava
# Program to find the sum of factors of a number
n = int(input("Enter number"))

def sum_ (n):
  s=0
  for i in range(1,n+1):
    if n%i==0 :
      s += i
  return s
  
print('sum: ' + str(sum_(n)))