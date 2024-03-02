import threading
import winsound
import cv2
import imutils
from twilio.rest import Client
import time

# Twilio credentials
account_sid = 'your_actual_account_sid'
auth_token = 'your_actual_auth_token'
twilio_phone_number = 'your_actual_twilio_phone_number'
recipient_phone_number = 'your_actual_recipient_phone_number'

client = Client(account_sid, auth_token)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
_, start_frame = cap.read()
start_frame = imutils.resize(start_frame, width=500)
start_frame = cv2.cvtColor(start_frame, cv2.COLOR_BGR2GRAY)
start_frame = cv2.GaussianBlur(start_frame, (21, 21), 0)

alarm = False
alarm_mode = False
alarm_counter = 0

last_alert_time = 0
cooldown_duration = 300 

def beep_alarm():
    global alarm
    for _ in range(5):
        if not alarm_mode:
            break
        print('ALARM')
        winsound.Beep(2500, 1000)
    alarm = False

def send_sms_alert():
    global last_alert_time
    current_time = time.time()
    if current_time - last_alert_time >= cooldown_duration:
        message = client.messages.create(
            body='Motion detected! Check the surveillance system.',
            from_=twilio_phone_number,
            to=destination_phone_number
        )
        print(f"SMS sent: {message.sid}")
        last_alert_time = current_time
    else:
        print("Cooldown period active. Skipping message.")

while True:
    _, frame = cap.read()
    frame = imutils.resize(frame, width=500)

    if alarm_mode:
        frame_bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_bw = cv2.GaussianBlur(frame_bw, (5, 5), 0)

        difference = cv2.absdiff(frame_bw, start_frame)
        threshold = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)[1]
        start_frame = frame_bw

        if threshold.sum() > 300:
            alarm_counter += 1
            if alarm_counter > 10:  # Adjust the threshold as needed
                send_sms_alert()
        else:
            if alarm_counter > 0:
                alarm_counter -= 1
        cv2.imshow("Cam", threshold)
    else:
        cv2.imshow("cam", frame)

    if alarm_counter > 20:
        if not alarm:
            alarm = True
            threading.Thread(target=beep_alarm).start()

    key_pressed = cv2.waitKey(30)
    if key_pressed == ord('t'):
        alarm_mode = not alarm_mode
        alarm_counter = 0
    if key_pressed == ord("q"):
        alarm_mode = False
        break

cap.release()
cv2.destroyAllWindows()
