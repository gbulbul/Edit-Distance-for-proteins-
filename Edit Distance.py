# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 23:43:26 2024

@author: gbulb
"""

class find_matches_nonmatches:
    def find_matches(dict_):
        STRING_MATCHES=''
        for value1 in dict_.values():
            for value2 in dict_.values():
                if value1!=value2 and len(value1)<len(value2):
                   for j in range(len(value1)):
                       for i in range(len(value2)):
                           if value1[j]==value2[i]:
                              if value1[j] not in STRING_MATCHES:
                                 STRING_MATCHES+=value1[j]
        return STRING_MATCHES
                             
                                
    def find_nonmatches(dict_,STRING_MATCHES):
        for value1 in dict_.values():
            for value2 in dict_.values():
                if value1!=value2 and len(value1)<len(value2):
                       for j in range(len(STRING_MATCHES)):
                           value2=value2.replace(STRING_MATCHES[j],'',1)
                       return len(value2) #P,S,A,T,L
                             
      
                                   
                         
                         
if __name__=="__main__": 
    dict_={}
    dict_['Rosalind_39']='PLEASANTLY'
    dict_['Rosalind_11']='MEANLY'  
    STRING_MATCHES=find_matches_nonmatches.find_matches(dict_)   
    #print(STRING_MATCHES)     #EANLY
    print(find_matches_nonmatches.find_nonmatches(dict_,STRING_MATCHES))