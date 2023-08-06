# import everything of this pagages
# from folder.file import class

from ggwp.EzDataModel.BasketEvolving import *
from ggwp.EzDataModel.Cohort import *
from ggwp.EzDataModel.CustomerMovement import *
from ggwp.EzDataModel.DataModel import *
from ggwp.EzDataModel.RFMT import *

from ggwp.EzModeling.BenchMark import *
from ggwp.EzModeling.Check import *
from ggwp.EzModeling.Evaluation import *
from ggwp.EzModeling.Log import *

from ggwp.EzPipeline.ConvertVariables import *
from ggwp.EzPipeline.GroupImputer import *

from ggwp.EzUtils import *

from ggwp.config.config import *

# -------------------------------------------------------------


import ggwp, os
current = os.sep.join(ggwp.__file__.split(os.sep)[:-1])
import configparser

config_path  = '{0}/config/config.cfg'.format(current)
parser = configparser.ConfigParser()
parser.read(config_path)
__version__ = parser['default']['version']

# __version__ = "0.0.43"