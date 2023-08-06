import sys
import codefast.utils as utils
from codefast.logger import Logger

# Export methods and variables
json = utils.JsonIO
text = utils.FileIO
file = utils.FileIO
csv = utils.CSVIO
net = utils.Network

p = utils.p
pp = utils.pp
say = utils.FileIO.say
format = utils.FormatPrint
logger = Logger()
info = logger.info
error = logger.error

sys.modules[__name__] = utils.wrap_mod(sys.modules[__name__],
                                       deprecated=['text'])
