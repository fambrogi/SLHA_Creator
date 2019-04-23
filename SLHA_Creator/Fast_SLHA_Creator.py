import os,sys

'''
This simple script just ask to input the txname and the masses of the particles you want to produce the SLHA for
'''


topo = raw_input('Please insert the topology (e.g. T5WW, TSlepSlep ...) \n')

Template = 'Templates/'+topo+'.template'
Out_Dir  = topo+'_OUTPUT_SLHA_Fast'

os.system('rm -r ' + Out_Dir)
os.system('mkdir ' + Out_Dir)

masses = 'a'

while masses != 'NO':
        masses = raw_input('Insert the three masses MOTHER, INTERMEDIATE, NEUTRALINO ; NO to stop \n \n')
        split = masses.split(' ')
        M = split[0]
        I = split[1]
        D = split[2]

        temp = open(Template, 'r')
        slha = open(Out_Dir+'/'+topo+'_'+str(M)+'_'+str(I)+'_'+str(D)+'.slha' , 'w')
        lines_in = temp.readlines()
        for line in lines_in:
                if ('MOTHER')in line:
                    line = line.replace('MOTHER',str(M))
                if ('NEUTRALINO') in line:
                    line = line.replace('NEUTRALINO',str(D))

                if ('INTERMEDIATE') in line:
                    line = line.replace('INTERMEDIATE',str(I))
                slha.write(line)
        temp.close()
        slha.close()

