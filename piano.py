import cv2
import imutils

from audio import KeyPressManager, load_sound_map, play_note
from collision import PianoKeyCollision
from hand_tracking import HandDetector
from rendering import draw_fingertips, draw_piano, draw_status_overlay


def main():
    sound_map = load_sound_map()
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    detector = HandDetector()
    collision = PianoKeyCollision()
    manager = KeyPressManager()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        img = imutils.resize(frame, width=1280)
        detector.findHands(img)

        fingers = []
        for hand_index in range(detector.handsCount()):
            fingers += detector.getFingerData(hand_index)

        hovered, pressed = collision.check_key_interaction(fingers, img.shape)
        for note in manager.process(pressed):
            play_note(note, sound_map)

        sustained = manager.get_sustained()
        img = draw_piano(img, hovered, pressed, collision)
        draw_fingertips(img, fingers)
        draw_status_overlay(img, detector.handsCount(), pressed, hovered, sustained)

        cv2.imshow("Virtual Piano", img)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
