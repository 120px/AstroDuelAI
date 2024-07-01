import cv2

class Location:
    def get_locations(self, object_to_locate):
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(object_to_locate)
        values = {"min_val": min_val, "max_val": max_val, "min_loc": min_loc, "max_loc": max_loc}
        return values