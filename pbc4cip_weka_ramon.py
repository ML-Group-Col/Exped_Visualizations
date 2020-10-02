import sys
import weka.core.jvm as jvm
import weka.core.packages as packages
from weka.core.classes import complete_classname
from weka.core.converters import Loader
from weka.classifiers import Classifier
import weka.plot.graph as graph  # NB: pygraphviz and PIL are required
from weka.core.classes import Random, from_commandline
import weka.core.serialization as serialization
import re
from tqdm import tqdm
import time
import pandas as pd

start_time = time.time()
jvm.start(packages='C:/Users/edudi/wekafiles', max_heap_size='12g')

pkg = "PBC4cip"
pkg_source = 'C:/Users/edudi/Downloads/PBC4cip-1.0-weka.zip'
print(complete_classname("." + pkg))
# install package if necessary 
if not packages.is_installed(pkg):
    print("Installing %s..." % pkg)
    #packages.install_package("http://prdownloads.sourceforge.net/weka/discriminantAnalysis1.0.3.zip?download")
    packages.install_package(pkg_source)
    print("Installed %s, please re-run script!" % pkg)
    jvm.stop()
    sys.exit(0)

# testing classname completion

print("\n\n\n\n\n")
print(">>> Start...")

data_dir = "G:/My Drive/Github/DRAE-MLP/Exped_Visualizations/"
arff_file = "weka_dataset_clean.arff"

loader = Loader(classname="weka.core.converters.ArffLoader")
data = loader.load_file(data_dir + arff_file)
data.class_is_last()

filename_array = ["NumberOfTrees", "RandomFeatures", "DepthOfTrees", "MinimumObjectByLeaf", "RandomSubSpace", "InfoGainAttributeEval", "PrincipalComponents", "GainRatioAttributeEval", "WrapperSubsetEval", "CorrelationAttributeEval"]
filename = str(filename_array[9])
filename_index = filename_array.index(filename)

cmdline = []