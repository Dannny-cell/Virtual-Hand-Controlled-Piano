import cv2
import mediapipe as mp


class HandDetector:
    def __init__(self, maxHands=2, detectionCon=0.7, trackCon=0.7):
        if not hasattr(mp, "solutions") or not hasattr(mp.solutions, "hands"):
            version = getattr(mp, "__version__", "unknown")
            raise RuntimeError(
                "This project uses MediaPipe's legacy Solutions API "
                "(`mp.solutions.hands`), but the installed mediapipe package "
                f"does not provide it. Detected mediapipe version: {version}. "
                "Install the compatible dependency set with "
                "`pip install -r requirements.txt` or reinstall "
                "`mediapipe==0.10.21` in your virtual environment."
            )

        self.hands = mp.solutions.hands.Hands(
            static_image_mode=False,
            max_num_hands=maxHands,
            min_detection_confidence=float(detectionCon),
            min_tracking_confidence=float(trackCon),
        )
        self.mpDraw = mp.solutions.drawing_utils
        self.results = None
        self.img_h = 0
        self.img_w = 0

    def findHands(self, img, draw=True):
        self.img_h, self.img_w = img.shape[:2]
        image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(image_rgb)

        if self.results.multi_hand_landmarks and draw:
            for landmarks in self.results.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(
                    img,
                    landmarks,
                    mp.solutions.hands.HAND_CONNECTIONS,
                    landmark_drawing_spec=self.mpDraw.DrawingSpec((0, 255, 0), 2, 3),
                    connection_drawing_spec=self.mpDraw.DrawingSpec((0, 255, 0), 2, 2),
                )
        return img

    def handsCount(self):
        if not self.results or not self.results.multi_hand_landmarks:
            return 0
        return len(self.results.multi_hand_landmarks)

    def getFingerData(self, handNo=0):
        fingers = []
        if not self.results or not self.results.multi_hand_landmarks:
            return fingers
        if len(self.results.multi_hand_landmarks) <= handNo:
            return fingers

        landmarks = self.results.multi_hand_landmarks[handNo]
        pip_map = {4: 3, 8: 6, 12: 10, 16: 14, 20: 18}

        for tip_id, pip_id in pip_map.items():
            tip = landmarks.landmark[tip_id]
            pip = landmarks.landmark[pip_id]
            fingers.append(
                {
                    "tip_id": tip_id,
                    "x": int(tip.x * self.img_w),
                    "y": int(tip.y * self.img_h),
                    "pip_x": int(pip.x * self.img_w),
                    "pip_y": int(pip.y * self.img_h),
                    "z": tip.z,
                }
            )
        return fingers
