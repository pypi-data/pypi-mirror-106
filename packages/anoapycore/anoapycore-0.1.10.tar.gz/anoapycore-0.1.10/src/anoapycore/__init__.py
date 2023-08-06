from . import data
from . import chart
from . import ml
from . import statmodel

from pkg_resources import get_distribution as __dist

def version () :
    return __dist('anoapycore').version
