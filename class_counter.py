import cv2
import numpy as np


class ColonyCounter:

    def __init__(self, image_path):
        self.image_path = image_path

    def counter_colonies(self):

        image = cv2.imread(self.image_path)

        if image is None:
            raise ValueError(
                f"Unable to read image: {self.image_path}"
            )

        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Reduce noise
        gray = cv2.GaussianBlur(gray, (9, 9), 2)

        # Detect colonies
        circles = cv2.HoughCircles(
            gray,
            cv2.HOUGH_GRADIENT,
            dp=1.2,

            # Increase distance between detected colonies
            minDist=12,

            # Edge detection threshold
            param1=100,

            # Higher value = stricter detection
            param2=19,

            # Expected colony size
            minRadius=3,
            maxRadius=25
        )

        normal = 0

        if circles is not None:
            circles = np.round(circles[0, :]).astype("int")
            normal = len(circles)

        return {
            "normal": normal
        }