import cv2
import numpy as np
from typing import Tuple, List, Optional
from pathlib import Path
from ....utils import dprint

def readRaw(path:str, nFrames:Optional[int]) -> Tuple[np.ndarray, int, List[int], int]:
	dprint("[mpl::video::opencv] Reading raw data.")
	path = str(path) if isinstance(path, Path) else path
	cap = cv2.VideoCapture(path)
	fps = cap.get(cv2.CAP_PROP_FPS)
	nFrames = 1<<31 if nFrames is None else nFrames

	data = []
	i = 0
	while cap.isOpened():
		if i == nFrames:
			break

		i += 1
		ret, frame = cap.read()
		if not ret:
			break

		frame = frame[..., ::-1]
		data.append(frame)
	cap.release()

	video = np.array(data)
	nFrames = len(video)
	video = video[..., 0 : 3]

	return video, fps, video.shape, nFrames