'''
Created on Aug 30, 2018

@author: Manikandan.R
'''

print ('Running Fibonacci')
a, b = 0, 1
while a < 10:
 print(a, end=',')
 a, b = b, a + b

print ('Handling Strings')  
alphas = "abcdefghijklmnopqrstuvwxyz"
index = len(alphas) // 2
alpha1 = alphas[: index]
alpha2 = alphas[index :]
print ('alphas: ' + alphas)
print ('alpha1: ' + alpha1)
print ('alpha2: ' + alpha2)

print ('Handling Lists')

lists = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print ('My List: ', lists)
print ('4th element from start: ', lists[4])
print ('1st element from end: ', lists[-1])     