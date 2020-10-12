# import math
# 上滑手机屏幕

import subprocess
import time
import os
import shutil
for i in range(0,10000):
    os.system("adb shell input swipe 750 250 250 500 50")

