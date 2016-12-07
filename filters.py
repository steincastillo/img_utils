# -*- coding: utf-8 -*-
"""
Created on Sun Dec 04 14:48:18 2016

@author: Stein
"""

import cv2
import numpy as np 
import utils

#Edge detection using Laplacian filter
def strokeEdges(src, dst, blurKsize=7, edgeKsize=5):
	if blurKsize >= 3:
		blurredSrc = cv2.medianBlur(src, blurKsize)
		graySrc = cv2.cvtColor(blurredSrc, cv2.COLOR_BGR2GRAY)
	else:
		graySrc = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
	cv2.Laplacian(graySrc, cv2.CV_8U, graySrc, ksize = edgeKsize)
	normalizedinverseAlpha = (1.0 / 255) * (255 - graySrc)
	channels = cv2.split(src)
	for channel in channels:
		channel[:] = channel * normalizedinverseAlpha
	cv2.merge(channels, dst)


class VConvolutionFilter(object):
	"""A filter that applies a convolution to V. """
	def __init__(self, kernel):
		self._kernel = kernel

	def apply(self, src, dst):
		"""Applz the filter with BGR or gray source/destination"""
		cv2.filter2D(src, -1, self._kernel, dst)

class SharpenFilter(VConvolutionFilter):
	"""A sharpen filter with a 1-pixel radius"""
	def __init__(self):
		kernel = np.array([[-1, -1, -1],
							[-1, 9, -1],
							[-1, -1, -1]])
		VConvolutionFilter.__init__(self, kernel)

class FindEdgesFilter(VConvolutionFilter):
	"""An edge-finding filter with a 1-pixel radius"""
	def __init__(self):
		kernel = np.array([[-1, -1, -1],
							[-1, 8, -1],
							[-1, -1, -1]])
		VConvolutionFilter.__init__(self, kernel)

class BlurFilter(VConvolutionFilter):
	"""A blur filter with a 2-pixel radius"""
	def __init__(self):
		kernel = np.array([[0.04, 0.04, 0.04, 0.04, 0.04],
							[0.04, 0.04, 0.04, 0.04, 0.04],
							[0.04, 0.04, 0.04, 0.04, 0.04],
							[0.04, 0.04, 0.04, 0.04, 0.04],
							[0.04, 0.04, 0.04, 0.04, 0.04]])
		VConvolutionFilter.__init__(self, kernel)

class EmbossFilter(VConvolutionFilter):
	"""An emboss filter with a 1-pixel radius"""
	def __init__(self):
		kernel = np.array([[-2, -1, 0],
							[-1, 1, 1],
							[ 0, 1, 2]])
		VConvolutionFilter.__init__(self, kernel)

class SharpenFilter(VConvolutionFilter):
	"""A sharpening filter with a 1 pixel radius"""
	def __init__(self):
		kernel = np.array([[0, -1, 0],
				[-1,  5, -1],
				[ 0, -1,  0]])
		VConvolutionFilter.__init__(self, kernel)

class AverageBlur(VConvolutionFilter):
	"""Average blur filter, 1 pixel radius"""
	def __init__(self):
		kernel = np.array([[1, 1, 1],
				[1, 1, 1],
				[1, 1, 1]])
		VConvolutionFilter.__init__(self, kernel)



