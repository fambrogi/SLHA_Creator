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


Glu  = [ 1 + i*50 for i in range (0,21) ] 

Glu = [ 200, 400 , 600 , 900 ] 
Squa = [ 500, 1000]

Glu = [500]
Sq = [1000]


Neu  = [ 1 + i*75 for i in range (0,50) ] 


OUT_DIR = 'TGonQ_TEST_2'
os.system('rm -r ' + OUT_DIR )
os.system('mkdir ' + OUT_DIR )

for q in Squa :
    if q > 2001 : continue
    for g in Glu:
        if g >= (q - 4 ) : continue
        if g > 1001      : continue
        
        for n in Neu:
            if n < 1: continue
            if n > g : continue
            
 
#            print g , ' ' , s , ' ' , n
            SLHA_Write( T, q, 30    ,  g , Out_Dir = OUT_DIR+'/TGonQ_Sq_' + str(q) , t = 'yes' ) 
            SLHA_Write( T, q, n     ,  g , Out_Dir = OUT_DIR+'/TGonQ_Sq_' + str(q) , t = 'yes' )
	    SLHA_Write( T, q, g-5   ,  g , Out_Dir = OUT_DIR+'/TGonQ_Sq_' + str(q) , t = 'yes' )
            SLHA_Write( T, q, g-10  ,  g , Out_Dir = OUT_DIR+'/TGonQ_Sq_' + str(q) , t = 'yes' )
            SLHA_Write( T, q, g-20  ,  g , Out_Dir = OUT_DIR+'/TGonQ_Sq_' + str(q) , t = 'yes' )


