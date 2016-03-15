# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 18:44:17 2016

@author: TedmanForrey
"""
from abc import ABCMeta, abstractmethod

class Datacode():
    __metaclass__=ABCMeta
    
    def __init__(self, message, errorlevel):
        self.tablelength = Codingtable(errorlevel)        
        self.message = message
        self.code = ""
        self.tablelength.computeversion(len(message))
        
    def encodingdata(self):
        self.code += self.encodingtype()
        self.code += self.addsizetocode()
        self.code += self.messageencoding()
        self.code += self.zeropadding()        
        self.code += self.codepadding()        
        
        return self.topolynomial()
        
    def addsizetocode(self):
        le = self.tablelength.getlengthsize(self.toString)
        return bin(len(self.message))[2:].zfill(le)
        
    def zeropadding(self):
        n1 = (self.tablelength.getlengthcoding())*8 - len(self.code)
        n = min(n1, 4)
        code = n*'0'
        n1 -= n
        if n1 > 0:
            n2 = len(self.code) + n
            n2 = n2%8
            code += (8-n2)*'0'
            
        return code
        
    def codepadding(self):
        pad1 = '11101100'
        pad2 = '00010001'
        n = len(self.code)
        code = ""        
        
        while n < self.tablelength.getlengthcoding()*8:
            code += pad1
            n += 8
            if n >= self.tablelength.getlengthcoding()*8:
                break
            code += pad2
            n += 8
            
        return code
        
    def topolynomial(self):

        poly = []
        current = self.code
        
        while len(current) > 0 : 
            poly += [int(current[:8],2)]
            current = current[8:]
            
        return poly
        
    @abstractmethod
    def encodingtype(self):pass
    
    @abstractmethod
    def messageencoding(self):pass

    @abstractmethod
    def toString(self):pass
        
    
    
class Numeric(Datacode):   
    def encodingtype(self):
        return "0001"        
        
    def toString(self):return "Numeric"        
        
class Alphanumeric(Datacode):
    def encodingtype(self):
        return "0010"

    def toString(self): return "Alphanumeric"
    
class Bytecoding(Datacode):
    def encodingtype(self):
        return "0100"
    
    def messageencoding(self):
        self.message.encode('iso-8859-1')
        code = ""
        for i in self.message:
            code = code + bin(ord(i))[2:].zfill(8)
        return code
        
    def toString(self):return "Bytecoding"
        
class Kanjicoding(Datacode):
    def encodingtype(self):
        return "1000"
        
    def toString(self): return "Kanjicoding"
        
class Codingtable:
    def __init__(self, errorlevel):
        self.version = 1        
        self.errorlevel = errorlevel        
    
    def computeversion(self, length):
        return self.version 
    
    def getlengthsize(self, encoding):
        return 8
        
    def getlengthcoding(self):
        return 13

    def getlengtherror(self):
        return 13        
        
    def getblockgroup1(self):
        return 1
        
    def getblockgroup2(self):
        return 0
    
    def getcodewordblockgroup1(self):
        return 19
        
    def getcodewordblockgroup2(self):
        return 0
