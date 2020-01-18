import os
import json
import time
import subprocess
import threading
from sys import platform

ROOT = os.path.dirname(__file__)
DEFAULT_NAME = "myapp"
DEFAULT_PORT= 8080
DEFAULT_WIDTH = 1000
DEFAULT_HEIGHT = 700
DEFAULT_FULLSCREEN = False

class PyNeutralino:
    def __init__(self, app, name=DEFAULT_NAME, port=DEFAULT_PORT, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT, fullscreen=DEFAULT_FULLSCREEN):
        self.app = app
        self.name = name
        self.port = port
        self.width = width
        self.height = height
        self.fullscreen = fullscreen

    def neutralino(self):
        if platform == "linux":
            cmd = "neutralino-linux"
        elif platform == "darwin":
            cmd = "neutralino-mac"
        elif platform == "win32":
            cmd = "neutralino-win.exe"
        else:
            raise Exception("Your platform is not supported")
        cmd = '"%s"' % os.path.join(ROOT, cmd)
        subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read()
        os.remove('./neutralinojs.log') # remove log file

    def _load_config(self, default=False):
        if default:
            appname = DEFAULT_NAME
            appport = DEFAULT_PORT
            width = DEFAULT_WIDTH
            height = DEFAULT_HEIGHT
            fullscreen = DEFAULT_FULLSCREEN
        else:
            appname = self.name
            appport = self.port
            width = self.width
            height = self.height
            fullscreen = self.fullscreen
        settings = {'appname': appname, 'appport': '0', 'mode': 'window', 'window': {'width': str(width), 'height': str(height), 'fullscreen': fullscreen}}
        html = """<!DOCTYPE html>\n<html>\n  <head>\n    <meta charset="UTF-8">\n    <title>PyNeutralino</title>\n    <script>\n      window.location = "http://localhost:{}/"\n    </script>\n  </head>\n  <body>\n  </body>\n</html>""".format(appport)
        html_file = os.path.join(ROOT, 'app/index.html')
        setting_file = os.path.join(ROOT, 'app/settings.json')
        with open(html_file,'w') as f1, open(setting_file,'w') as f2:
            f1.write(html)
            json.dump(settings, f2)

    def run(self):
        self._load_config(False) # set user config
        t1 = threading.Thread(target=lambda:self.app.run(port=self.port), daemon=True)
        t2 = threading.Thread(target=self.neutralino, daemon=True)
        t1.start()
        t2.start()
        while t2.is_alive():
            time.sleep(0.5)
        self._load_config(True) # restore default config