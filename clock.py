import display
import unicornhathd
import datetime
import time

try:

    while True:
        now = datetime.datetime.now()
        display.display(now.hour, now.minute)
        time.sleep(30)

except KeyboardInterrupt:
    unicornhathd.off()

finally:
    unicornhathd.off()
