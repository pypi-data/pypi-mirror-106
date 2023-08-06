import os.path as osp
import subprocess

import skvideo.io


def get_video_duration(video_path):
    video_path = str(video_path)
    if not osp.exists(video_path):
        raise OSError("{} not exists".format(video_path))
    metadata = skvideo.io.ffprobe(video_path)
    if '@duration' not in metadata['video']:
        result = subprocess.Popen(
            ["ffprobe", video_path],
            stdout=subprocess.PIPE, stderr = subprocess.STDOUT)
        duration = [x.decode('utf-8') for x in result.stdout.readlines()
                    if "Duration" in x.decode('utf-8')]
        duration_in_second = float(
            duration[0][15:17]) * 60 + float(duration[0][18:23])
        return duration_in_second
    return float(metadata['video']['@duration'])


def get_video_count(video_path):
    video_path = str(video_path)
    if not osp.exists(video_path):
        raise OSError("{} not exists".format(video_path))
    metadata = skvideo.io.ffprobe(video_path)
    if '@nb_frames' not in metadata['video']:
        nb_frames = subprocess.Popen(
            'ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames -of default=nokey=1:noprint_wrappers=1 {}'.format(video_path).split(),
            stdout=subprocess.PIPE, stderr = subprocess.STDOUT).stdout.read()
        return int(nb_frames)
    return int(metadata['video']['@nb_frames'])
