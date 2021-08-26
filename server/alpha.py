import time

import pantilthat

pantilthat.idle_timeout(0.5)

while True:
    for i in range(0, 180, 5):
        alpha = i-90
        pantilthat.pan(alpha)
        time.sleep(0.3)

