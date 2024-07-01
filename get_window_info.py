import cv2
import os
import numpy as np
import pyautogui
from time import time
from PIL import ImageGrab, Image
import Quartz

def get_window_list():
    window_list = []
    window_info_list = Quartz.CGWindowListCopyWindowInfo(Quartz.kCGWindowListOptionOnScreenOnly, Quartz.kCGNullWindowID)
    for window_info in window_info_list:
        window_list.append(window_info)
    return window_list

def get_window_with_title(title):
    for window in get_window_list():
        window_title = window.get('kCGWindowName', 'No Title')
        if window_title == title:
            return window['kCGWindowBounds']
    return None