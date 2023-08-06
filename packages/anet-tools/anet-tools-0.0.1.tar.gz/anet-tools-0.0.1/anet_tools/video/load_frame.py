import cv2


def load_frame(video_path, start=0.0, duration=-1,
               target_size=None):
    """Load frame

    Parameters
    ----------
    video_path : str or pathlib.Path
        input video path.
    start : float
        start time
    duration : int or float
        duration. If this value is `-1`, load all frames.

    Returns
    -------
    frames : list[numpy.ndarray]
        all frames.
    stamps : list[float]
        time stamps.
    """
    video_path = str(video_path)
    vid = cv2.VideoCapture(video_path)
    vid.set(cv2.CAP_PROP_POS_MSEC, start)
    vid_avail = True
    frames = []
    stamps = []
    while True:
        mills = vid.get(cv2.CAP_PROP_POS_MSEC)
        vid_avail, frame = vid.read()
        if not vid_avail:
            break
        if duration != -1 and mills > start + duration:
            break
        if target_size is not None:
            frame = cv2.resize(frame, target_size)
        frames.append(frame)
        stamps.append(mills / 1000.0)
    vid.release()
    return frames, stamps


def frame_extractor(video_path, start_time, end_time):
    video_path = str(video_path)
    cap = cv2.VideoCapture(video_path)

    fps = cap.get(cv2.CAP_PROP_FPS)
    dt = 1.0 / fps

    second = start_time
    cap.set(cv2.CAP_PROP_POS_MSEC, second * 1000)
    success, image = cap.read()
    while success and second <= end_time:
        second += dt
        yield image
        success, image = cap.read()
    cap.release()
