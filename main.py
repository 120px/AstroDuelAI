import get_window_info
from vision_module import Vision
from location_module import Location
from astroduelenv import AstroDuelEnv
import cv2
import pyautogui
import numpy as np
from time import time


def init_assets():
    ryu_img = cv2.imread("./assets/ryu.png", cv2.COLOR_RGB2BGR)
    gray_bot = cv2.imread("./assets/gray_bot.png", cv2.COLOR_RGB2BGR)
    assets = {"ryu_img": ryu_img, "gray_bot": gray_bot}
    return assets

def main():
    assets = init_assets()
    loop_time = time()

    vision = Vision()
    location = Location()
    env = AstroDuelEnv()
    state = env.reset()

    for _ in range(5):
        action = env.action_space.sample()
        if action == 0:
            pyautogui.press('left')
        elif action == 1:
            pyautogui.press('right')
        elif action == 2:
            pyautogui.press('up')
        elif action == 3:
            pyautogui.press('down')
        # print(action)
        observation, reward, terminated, info, = env.step(action)
        # print("State:", state, "Reward:", reward, "Done:", terminated)


    while True:
        window_info = get_window_info.get_window_with_title("Astro Duel 2")
        print(window_info)
        region = (window_info['left'], window_info['top'],
                  window_info['Width'], window_info['Height'])

        screenshot = pyautogui.screenshot(region=region)
        screenshot = np.array(screenshot)
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

        result_locate_player = vision.locate_player(game_screenshot=screenshot, player_img=assets["ryu_img"])
        # result_locate_enemy = vision.locate_enemies(game_screenshot=screenshot, enemy=assets["gray_bot"])

        player_locations = location.get_locations(object_to_locate=result_locate_player)
        # enemy_locations = location.get_locations(object_to_locate=result_locate_enemy)

        needle_w = assets["ryu_img"].shape[1]
        needle_h = assets["ryu_img"].shape[0]

        top_left = player_locations['min_loc']
        bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)

        cv2.rectangle(screenshot, top_left, bottom_right, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_4)

        cv2.imshow("Computer Vision", screenshot)

        # print("FPS {}".format(1 / (time() - loop_time)))
        if cv2.waitKey(1) == ord('q'):
            cv2.destroyAllWindows()
            break

        # print("Done")

main()