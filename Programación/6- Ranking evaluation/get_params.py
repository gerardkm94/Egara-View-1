import os
import pandas as pd
import numpy as np

def get_params():

    '''
    Define dictionary with parameters
    '''
    params = {}

    # Source data
    params['root'] = '\Users\Gerard\Documents\Universidad\TercerCurso\GDSA\Proyecto\codigo'
    params['database'] = 'TerrassaBuildings900'

    # To generate
    params['root_save'] = 'save'
    params['image_lists'] = 'image_lists'
    params['feats_dir'] = 'features'
    params['rankings_dir'] = 'rankings'
    params['classification_dir'] = 'classification'

    # Parameters
    params['split'] = 'val'
    params['descriptor_size'] = 100
    params['descriptor_type'] = 'random'
    
    # We read the training annotations to know the set of possible labels
    data = pd.read_csv(os.path.join(params['root'],params['database'],'train','annotation.txt'), sep='\t', header = 0)
    
    # Store them in the parameters dictionary for later use
    params['possible_labels'] = np.unique(data['ClassID'])

    create_dirs(params)

    return params


def make_dir(dir):
    '''
    Creates a directory if it does not exist
    dir: absolute path to directory to create
    '''
    if not os.path.isdir(dir):
        os.makedirs(dir)

def create_dirs(params):

    '''
    Create directories specified in params
    '''
    save_dir = os.path.join(params['root'], params['root_save'])

    make_dir(save_dir)
    make_dir(os.path.join(save_dir,params['image_lists']))
    make_dir(os.path.join(save_dir,params['feats_dir']))
    make_dir(os.path.join(save_dir,params['rankings_dir']))
    make_dir(os.path.join(save_dir,params['classification_dir']))
    
    make_dir(os.path.join(save_dir,params['rankings_dir'],params['descriptor_type']))
    make_dir(os.path.join(save_dir,params['rankings_dir'],params['descriptor_type'],params['split']))
    make_dir(os.path.join(save_dir,params['classification_dir'],params['descriptor_type']))

if __name__ == "__main__":

    params = get_params()