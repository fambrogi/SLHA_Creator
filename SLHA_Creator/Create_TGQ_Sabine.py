import os,sys

T = 'Templates/TGonQ.template'


def SLHA_Write(T, M,D,I, Out_Dir='' , t = 'yes'):
        SMS = 'TGonQ'
        #os.system('rm -r ' + Out_Dir )
        os.system('mkdir ' + Out_Dir )

        #os.system('rm -r ' + Out_Dir )
        #os.system('mkdir ' + Out_Dir )

        temp = open(T)
        slha = ''
        if t : slha = open(Out_Dir+'/'+SMS+'_'+str(M)+'_'+str(I)+'_'+str(D)+'_'+str(M)+'_'+str(I)+'_'+str(D)+'.slha' , 'w')
        else  : slha = open(Out_Dir+'/'+SMS+'_'+str(M)+'_'+str(D)+'_'+str(M)+'_'+str(D)+'.slha' , 'w')
        lines_in = temp.readlines()

        for line in lines_in:
            line = line.replace('MOTHER',str(M))
            line = line.replace('NEUTRALINO',str(D))
            line = line.replace('INTERMEDIATE',str(I))
            slha.write(line)
            temp.close()


Glu  = [ 1100 + i*100 for i in range (0,38) ] 
Squa = [ 100 + i*75 for i in range (0,50) ]
Neu  = [ 1 + i*75 for i in range (0,50) ] 


OUT_DIR = 'TGonQ_TEST'

for g in Glu :
    if g < 1201 : continue
    if g > 2001 : continue
    for s in Squa:
        if s >= (g - 4 ) : continue
        if s > 1001      : continue
        
        for n in Neu:
            if n > s : continue
 
#            print g , ' ' , s , ' ' , n
            SLHA_Write( T, g, 30    ,  s , Out_Dir = OUT_DIR+'/TGonQ_Sq' + str(q) , t = 'yes' ) 
            SLHA_Write( T, g, n     ,  s , Out_Dir = OUT_DIR+'/TGonQ_Sq' + str(q) , t = 'yes' )
	    SLHA_Write( T, g, s-5   ,  s , Out_Dir = OUT_DIR+'/TGonQ_Sq' + str(q) , t = 'yes' )
            SLHA_Write( T, g, s-10  ,  s , Out_Dir = OUT_DIR+'/TGonQ_Sq' + str(q) , t = 'yes' )
            SLHA_Write( T, g, s-20  ,  s , Out_Dir = OUT_DIR+'/TGonQ_Sq' + str(q) , t = 'yes' )


