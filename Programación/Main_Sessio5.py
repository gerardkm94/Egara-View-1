import os
import numpy as np
import cPickle as pk
from get_params import get_params
from get_local_features import get_local_features
from train_codebook import train_codebook
from get_assignments import get_assignments
from build_bow import build_bow

#Extraccio dels parametres
params=get_params()
ID =open(os.path.join(params['root'],params['database'],'train','ImageIDs.txt'), 'r')
desc=get_local_features(params,os.path.join(params['root'],params['database'],'train','images',str(ID.readline()).replace('\n','') + '.jpg'))
#Extraccio de les características per a totes les imatges d'entrenament
for line in ID:
    x=get_local_features(params,os.path.join(params['root'],params['database'],'train','images',str(line).replace('\n','') + '.jpg'))
    #Concatenar les caracteristiques de cada imatge
    desc=np.concatenate((desc,x))
ID.close()

#Entrenament del KMeans només per les fotos d'entrenament
codebook=train_codebook(params,desc)

ID =open(os.path.join(params['root'],params['database'],'val','ImageIDs.txt'), 'r')
desc_val=get_local_features(params,os.path.join(params['root'],params['database'],'val','images',str(ID.readline()).replace('\n','') + '.jpg'))
assignments=get_assignments(desc_val,codebook)
dic1=dict()
dic1[str(ID.readline()).replace('\n','')]=build_bow(assignments,codebook)
for line in ID:
    x=get_local_features(params,os.path.join(params['root'],params['database'],'val','images',str(line).replace('\n','') + '.jpg'))
    assignments=get_assignments(x,codebook)
    dic1[str(line).replace('\n','')]=build_bow(assignments,codebook)
ID.close()

