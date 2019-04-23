import os,sys


os.system('rm -r Out_TGQ')
os.system('mkdir Out_TGQ')

'''
while True:

   m1  = raw_input('gluino:  ')
   m2  = raw_input('squark:  ')
   neu = raw_input('neu:  ')


   IN  = open('ATGQon.template','r')

   new = 'TGQ_'+ m1 + '_' + m2 + '_' + neu + '.slha'
   OUT = open('Out_TGQ/'+new,'w')
   for line in IN.readlines():
       line = line.replace('MOTHER',m1)
       line = line.replace('INTERMEDIATE',m2)
       line = line.replace('NEUTRALINO',neu)
       OUT.write(line)      
'''

while True:                                                                                                                                                                       
                                                                                                                                                                                  
   m1  = raw_input('gluino:  ')                                                                                                                                                   
   m2  = raw_input('squark:  ')                                                                                                                                                   
   neu = raw_input('neu:  ')                                                                                                                                                      
                                                                                                                                                                                  
                                                                                                                                                                                  
   IN  = open('TSlepSlep.template','r')                                                                                                                                      
                                                                                                                                                               
   new = 'TSlepSlep_'+ m1 + '_' + m2 + '_' + neu + '.slha'                                                                                                                     
   OUT = open('Out_SLEP/'+new,'w')                                                                                                                                                 
   for line in IN.readlines():                                                                                                                                                    
       line = line.replace('MOTHER',m1)                                                                                                                                           
       line = line.replace('INTERMEDIATE',m2)                                                                                                                                     
       line = line.replace('NEUTRALINO',neu)                                                                                                                                      
       OUT.write(line)
