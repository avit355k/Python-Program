import random 
import string  
def check(a):     
    if(a[0] == 'A'):
        return True;    
    return False; 

def getRandomString():     
    initial = ""     
    password = ""     
    source = chr(random.randint(65,90))     
    initial += source     
    lc = chr(random.randint(97,122))    
    digit = chr(random.randint(48,57))     
    lst =  []     
    lst.append(lc)     
    lst.append(digit)    
    while(len(lst) > 0):         
        random.shuffle(lst) 
        password += lst.pop()     
    sourcelist = string.ascii_letters + string.digits      
    password += ''.join(random.choice(sourcelist) for i in range(3))     
    passList = list(password)     
    random.shuffle(passList)     
    for i in passList:         
        initial += i     
    return initial 

rlist = [] 
count = 0 
for i in range (50):    
     word = getRandomString()     
     rlist.append(word)     
     if (check(word) == True):         
        count+=1 
print("list is = ", rlist) 
print("word with A as start = ", count)
      