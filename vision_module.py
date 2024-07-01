import cv2

class Vision:

    def __int__(self):
        pass

    def locate_player(self, game_screenshot, player_img):
        result = cv2.matchTemplate(game_screenshot, player_img, cv2.TM_SQDIFF_NORMED)
        return result

    def locate_enemies(self, game_screenshot, enemy):
        result = cv2.matchTemplate(game_screenshot, enemy, cv2.TM_SQDIFF_NORMED)
        return result

    def locate_weapons(self, weapons):
        pass
