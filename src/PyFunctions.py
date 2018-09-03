'''
Created on Aug 30, 2018

@author: Manikandan.R
'''

#Default arguments
def prompter(prompt, retries=3, reminder='Pleasr try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes', 'yep'):
            return 'True'
        if ok in ('n', 'no', 'nah', 'nop', 'nope'):
            return 'False'
        retries = retries - 1
        if retries < 0:
            raise ValueError('Invalid user response!!')
        print (reminder)
        
#print('response', prompter('Do you really want to quit?', 2))

#default value manipulation
#default value initiated or evaluated only once. So default values shared between function calls
def f(a, l=[]):
    l.append(a)
    return l

print(f(1))
print(f(2))
print(f(3))

##in case don't want to share the default values
def f1(a, l1=None):
    if l1 is None:
        l1 = [];
    l1.append(a)
    return l1;

print(f1(1))
print(f1(2))
print(f1(3))

#keyword arguments
def keyarg(voltage, state='start', action='run', vtype='inverter'):
    print ('The voltage is ', voltage)
    print('The voltage action is ', action)
    print ('the voltage state is ', state)
    print ('The voltage type is ', vtype)

#correct forms of function call with keyword arguments
keyarg(voltage=1000, state='abort')
keyarg(1000)
keyarg(voltage=2000, vtype='machines', action='wait')

#incorrect foramts
# keyarg(voltage=1500, 'ready') #keyword argument param should be followed by a keyword argument param
# keyarg(2500, voltage=1400) #duplicate keyword argument not allowed
# keyarg(speed='150mph') #incorrect argument name

#positional arguments * and formal parameters **
def pizza(mode, *arguments, **keywords):
    print('Request Pizza mode ', mode)
    print ('User arguments:')
    for arg in arguments:
        print(arg);
    print('User parameters:')
    for kw in keywords:
        print(kw, ' : ', keywords[kw])
        
pizza('Cheezy', 'Topped with Jalapeno', 'With added flavours', type='Hand tossed', sides='chaco lava cake')

#unpacking positional arguments
print (list(range(1,6)))
args = [3,6]
print (list(range(*args)))

#unpacking keyword arguments
args = { 'voltage': 3500, 'state': 'running', 'action':'pause', 'vtype':'refridgerator' }
keyarg(**args)

#lambda function 
def make_func(n):
    return lambda x: x + n

f = make_func(25)
print(f(10))
print(f(15))

#another lambda example
pairs = [(1, 'one'), (2, 'two'), (3, 'three')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)

##Function annotations
def f3(arg1: str, arg2: str = 'Sample') -> str:
    print ('Annotations ', f3.__annotations__)
    print ('Arguments ', arg1, arg2)
    
f3('test')