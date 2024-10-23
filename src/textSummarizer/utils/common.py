# utility functions - functions which we use a lot 

import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml : Path) -> ConfigBox : 
    """
    reads yaml file and returns a ConfigBox object
    
    Args : path_to_yaml (str) : path like input 
    
    Raises : 
        ValueError : if yaml file is empty or does not exist
        e : empty file
    
    Returns : ConfigBox object
    """

    try: 
        with open(path_to_yaml, 'r') as file:
            config_dict = yaml.safe_load(file)
            logger.info(f"Successfully loaded yaml file : {path_to_yaml}")
            return ConfigBox(config_dict)
    
    except BoxValueError :
        raise ValueError(f"Invalid yaml file : {path_to_yaml}")
    
    except Exception as e:
        raise e 

@ensure_annotations
def create_directory(directory_paths : list , verbose  = True):
    """
    create list of directories
    Args : directory_paths (list) : list of paths like input
    """

    for path in directory_paths :
        os.makedirs(path, exist_ok=True)
        if verbose :
            logger.info(f"Created directory : {path}")

@ensure_annotations
def get_size(path : str) -> str:
    """
    get size of file in KB
    Args : path (str) : path like input
    """

    size_in_kb = round(os.path.getsize(path) / 1024)
    return f" ~ {size_in_kb} KB"