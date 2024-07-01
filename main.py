import pyautogui
import recognizing
import cv2
import numpy as np
from time import time

ryu_img = cv2.imread("./assets/ryu.png", cv2.COLOR_RGB2BGR)
gray_bot = cv2.imread("./assets/gray_bot.png", cv2.COLOR_RGB2BGR)

def main():
    loop_time = time()
    while True:
        window_info = recognizing.get_window_with_title("Astro Duel 2")
        region = (window_info['X'], window_info['Y'],
                  window_info['Width'], window_info['Height'])

        screenshot = pyautogui.screenshot(region=region)
        screenshot = np.array(screenshot)
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

        result = cv2.matchTemplate(screenshot, gray_bot, cv2.TM_SQDIFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        needle_w = gray_bot.shape[1]
        needle_h = gray_bot.shape[0]

        top_left = min_loc
        bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)

        cv2.rectangle(screenshot, top_left, bottom_right, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_4)

        cv2.imshow("Computer Vision", screenshot)

        # print("FPS {}".format(1 / (time() - loop_time)))
        if cv2.waitKey(1) == ord('q'):
            cv2.destroyAllWindows()
            break

        # print("Done")

main()