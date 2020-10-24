import time

import cv2
import notify2 as notify2
import numpy as np
import pyautogui
import requests
import threading

def exchange_call():
    data = requests.get('http://api.currencies.zone/v1/quotes/USD/EUR/json?quantity=10&key=5050|6sHk8hUxpWQ~NeWrP6WbKRN50exTXAg7')
    return data.json()['result']['value']


def exchange():
    notify2.init('EUR USD Exchange')
    notify2.Notification("Exchangerate USD EUR",
                         str(exchange_call()),
                         '/icons/kasse.png'
                         ).show()


def webmail_call():
    url = 'https://web-mail.uibk.ac.at/imp/redirect.php'
    values = {'imapuser': 'csaz2114',
              'pass': 'lepitu86'}
    with requests.Session() as s:
        p = s.post(url, data=values)
        r = s.get('https://web-mail.uibk.ac.at/imp/login.php?frameset_loaded=1')
        if r.text.coudnt('class="unseen"') > 0:
            notify2.init('Uni Postfach')
            notify2.Notification("Uni Postfach",
                                 'Eine neue Email im Uni Postfach ist verfügbar').show()

def webmail():
    while True:
        webmail_call()
        time.sleep(18000)

threading.Thread(target=exchange())
threading.Thread(target=webmail())

# def record():
#     SCREEN_SIZE = (1920, 1080)
#     fourcc = cv2.VideoWriter_fourcc(*"XVID")
#     out = cv2.VideoWriter("output.avi", fourcc, 20.0, (SCREEN_SIZE))
#
#     while True:
#         # make a screenshot
#         img = pyautogui.screenshot()
#         # convert these pixels to a proper numpy array to work with OpenCV
#         frame = np.array(img)
#         # convert colors from BGR to RGB
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         # write the frame
#         out.write(frame)
#         # show the frame
#         cv2.imshow("screenshot", frame)
#         # if the user clicks q, it exits
#         if cv2.waitKey(1) == ord("q"):
#             break
#
#     # make sure everything is closed when exited
#     cv2.destroyAllWindows()
#     out.release()
#     img = pyautogui.screenshot(region=(0, 0, 300, 400))
#
# record()






#News API Key
#3d1bf078202a45a99a8bac7cfd3e3a00
