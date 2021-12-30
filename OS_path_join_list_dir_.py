import os
import glob
import pandas as pd
path='/home/sandipan/Videos/My-codes-on-MLDL'
a=os.listdir(path)
#print(a)
path0='Use_pretrained_model'
#path1=os.path.join(path,'Use_pretrained_model/','*.csv')
#path2=glob.glob(path1)
#print(path2)
#for f in path2:
    #print(f)

for f in os.listdir(os.path.join(path, path0)):
    #print(f)
    if os.path.isfile(os.path.join(path, path0,f)):
        print(f)
#c=pd.read_csv(path1)
#print(path2)
#for f in path2:
   #rint(f)
   #pd.read_csv(f)
#print(a)
##print(len(path))
#print(type(path1))
#print(c)
