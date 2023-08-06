from __future__ import division

import math

import cv2
import numpy as np

from anet_tools.anet_db import Video
from anet_tools.video.video_info import get_video_duration


class VideoProc(object):

    def __init__(self, vid_info, open_on_init=False):
        self._vid_info = vid_info
        self._vid_path = vid_info.path
        self._instances = vid_info.instances

        # video info
        self._vid_cap = None
        self._fps = -1
        self._frame_count = -1
        self._real_fps = -1
        self._frame_width = -1
        self._frame_height = -1

        # length limit
        self._max_frames = 30 * (-1)

        if open_on_init:
            self.open_video()

    @staticmethod
    def from_file(video_filename):
        duration_in_second = get_video_duration(video_filename)
        info_dict = {
          'annotations': list(),
          'url': '',
          'duration': duration_in_second,
          'subset': 'testing'
         }

        vid_info = Video('0', info_dict)
        vid_info.path = video_filename
        video_proc = VideoProc(vid_info)
        video_proc.open_video(False)
        return video_proc

    def open_video(self, preload=True):
        vcap = cv2.VideoCapture(self._vid_path)

        if not vcap.isOpened():
            raise IOError("Cannot open video file {}, associated to video id {}".format(
                self._vid_path, self._vid_info.id
            ))
        self._frame_width = vcap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self._frame_height = vcap.get(cv2.CAP_PROP_FRAME_HEIGHT)

        if not preload:
            self._fps = vcap.get(cv2.CAP_PROP_FPS)
            self._frame_count = vcap.get(cv2.CAP_PROP_FRAME_COUNT)
            self._real_fps = self._frame_count / float(self._vid_info.duration)
            self._vid_cap = vcap
            self._loaded = False
        else:
            cnt = 0
            self._frames = []
            cnt = 0
            while True:
                suc, frame = vcap.read()
                cnt += 1

                if 0 < self._max_frames <= cnt:
                    break

                if suc:
                    self._frames.append(frame)
                else:
                    break
            self._frame_count = len(self._frames)
            self._real_fps = self._frame_count / float(self._vid_info.duration)
            self._loaded = True

    def frame_iter(self, starting_frame=0, interval=1, length=1, timely=False, new_size=None, ignore_err=False,
                   debug=False):
        """This is a generator that will return a set of frames according to step and length

        :param starting_frame: the frame index from which the iteration starts
        :param interval: interval of frame sampling
        :param length: how many frame to extract at once
        :param timely: if set to True, the interval will be using the unit of second, instead of frame
        :return: generator of frame stacks
        """
        if not self._loaded:
            self._vid_cap.set(cv2.CAP_PROP_POS_FRAMES, starting_frame)

            if int(self._vid_cap.get(cv2.CAP_PROP_POS_FRAMES)) != starting_frame:
                raise IOError("Fail to locate to frame {} of video {} associated with ")

        if timely:
            # calculate the frame interval for the time interval
            frame_interval = int(math.ceil(self._real_fps * interval))
            if debug:
                print('frame interval is {}'.format(frame_interval))
        else:
            frame_interval = interval

        # start the iters
        cur_frame = starting_frame
        while (cur_frame + length) <= self._frame_count:
            frames = []
            for i in range(length):
                if self._loaded:
                    frm = self._frames[cur_frame+i]
                    if new_size is not None:
                        frm = cv2.resize(frm, new_size)
                    frames.append(frm.copy())
                else:
                    success, frm = self._vid_cap.read()
                    if not success:
                        if not ignore_err:
                            raise IOError("Read frame failed")
                        else:
                            raise StopIteration
                    if new_size is not None:
                        frm = cv2.resize(frm, new_size)
                    frames.append(frm.copy())
            cur_frame += length
            yield frames

            if not self._loaded:
                skip = frame_interval - length
                if 0 < skip < 100:
                    for i in range(skip):
                        self._vid_cap.read()
                    cur_frame += skip
                elif skip < 0 or skip >= 5:
                    self._vid_cap.set(cv2.CAP_PROP_POS_FRAMES, cur_frame + skip)
                    cur_frame += skip
            else:
                cur_frame += frame_interval - length


class ImageSequenceProc(object):

    def __init__(self, imgs, timestamps):
        if len(imgs) != len(timestamps):
            raise ValueError(
                "length of imgs and timestamps should be same.")
        if len(imgs) == 0:
            raise ValueError('length of imgs should be greater than 0.')

        timestamps = np.array(timestamps, dtype=np.float64)
        sorted_indices = np.argsort(timestamps)
        timestamps = timestamps[sorted_indices]
        imgs = np.array(imgs, dtype=np.uint8)[sorted_indices]
        timestamps = timestamps - timestamps[0]
        first_frame = imgs[0]

        self._frame_height, self._frame_width, _ = first_frame.shape

        dt = np.min(np.diff(timestamps))

        self._frames = imgs
        self._frame_count = len(self._frames)
        self._real_fps = 1.0 / dt
        self._timestamps = timestamps

        indices = []
        j = 0
        n = len(self._timestamps)
        for i in range(int(np.ceil(timestamps[-1] / dt))):
            stamp = dt * i
            while n - 1 > j:
                prev = self._timestamps[j]
                cur = self._timestamps[j + 1]
                if prev <= stamp < cur:
                    break
                j += 1
            indices.append(j)
        self.indices = indices

    def frame_iter(self, starting_frame=0, interval=1, length=1,
                   new_size=None):
        # calculate the frame interval for the time interval
        frame_interval = int(math.ceil(self._real_fps * interval))

        indices = self.indices

        # start the iters
        cur_frame = starting_frame
        while (cur_frame + length) <= self._frame_count:
            frames = []
            for i in range(length):
                frm = self._frames[indices[min(cur_frame + i, len(indices) - 1)]]
                if new_size is not None:
                    frm = cv2.resize(frm, new_size)
                frames.append(frm.copy())
            cur_frame += length
            yield frames
            cur_frame += frame_interval - length
