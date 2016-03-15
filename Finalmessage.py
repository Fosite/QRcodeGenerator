# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 19:03:27 2016

@author: TedmanForrey
"""

import os
execfile('DataCoding.py')
execfile('ErrorCorrectionCoding.py')

def finalmessage(message, errorlevel):
    
    "Don't forget! Encoding depend on the message!!!"
    encoder=Bytecoding(message,errorlevel)
    
    table=encoder.tablelength
    codeword=encoder.encodingdata()
    
    numberblock1=table.getcodewordblockgroup1()
    numberblock2=table.getcodewordblockgroup2()
    numberblockmax=max(numberblock1,numberblock2)
    numberblocktotal=table.getblockgroup1()+table.getblockgroup2()
    
    message=[]
    errorcode=[]
    
    for i in range(table.getblockgroup1()):
        message.append(codeword[:numberblock1])
        errorcode.append(finalgeneratorerrorcode(codeword[:numberblock1],table.getlengtherror()))
        codeword=codeword[numberblock1:]
    
    for i in range(table.getblockgroup2()):
        message.append(codeword[:numberblock2])
        errorcode.append(finalgeneratorerrorcode(codeword[:numberblock2],table.getlengtherror()))
        codeword=codeword[numberblock2:]
    
    finalmessage=[]    

    for i in range(numberblockmax):
        for j in range(numberblocktotal):
            if len(message[j]) > i:
                finalmessage.append(message[j][i])
                
    for i in range(table.getlengtherror()):
        for j in range(numberblocktotal):
            if len(errorcode[j]) > i:
                finalmessage.append(errorcode[j][i])
    
    return finalmessage
    
