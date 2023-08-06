# flake8: noqa

import pkg_resources


__version__ = pkg_resources.get_distribution("fastflownet").version


from fastflownet.model import FastFlowNet
from fastflownet.visualization import visualize_flow
