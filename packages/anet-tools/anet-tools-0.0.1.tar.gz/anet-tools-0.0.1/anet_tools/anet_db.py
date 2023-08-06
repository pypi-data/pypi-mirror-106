import json
import os
import os.path as osp

from easydict import EasyDict

"""
This file contains the setting for running ActivityNet related experiments.
"""

ANET_CFG = EasyDict()

# Version and other macro settings

cur_dir = osp.dirname(__file__)

ANET_DB_VERSIONS = {
    '1.2': osp.join(cur_dir, 'data/activity_net.v1-2.json'),
    '1.3': osp.join(cur_dir, 'data/activity_net.v1-3.json'),
}

# Force the leaf node to be included in the label list
ANET_CFG.FORCE_INCLUDE = {"1.3": [], "1.2": []}


# Allow using external config files to override the above settings
def LoadExternalYAMLConfig(yaml_file):
    import yaml
    new_cfg = yaml.load(open(yaml_file))
    ANET_CFG.update(new_cfg)


import glob


def get_all_media_files(src_folders, accepted_extensions):
    media_files = []
    for f in src_folders:
        all_files = glob.glob(os.path.join(f, "*"))
        media_files.extend([name for name in all_files if os.path.splitext(name)[-1] in accepted_extensions])
    return media_files


import logging
import sys

_formatter = logging.Formatter('%(asctime)s - %(filename)s:%(lineno)d - [%(levelname)s] %(message)s')
_ch = logging.StreamHandler()
_ch.setLevel(logging.DEBUG)
_ch.setFormatter(_formatter)

def get_logger(debug=False):
    logger = logging.getLogger("pyActionRec")
    logger.setLevel(logging.DEBUG if debug else logging.INFO)
    logger.addHandler(_ch)
    return logger


logger = get_logger()


class Instance(object):
    """
    Representing an instance of activity in the videos
    """

    def __init__(self, idx, anno, vid_id, vid_info, name_num_mapping):
        self._starting, self._ending = anno['segment'][0], anno['segment'][1]
        self._str_label = anno['label']
        self._total_duration = vid_info['duration']
        self._idx = idx
        self._vid_id = vid_id
        self._file_path = None

        if name_num_mapping:
            self._num_label = name_num_mapping[self._str_label]

    @property
    def start_time(self):
        return self._starting

    @property
    def end_time(self):
        return self._ending

    @property
    def time_span(self):
        return self._starting, self._ending

    @property
    def covering_ratio(self):
        return self._starting / float(self._total_duration), self._ending / float(self._total_duration)

    @property
    def num_label(self):
        return self._num_label

    @property
    def label(self):
        return self._str_label

    @property
    def name(self):
        return '{}_{}'.format(self._vid_id, self._idx)

    @property
    def path(self):
        if self._file_path is None:
            raise ValueError("This instance is not associated to a file on disk. Maybe the file is missing?")
        return self._file_path

    @path.setter
    def path(self, path):
        self._file_path = path


class Video(object):
    """
    This class represents one video in the activity-net db
    """
    def __init__(self, key, info, name_idx_mapping=None):
        self._id = key
        self._info_dict = info
        self._instances = [Instance(i, x, self._id, self._info_dict, name_idx_mapping)
                           for i, x in enumerate(self._info_dict['annotations'])]
        self._file_path = None

    @property
    def id(self):
        return self._id

    @property
    def url(self):
        return self._info_dict['url']

    @property
    def instances(self):
        return self._instances

    @property
    def duration(self):
        return self._info_dict['duration']

    @property
    def subset(self):
        return self._info_dict['subset']

    @property
    def instance(self):
        return self._instances

    @property
    def path(self):
        if self._file_path is None:
            raise ValueError("This video is not associated to a file on disk. Maybe the file is missing?")
        return self._file_path

    @path.setter
    def path(self, path):
        self._file_path = path


class ANetDB(object):
    """
    This class is the abstraction of the activity-net db
    """

    def __init__(self, version="1.3"):
        if version not in ANET_DB_VERSIONS:
            raise ValueError("Unsupported database version {}".format(version))

        raw_db_file = os.path.join(ANET_DB_VERSIONS[version])
        db_data = json.load(open(raw_db_file))

        self.version = version
        self._prepare_data(db_data)

    def _prepare_data(self, raw_db):
        self._version = raw_db['version']

        # deal with taxonomy
        self._taxonomy = raw_db['taxonomy']
        self._parse_taxonomy()

        self._database = raw_db['database']
        self._video_dict = {k: Video(k, v, self._name_idx_table) for k,v in self._database.items()}

        # split testing/training/validation set
        self._testing_dict = {k: v for k, v in self._video_dict.items() if v.subset == 'testing'}
        self._training_dict = {k: v for k, v in self._video_dict.items() if v.subset == 'training'}
        self._validation_dict = {k: v for k, v in self._video_dict.items() if v.subset == 'validation'}

        self._training_inst_dict = {i.name: i for v in self._training_dict.values() for i in v.instances}
        self._validation_inst_dict = {i.name: i for v in self._validation_dict.values() for i in v.instances}

    def get_ordered_label_list(self):
        """
        This function return a list of textual labels corresponding the numerical labels. For example, if one samples is
        classified to class 18, the textual label is the 18-th element in the returned list.
        Returns: list
        """
        return [self._idx_name_table[x] for x in sorted(self._idx_name_table.keys())]

    def get_subset_videos(self, subset_name):
        if subset_name == 'training':
            return self._training_dict.values()
        elif subset_name == 'validation':
            return self._validation_dict.values()
        elif subset_name == 'testing':
            return self._testing_dict.values()
        else:
            raise ValueError("Unknown subset {}".format(subset_name))

    def get_subset_instance(self, subset_name):
        if subset_name == 'training':
            return self._training_inst_dict.values()
        elif subset_name == 'validation':
            return self._validation_inst_dict.values()
        else:
            raise ValueError("Unknown subset {}".format(subset_name))

    def _parse_taxonomy(self):
        """
        This function just parses the taxonomy file
        It gives alphabetical ordered indices to the classes in competition
        :return:
        """
        name_dict = {x['nodeName']: x for x in self._taxonomy}
        parents = set()
        for x in self._taxonomy:
            parents.add(x['parentName'])

        # leaf nodes are those without any child
        leaf_nodes = [name_dict[x] for x
                      in list(set(name_dict.keys()).difference(parents)) + ANET_CFG.FORCE_INCLUDE.setdefault(self.version, [])]
        sorted_lead_nodes = sorted(leaf_nodes, key=lambda l: l['nodeName'])
        self._idx_name_table = {i: e['nodeName'] for i, e in enumerate(sorted_lead_nodes)}
        self._name_idx_table = {e['nodeName']: i for i, e in enumerate(sorted_lead_nodes)}
        self._name_table = {x['nodeName']: x for x in sorted_lead_nodes}

    def parse_activitynet_splits(self):
        train_instance = self.get_subset_instance('training')
        val_instance = self.get_subset_instance('validation')
        test_instance = self.get_subset_videos('testing')

        splits = []

        train_list = [(x.name, x.num_label) for x in train_instance]
        val_list = [(x.name, x.num_label) for x in val_instance]
        test_list = [(x.id, 0) for x in test_instance]

        splits.append((train_list, val_list))
        splits.append((train_list + val_list, test_list))

        return splits


if __name__ == '__main__':
    db = ANetDB()
    logger.info("Database construction success".format())
