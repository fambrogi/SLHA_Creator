import os,sys
from SLHA_Input import *
'''
This script easily creates the SLHA grid for the topology specified.
You have to type at running time the plane you consider, and edit here the binning for the mother and daughter particles
'''

Topo_Direct  = ['T1tttt','T1ttttoff','T2cc','TSlepSlep','T1bbbb', 'T1','T2bb',
                'TChiWZ','TChiWZ_BinoWino','TChiWZ_WinoBino','TChiWZ_HiggsinoWino','TChiWZ_BinoHiggsino',
                'T2tt','T2ttoff','TChiWW','T1btbt', 'TChiZZ_BinoWino']


Topo_Cascade = ['T5WW','T5WWoff','T5ZZ','T5ZZoff', 'T5tttt',
                'TChiChipmSlepSlep','TChipChimSlepSnu',
                'T6bbWW','T6ttWW','T6','T5bbbb',
                'T6ZZtt','T6ZZbbWW','T6ZZbbWWoff',
                'T6ZZofftt','T6ZZoffbbWW','T6ZZoffbbWWoff',
                'TSlepW','T5VV', 'T6WWttoff', 'T1bbbt']

def SLHA_Write(SMS, M,D,I, Out_Dir, t = ''):
        if (not os.path.isfile('Templates/'+SMS+'.template') ):
            print 'The template does not esist !!! CHECK the templates folder!'
            sys.exit()
        temp = open('Templates/'+SMS+'.template', 'r')
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

            
Template_Folder = os.getcwd()+'/Templates' # Folder containing the template SLHA files
# Choose the topology

Mothers   = [i*Mother_Binning   for i in range(0,40) if i*Mother_Binning   < Mother_Max   ]
Daughters = [i*Daughter_Binning for i in range(0,40) if i*Daughter_Binning < Daughter_Max ]
            
I = 0 # dummy for the case of direct decays
            
Out_Dir = SMS +'_'+ Type +'_'+ str(x) +'_'+ str(Delta_Mother_Intermediate) +'_'+ str(Delta_Intermediate_Daughter)
os.system('rm -r ' + Out_Dir)
os.system('mkdir ' + Out_Dir)

for M in Mothers:
    m = float(M)
    if m < Mother_Min: continue 
    for D in Daughters: 
        if D == 0: D = 1
        d = float(D)
        if (d >= m): continue
        if (i > m): continue
        
        if   Type == 'DIRECT':
             if (m-d) < Min_Gap_Mother_Daughter: continue
             SLHA_Write(SMS, M,D,I, Out_Dir)
             #SLHA_Write(SMS, M,M-5,I, Out_Dir)
             #SLHA_Write(SMS, M,M-20,I, Out_Dir)
                         
        elif Type == 'X':
             i = m*x  + d*(1.- x)
             
             if (d > i): continue
             if ( (m-i) < Min_Gap_Mother_Intermediate   ) : continue
             if ( (i-d) < Min_Gap_Intermediate_Daughter ) : continue
             if ( (m-i) > Max_Gap_Mother_Intermediate   ) : continue
             if ( (i-d) > Max_Gap_Intermediate_Daughter ) : continue

             I = str(i)

             SLHA_Write(SMS, M,D,I, Out_Dir, t = Type)
            
        elif Type == 'DELTA_M_I':
             i = m - Delta_Mother_Intermediate
             
             if (d > i): continue
             if ( (m-i) < Min_Gap_Mother_Intermediate   ) : continue
             if ( (i-d) < Min_Gap_Intermediate_Daughter ) : continue
             if ( (m-i) > Max_Gap_Mother_Intermediate   ) : continue
             if ( (i-d) > Max_Gap_Intermediate_Daughter ) : continue
             
             I = str(i)

             SLHA_Write(SMS, M,D,I, Out_Dir, t = Type)

        elif Type == 'DELTA_I_D':
             i = d + Delta_Intermediate_Daughter
             
             if (d > i): continue
             if ( (m-i) < Min_Gap_Mother_Intermediate   ) : continue
             if ( (i-d) < Min_Gap_Intermediate_Daughter ) : continue
             if ( (m-i) > Max_Gap_Mother_Intermediate   ) : continue
             if ( (i-d) > Max_Gap_Intermediate_Daughter ) : continue
             
             I = str(i)
             
             SLHA_Write(SMS, M,D,I, Out_Dir, t = Type)
        
        else: print 'WTF is this model ???'
            
            
            
