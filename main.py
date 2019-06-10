import yaml

from . import Dino

with open('./dinos.yaml', 'r') as f:
    a = yaml.load(f, Loader=yaml.FullLoader)
