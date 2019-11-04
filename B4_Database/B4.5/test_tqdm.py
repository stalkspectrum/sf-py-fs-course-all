'''
import time
from tqdm import tqdm
for i in tqdm(range(10000)):
    time.sleep(0.001)
'''
import yaml
fp = open('example.yaml')
#example = yaml.load(fp, Loader=yaml.FullLoader)
example = yaml.full_load(fp)    ##### See https://github.com/yaml/pyyaml/wiki/PyYAML-yaml.load(input)-Deprecation
fp.close()
print(example)
