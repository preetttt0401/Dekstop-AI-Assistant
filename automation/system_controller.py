import os
import subprocess
from datetime import datetime

import pyautogui
import psutil
import pyperclip

from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL

from utils.logger import logger


class SystemController:

    def __init__(self):

        logger.info("System Controller initialized.")

    # --------------------------------------------------

    def shutdown_pc(self):

        try:

            subprocess.Popen("shutdown /s /t 1")

            return True

        except Exception as e:

            logger.error(e)

            return False

    # --------------------------------------------------

    def restart_pc(self):

        try:

            subprocess.Popen("shutdown /r /t 1")

            return True

        except Exception as e:

            logger.error(e)

            return False

    # --------------------------------------------------

    def lock_pc(self):

        try:

            subprocess.Popen("rundll32.exe user32.dll,LockWorkStation")

            return True

        except Exception as e:

            logger.error(e)

            return False

    # --------------------------------------------------

    def take_screenshot(self):

        try:

            folder = "Screenshots"

            os.makedirs(folder, exist_ok=True)

            filename = datetime.now().strftime(
                "screenshot_%Y-%m-%d_%H-%M-%S.png"
            )

            filepath = os.path.join(folder, filename)

            image = pyautogui.screenshot()

            image.save(filepath)

            logger.info(f"Screenshot saved : {filepath}")

            return filepath

        except Exception as e:

            logger.error(e)

            return None
        
            # --------------------------------------------------

    def battery_status(self):

        try:

            battery = psutil.sensors_battery()

            if battery is None:

                return "Battery information is not available."

            percent = int(battery.percent)

            if battery.power_plugged:

                return f"Battery is {percent} percent and the charger is connected."

            return f"Battery is {percent} percent."

        except Exception as e:

            logger.error(e)

            return "Unable to get battery information."
        
        # --------------------------------------------------

    def current_time(self):

        try:

            now = datetime.now()

            return now.strftime("The current time is %I:%M %p.")

        except Exception as e:

            logger.error(e)

            return "Unable to get the current time."

    # --------------------------------------------------

    def current_date(self):

        try:

            today = datetime.now()

            return today.strftime("Today is %A, %d %B %Y.")

        except Exception as e:

            logger.error(e)

            return "Unable to get today's date."
        
        # --------------------------------------------------

    def volume_up(self):

        try:

            devices = AudioUtilities.GetSpeakers()

            interface = devices.Activate(
                IAudioEndpointVolume._iid_,
                CLSCTX_ALL,
                None
            )

            volume = cast(interface, POINTER(IAudioEndpointVolume))

            current = volume.GetMasterVolumeLevelScalar()

            current = min(1.0, current + 0.1)

            volume.SetMasterVolumeLevelScalar(current, None)

            return "Volume increased."

        except Exception as e:

            logger.error(e)

            return "Unable to increase volume."

    # --------------------------------------------------

    def volume_down(self):

        try:

            devices = AudioUtilities.GetSpeakers()

            interface = devices.Activate(
                IAudioEndpointVolume._iid_,
                CLSCTX_ALL,
                None
            )

            volume = cast(interface, POINTER(IAudioEndpointVolume))

            current = volume.GetMasterVolumeLevelScalar()

            current = max(0.0, current - 0.1)

            volume.SetMasterVolumeLevelScalar(current, None)

            return "Volume decreased."

        except Exception as e:

            logger.error(e)

            return "Unable to decrease volume."

    # --------------------------------------------------

    def get_clipboard(self):

        try:

            text = pyperclip.paste()

            if not text:

                return "Clipboard is empty."

            return f"Clipboard contains:\n{text}"

        except Exception as e:

            logger.error(e)

            return "Unable to access clipboard."