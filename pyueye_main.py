#!/usr/bin/env python

from pyueye import ueye
from pyueye_camera import Camera
from pyueye_utils import FrameThread

import time

import cv2
import numpy as np

def main():

    # camera class to simplify uEye API access
    cam = Camera()
    cam.init()
#    cam.set_colormode(ueye.IS_CM_BGR8_PACKED)
#    cam.set_aoi(0,0, 640, 480)

    cam.alloc()
    cam.capture_video()

    # a thread that waits for new images and processes all connected views
    thread = FrameThread(cam)
    thread.start()

    time.sleep(60) 

    thread.stop()
    thread.join()

    cam.stop_video()
    cam.exit()

if __name__ == "__main__":
    main()


