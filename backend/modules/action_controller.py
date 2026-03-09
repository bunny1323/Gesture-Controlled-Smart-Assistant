import pyautogui
import json
import os

class ActionController:
    def __init__(self, config_path='database/gesture_actions.json'):
        self.config_path = config_path
        self.actions = {
            'play_pause': lambda: pyautogui.press('space'),
            'next_slide': lambda: pyautogui.press('right'),
            'prev_slide': lambda: pyautogui.press('left'),
            'volume_up': lambda: pyautogui.press('volumeup'),
            'volume_down': lambda: pyautogui.press('volumedown'),
            'scroll_up': lambda: pyautogui.scroll(300),
            'scroll_down': lambda: pyautogui.scroll(-300),
            'stop_engine': lambda: print("Stopping engine signal...")
        }
        pyautogui.FAILSAFE = True

    def trigger(self, action_key):
        if action_key in self.actions:
            print(f"Executing System Action: {action_key}")
            self.actions[action_key]()
            return True
        return False

    def get_supported_actions(self):
        return list(self.actions.keys())
