# flake8: noqa

import pkg_resources

__version__ = pkg_resources.get_distribution("anet-tools").version


import anet_tools.augmentation
import anet_tools.features
import anet_tools.video
from anet_tools.anet_db import ANetDB
from anet_tools.feature_extractor import ActionFeatureExtractor
