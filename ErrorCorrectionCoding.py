# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 16:40:48 2016

@author: TedmanForrey
"""

from numpy import *


def powerof2bytewise285(result):
    """ This function give n such as 2**n = result in GF(256)"""
    result = result%256    
    
    alpha=1    
    n=0    
    while alpha != result:
        alpha = alpha*2
        n+=1
        if alpha >= 256:
            alpha=alpha^285
    return n
    
def antilog(n):
    """This function give request such as 2**n = request in GF(256) """
    inte = 0
    request = 1    
    while inte != n:
        inte += 1
        request *= 2
        if (request >= 256):
            request = request^285
    
    return request    
        
def generatorpolynomial (degree):
    """This function generate polynomial such as d(polynomial) = degree """
    if degree == 1:
        return [0,0]
    else:
        T = generatorpolynomial(degree - 1)
        T1 = T[:]
        T2 = T[:]
        
        for i in range(len(T2)):
            T2[i] = T2[i] + degree - 1 
        
        T3 = [T2[0]]
        
        for i in range(1,len(T1)):
            X = (antilog(T1[i-1])^antilog(T2[i]))
            if X >= 256:
                X = X %255
            X = powerof2bytewise285(X)
            T3.append(X) 

        T3.append(T1[len(T1)-1])
        
        return T3
    
def errorcode(T, n):
    """ This function generate the error code of n items for the message encoding in T"""
    gp = generatorpolynomial(n)
    etape = len(T)    
    code = n*[0] + T
    
    while etape != 0:
        etape -= 1

        gpnow = gp[:]
        maxterme = powerof2bytewise285(code[len(code) - 1])
        for i in range(len(gpnow)):
            gpnow[i] = (gpnow[i] + maxterme)%255
            gpnow[i] = antilog(gpnow[i])
            
        
        gpnow = (len(code)-n-1)*[0]+gpnow
        
        for i in range(len(gpnow)):
            code [i] = code[i]^gpnow[i]
        i = len(code) - 1
        
        while code [i] == 0:
            del code[i]
            i -=1

    return code

def inverpoly(T):
    bufferpoly=[]

    for i in range(len(T) -1,-1,-1):
        bufferpoly.append(T[i])

    return bufferpoly           
            
def finalgeneratorerrorcode(T,n):
    bufferpoly=inverpoly(T)
    result=errorcode(bufferpoly,n)
    bufferpoly=inverpoly(result)

    return bufferpoly    
            
    
