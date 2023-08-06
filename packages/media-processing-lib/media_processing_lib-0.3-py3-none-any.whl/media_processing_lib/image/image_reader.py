import numpy as np
from ..utils import dprint
from pathlib import Path

def tryReadImage(path:str, imgLib:str="opencv", count:int=5) -> np.ndarray:
	assert imgLib in ("opencv", "PIL", "pillow", "lycon")
	if imgLib == "opencv":
		from .libs.opencv import readImage
	elif imgLib in ("PIL", "pillow"):
		from .libs.pil import readImage
	elif imgLib == "lycon":
		from .libs.lycon import readImage

	path = str(path) if isinstance(path, Path) else path

	i = 0
	while True:
		try:
			return readImage(path)
		except Exception as e:
			dprint("Path: %s. Exception: %s" % (path, e))
			i += 1

			if i == count:
				raise Exception(e)