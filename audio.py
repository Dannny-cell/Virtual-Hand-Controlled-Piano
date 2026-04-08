import os
import time

import simpleaudio as sa


DEFAULT_SAMPLES_DIR = r"D:\piano_wav"


def load_sound_map(samples_dir=DEFAULT_SAMPLES_DIR):
    sound_map = {}
    if not os.path.exists(samples_dir):
        return sound_map

    for filename in os.listdir(samples_dir):
        if not filename.lower().endswith(".wav"):
            continue

        note = os.path.splitext(filename)[0].lower()
        file_path = os.path.join(samples_dir, filename)

        try:
            sound_map[note] = sa.WaveObject.from_wave_file(file_path)
        except Exception:
            continue

    return sound_map


def play_note(note, sound_map):
    for variant in (note, note.lower(), note.upper()):
        sound = sound_map.get(variant)
        if not sound:
            continue

        try:
            sound.play()
        except Exception:
            pass
        break


class KeyPressManager:
    def __init__(self):
        self.prev = set()
        self.times = {}
        self.debounce = 0.05
        self.sustain_time = 0.3
        self.sustained = {}

    def process(self, current_notes):
        now = time.time()
        new_keys = set(current_notes) - self.prev
        notes_to_play = []

        for key in new_keys:
            if now - self.times.get(key, 0) >= self.debounce:
                self.times[key] = now
                notes_to_play.append(key)

        released = self.prev - set(current_notes)
        for key in released:
            self.sustained[key] = now

        self.prev = set(current_notes)
        self.cleanup_sustain(now)
        return notes_to_play

    def cleanup_sustain(self, now):
        expired = [
            key for key, released_at in self.sustained.items()
            if now - released_at > self.sustain_time
        ]
        for key in expired:
            del self.sustained[key]

    def get_sustained(self):
        return list(self.sustained.keys())
