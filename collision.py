from piano_layout import BLACK_KEYS, WHITE_KEYS


class PianoKeyCollision:
    def __init__(self):
        self.white_kw = 55
        self.white_kh = 300
        self.black_kw = 33
        self.black_kh = 140
        self.hover_zone = 70
        self.bend_thresh = 3

    def get_piano_dims(self, img_shape):
        total = len(WHITE_KEYS) * self.white_kw
        start_x = (img_shape[1] - total) // 2
        start_y = img_shape[0] - self.white_kh - 80
        return start_x, start_y, total

    def point_in_rect(self, x, y, rect):
        x1, y1, x2, y2 = rect
        return x1 <= x <= x2 and y1 <= y <= y2

    def check_key_interaction(self, fingers, img_shape):
        hovered = set()
        pressed = set()
        start_x, start_y, _ = self.get_piano_dims(img_shape)

        for finger in fingers:
            x, y = finger["x"], finger["y"]
            bent = (y - finger["pip_y"]) > self.bend_thresh

            if not (start_y - self.hover_zone <= y <= start_y + self.white_kh):
                continue

            hit_black_key = False
            for note, _, position in BLACK_KEYS:
                key_x = start_x + int(position * self.white_kw) - self.black_kw // 2
                hover_rect = (
                    key_x,
                    start_y - self.hover_zone,
                    key_x + self.black_kw,
                    start_y + self.black_kh,
                )
                press_rect = (
                    key_x,
                    start_y,
                    key_x + self.black_kw,
                    start_y + self.black_kh,
                )

                if self.point_in_rect(x, y, hover_rect):
                    hovered.add(note)
                    if bent and self.point_in_rect(x, y, press_rect):
                        pressed.add(note)
                    hit_black_key = True
                    break

            if hit_black_key:
                continue

            for index, (note, _) in enumerate(WHITE_KEYS):
                key_x = start_x + index * self.white_kw
                hover_rect = (
                    key_x + 2,
                    start_y - self.hover_zone,
                    key_x + self.white_kw - 2,
                    start_y + self.white_kh,
                )
                press_rect = (
                    key_x + 2,
                    start_y,
                    key_x + self.white_kw - 2,
                    start_y + self.white_kh,
                )

                if self.point_in_rect(x, y, hover_rect):
                    hovered.add(note)
                    if bent and self.point_in_rect(x, y, press_rect):
                        pressed.add(note)
                    break

        return list(hovered), list(pressed)
