import cv2

from piano_layout import BLACK_KEYS, WHITE_KEYS
from utils import format_notes


def draw_piano(img, hovered, pressed, collision):
    start_x, start_y, _ = collision.get_piano_dims(img.shape)

    for index, (note, label) in enumerate(WHITE_KEYS):
        x = start_x + index * collision.white_kw
        color = (255, 255, 255) if note not in pressed else (0, 255, 255)
        cv2.rectangle(
            img,
            (x, start_y),
            (x + collision.white_kw, start_y + collision.white_kh),
            color,
            -1,
        )
        if note in hovered:
            cv2.rectangle(
                img,
                (x, start_y),
                (x + collision.white_kw, start_y + collision.white_kh),
                (255, 0, 0),
                2,
            )
        cv2.putText(
            img,
            label,
            (x + 10, start_y + collision.white_kh - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 0, 0),
            1,
        )

    for note, label, position in BLACK_KEYS:
        x = start_x + int(position * collision.white_kw) - collision.black_kw // 2
        color = (25, 25, 25) if note not in pressed else (0, 255, 0)
        cv2.rectangle(
            img,
            (x, start_y),
            (x + collision.black_kw, start_y + collision.black_kh),
            color,
            -1,
        )
        if note in hovered:
            cv2.rectangle(
                img,
                (x, start_y),
                (x + collision.black_kw, start_y + collision.black_kh),
                (255, 255, 0),
                2,
            )
        cv2.putText(
            img,
            label,
            (x + 5, start_y + collision.black_kh - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.4,
            (255, 255, 255),
            1,
        )

    return img


def draw_fingertips(img, fingers):
    for index, finger in enumerate(fingers):
        cv2.circle(img, (finger["x"], finger["y"]), 8, (0, 255, 0), -1)
        cv2.circle(img, (finger["x"], finger["y"]), 12, (255, 255, 255), 2)
        cv2.putText(
            img,
            str(index + 1),
            (finger["x"] - 5, finger["y"] + 5),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.4,
            (255, 255, 255),
            1,
        )
        cv2.putText(
            img,
            f"{finger['z']:.2f}",
            (finger["x"] - 15, finger["y"] - 15),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.3,
            (255, 255, 255),
            1,
        )


def draw_status_overlay(img, hands_count, pressed, hovered, sustained):
    x0, y0 = 10, 25

    cv2.putText(
        img,
        f"Hands: {hands_count}",
        (x0, y0),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 255),
        2,
    )

    status_rows = [
        ("Pressing", pressed, (0, 255, 0), 30),
        ("Hovering", hovered, (255, 0, 0), 60),
        ("Sustaining", sustained, (0, 255, 255), 90),
    ]

    for label, notes, color, y_offset in status_rows:
        if not notes:
            continue
        cv2.putText(
            img,
            f"{label}: ",
            (x0, y0 + y_offset),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.65,
            color,
            2,
        )
        cv2.putText(
            img,
            format_notes(notes),
            (x0 + 130, y0 + y_offset),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.65,
            color,
            2,
        )
