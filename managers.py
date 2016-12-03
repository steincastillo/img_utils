

import cv2
import numpy as np 
import time

class CaptureManager(object):
    def __init__(self, capture, previewWindowManager = None, shouldMirrorPreview = False):
        self.previewWindowManager = previewWindowManager
        self.shouldMirrorPreview = shouldMirrorPreview
        self._capture = capture
        self._channel = 0
        self._enteredFrame = False
        self._frame = None
        self._imageFilename = None
        self._videoFilename = None
        self._videoEncoding = None
        self._videoWriter = None

        self._startTime = None
        self._framesElapsed = long(0)
        self._fpsEstimate = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        if self._channel != value:
            self.channel = value
            self._frame = None

    @property
    def frame(self):
        if self._enteredFrame and self._frame is None:
            _, self._frame = self._capture.retrieve()
            return self._frame

    @property
    def isWritingImage (self):
        return self._imageFilename is not None

    @property
    def isWritingVideo(self):
        return self._videoFilename is not None

    def enterFrame(self):
        """Capture the next frame, if anz"""
        #but first, check that any previous frame was exited.
        assert not self._enteredFrame, \‘previous enterFrame() had no matching exitFrame‘
        if self.capture is not None:
            self._enteredFrame = self.capture.grab()

    def exitFrame(self):
        """Draw the window. Write to files. Release the frame."""
        #check wheter anz grabbed fram is retrievable.
        #The getter may retrieve and cache the frame.
        if self.frame is None:
            self._enteredFrame = False
            return

        #Update the FPS estimate and related variables.
        if self._framesElapse == 0:
            self._startTime = time.time()
        else:
            timeElapsed = time.time() - self._startTime
            self._fpsEstimate = self._framesElapsed / timeElapsed
        self._framesElapsed +=1

        #Draw the window, if ana,
        if self.previewWindowManager is not None:
            if self.shouldMirrorPreview:
                mirroedFrame = np.fliplr(self._frame).copy()
                self.previewWindowManager.show(mirroedFrame)
            else:
                self.previewWindowManager.show(self._frame)

        #Write to the image file, if any.
        if self.isWritingImage:
            cv2.imwrite(self._imageFilename, self._frame)
            