# -*- coding: utf-8 -*-
"""
Created on Sun Dec 04 14:48:18 2016

@author: Stein

usage:
python cameo.py
"""

import cv2
import filters
from managers import WindowManager, CaptureManager

class Cameo(object):
    
    def __init__(self):
        self._windowManager = WindowManager('Cameo',
                                             self.onKeypress)
        self._captureManager = CaptureManager(
            cv2.VideoCapture(0), self._windowManager, True)
        #self._curveFilter = filters.BGRPortraCurveFilter()
        self._EmbossFilter = filters.EmbossFilter()
        self._SharpenFilter = filters.SharpenFilter()
        self._AverageBlur = filters.AverageBlur()
        self._FindEdgesFilger = filters.FindEdgesFilter()
    
    def run(self):
        """Run the main loop."""
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame
            
            # TODO: Filter the frame (Chapter 3).
            #filters.bnw(frame, frame)
            #filters.strokeEdges(frame, frame)
            #self._EmbossFilter.apply(frame, frame)
            #self._curveFilter.apply(frame, frame)
            #self._SharpenFilter.apply(frame, frame)
            #self._AverageBlur.apply(frame, frame)
            self._FindEdgesFilger.apply(frame, frame)
            
            self._captureManager.exitFrame()
            self._windowManager.processEvents()
    
    def onKeypress(self, keycode):
        """Handle a keypress.
        
        space  -> Take a screenshot.
        tab    -> Start/stop recording a screencast.
        escape -> Quit.
        
        """
        if keycode == 32: # space
            self._captureManager.writeImage('screenshot.png')
        elif keycode == 9: # tab
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo(
                    'screencast.avi')
            else:
                self._captureManager.stopWritingVideo()
        elif keycode == 27: # escape
            self._windowManager.destroyWindow()

if __name__=="__main__":
    print("\n")
    print("**************************************")
    print("* CAMEO")
    print("*")
    print("* Version: 1.0")
    print("**************************************")
    print("\n")
    print ("Press [space] to take a screenshot")
    print ("Press [tab] to start/stop recording a screencast")
    print ("Press [esc] to quit")

    Cameo().run()