'''
Created on Aug 30, 2018

@author: Manikandan.R
'''
animals = ['cat', 'dog', 'elephant']
for w in animals:
    print (w, len(w))

#iterating over lists modified inside for loop
for w in animals[:]: #here using the sliced version of a animal list so that we aren't acting on actual animal list
    if len(w) > 3:
        animals.insert(0, w)

print ('Final animals: ', animals)   

#working with range function range (start, end, step)
for i in range(5):
    print (i)
    
rngs = ['mary', 'had', 'a', 'little', 'lamb']
for i in range(len(rngs)):
    print (i, rngs[i])

#Using list function to print range values
print (range(5)) #not desired result
print (list(range(5))) #will give desired result

#break statement
#finding the prime number between 2 & 10
for n in range (2,10):
    for x in range (2, n):
        if n % x == 0:
            print (n, ' equals ', x, '*', n // x)
            break
    else:
        #executed when break is not executed inside for loop
        print (n, ' is a prime number')
        
#continue statement
#finding odd and even numbers
for n in range (2, 10):
    if n % 2 == 0:
        print (n, ' is a even number')
        continue
    print (n, ' is a odd number')

#pass statements is like a TODO placeholders in Java, does nothing
#creating loop with pass statement
#while True:
#    pass

#pass with class
#class minimalClass:
#...   pass

#pass with function
#def initFunc(*args)
#...    pass 
