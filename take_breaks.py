import time
import webbrowser

breaks = 3
take_break = 0
print("Current time is: " + time.ctime())
while take_break < breaks:
    time.sleep(2 * 60 * 60)
    print "Now it's a good time to take a break and listen to your favorite music!"
    time.sleep(5)
    webbrowser.open("https://youtu.be/Da5qQD_RpEQ")
    time.sleep(5 * 60)
    print "Break is over, now get back to work!"
    take_break += 1
