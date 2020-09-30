# %% Import Weka
import weka.core.jvm as jvm
from weka.core.converters import Loader
import weka.core.converters as converters
import weka.core.packages as packages
from weka.core.classes import complete_classname
from weka.classifiers import Classifier
import weka.plot.graph as graph # pygraphviz and PIL required 
from weka.core.classes import Random, from_commandline
import weka.core.serialization as serialization 
import re 
from tqdm import tqdm 

import time 
import pandas as pd



# %%
st = time.time()
jvm.start(packages = True)
pkg = 'PBC4cip'

#install package 
if not packages.is_installed(pkg):
    print(f'Install the package {pkg}')
    packages.intall_package(pkg)
    print(f'Installed {pkg}')
    jvm.stop()
    sys.exit(0)

data_dir = 'datasets/'
csv_file = "universities-3.csv"

# %%

loader = Loader(classname = 'weka.core.converters.ArffLoader')
data = loader.load_any_file(data_dir + 'iris.arff')
data.class_is_last()
print(data)

# %%
import weka.core.converters as converters
data = converters.load_any_file(data_dir + file)
data.class_is_last()

print(data)



# %%
