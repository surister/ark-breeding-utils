import yaml
from dinos import Dino, DinoGroup
with open('./dinos.yaml', 'r') as f:
    a = yaml.load(f, Loader=yaml.FullLoader)
    p = [Dino(*k) for k in a]
# FIX ME
group = DinoGroup("Mygroup", p)

"""
# TODO 

group = Group(path, name)
inside group


* __open__ -> opens file, loads and creates the dinos.
* add() -> add dictionary.
* review yaml structure and write yaml template


"""