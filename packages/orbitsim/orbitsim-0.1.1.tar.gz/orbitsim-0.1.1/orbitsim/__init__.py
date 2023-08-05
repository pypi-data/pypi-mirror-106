# -*- coding: utf-8 -*-

"""
RocketPy is a trajectory simulation for High-Power Rocketry built by
[Projeto Jupiter](https://www.facebook.com/ProjetoJupiter/). The code allows
for a complete 6 degrees of freedom simulation of a rocket's flight trajectory,
including high fidelity variable mass effects as well as descent under
parachutes. Weather conditions, such as wind profile, can be imported from
sophisticated datasets, allowing for realistic scenarios. Furthermore, the
implementation facilitates complex simulations, such as multi-stage rockets,
design and trajectory optimization and dispersion analysis.
"""

__author__ = "Alexander Minchin"
__version__ = "0.1.1"
__maintainer__ = "Alexander Minchin"
__email__ = "alexander.w.minchin@gmail.com"
__status__ = "Developement"

from scipy import constants as const
import numpy as np
import kepler as kp
import datetime
from mayavi import mlab
import json

from .Environment import Environment
from .Engine import Engine
from .Spacecraft import Spacecraft
from .Orbit import Orbit