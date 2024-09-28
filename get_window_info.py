import ctypes
from ctypes import wintypes
import win32gui

# Constants for window enumeration
EnumWindows = ctypes.windll.user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
IsWindowVisible = ctypes.windll.user32.IsWindowVisible
GetWindowRect = ctypes.windll.user32.GetWindowRect

def get_window_list():
    window_list = []

    def foreach_window(hwnd, lParam):
        if IsWindowVisible(hwnd):
            length = GetWindowTextLength(hwnd)
            if length > 0:
                window_title = ctypes.create_unicode_buffer(length + 1)
                GetWindowText(hwnd, window_title, length + 1)
                rect = wintypes.RECT()
                GetWindowRect(hwnd, ctypes.byref(rect))
                window_info = {
                    "title": window_title.value,
                    "bounds": {
                        "left": rect.left,
                        "top": rect.top,
                        "right": rect.right,
                        "bottom": rect.bottom
                    },
                }
                if window_info["title"] == "Astro Duel 2":
                    window_list.append(window_info)
        return True

    EnumWindows(EnumWindowsProc(foreach_window), 0)
    return window_list

def get_window_with_title(title):
    for window in get_window_list():
        if window['title'] == title:
            return window['bounds']
    return None
