import yaml
from dinos import Dino, DinoGroup
with open('./dinos.yaml', 'r') as f:
    a = yaml.load(f, Loader=yaml.FullLoader)
    p = [Dino(*k) for k in a]
# FIX ME
group = DinoGroup("Mygroup", p)