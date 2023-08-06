# OpenCVZone


This is a Computer vision package that makes its easy to run Image processing and AI functions. At the core it uses [OpenCV](https://github.com/opencv/opencv) and [Mediapipe](https://github.com/google/mediapipe) libraries. 

## Installation
You can  simply use pip to install the latest version of cvzone.

`pip install opencvzone`

<hr>

### 60 FPS Face Detection

<hr>

<p align="center">
  <img width="640" height="360" src="https://www.computervision.zone/wp-content/uploads/2021/05/Face-Detection-2.jpg">
</p>

<pre>
import opencvzone
import cv2

cap = cv2.VideoCapture(0)
detector = opencvzone.FaceDetector()

while True:
    success, img = cap.read()
    img, bboxs = detector.findFaces(img)
    print(bboxs)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
</pre>

<hr>

### Hand Tracking

<hr>

<p align="center">
  <img width="640" height="360" src="https://github.com/cvzone/cvzone/blob/master/Results/Fingers-Distance.jpg">
</p>

#### Basic Code Example 
<pre>
import opencvzone
import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = opencvzone.HandDetector(detectionCon=0.5, maxHands=1)

while True:
    # Get image frame
    success, img = cap.read()

    # Find the hand and its landmarks
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    
    # Display
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
</pre>

#### Finding How many finger are up
<pre>
if lmList:
        # Find how many fingers are up
        fingers = detector.fingersUp()
        totalFingers = fingers.count(1)
        cv2.putText(img, f'Fingers:{totalFingers}', (bbox[0] + 200, bbox[1] - 30),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
</pre>

#### Finding distace between two fingers
<pre>                 
if lmList:
        # Find Distance Between Two Fingers
        distance, img, info = detector.findDistance(8, 12, img)
        cv2.putText(img, f'Dist:{int(distance)}', (bbox[0] + 400, bbox[1] - 30),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
</pre>

#### Find Hand Type - i.e. Left or Right 
<p align="center">
  <img width="320" height="180" src="https://github.com/cvzone/cvzone/blob/master/Results/LeftHand.jpg"> <img width="320" height="180" src="https://github.com/cvzone/cvzone/blob/master/Results/RightHand.jpg">
</p>



<pre>
if lmList:
        # Find Hand Type
        myHandType = detector.handType()
        cv2.putText(img, f'Hand:{myHandType}', (bbox[0], bbox[1] - 30),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

</pre>

<hr>

### Pose Estimation

<hr>

<p align="center">
  <img width="640" height="360" src="https://www.computervision.zone/wp-content/uploads/2021/04/vlcsnap-2021-03-27-22h34m51s546.jpg">
</p>

<pre>
import opencvzone
import cv2

cap = cv2.VideoCapture(0)
detector = opencvzone.PoseDetector()
while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList = detector.findPosition(img, draw=False)
    if lmList:
        print(lmList[14])
        cv2.circle(img, (lmList[14][1], lmList[14][2]), 15, (0, 0, 255), cv2.FILLED)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

</pre>


<hr>

### Face Mesh Detection

<hr>

<p align="center">
  <img width="640" height="360" src="https://www.computervision.zone/wp-content/uploads/2021/05/Face-Landmarks-2.jpg">
</p>

<pre>
import opencvzone
import cv2

cap = cv2.VideoCapture(0)
detector = opencvzone.FaceMeshDetector(maxFaces=2)
while True:
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img)
    if faces:
        print(faces[0])
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
</pre>

<hr>

### Stack Images

<hr>

<p align="center">
  <img width="640" height="360" src="https://github.com/cvzone/cvzone/blob/master/Results/ImageStack1.gif">
</p>

<pre>
import opencvzone
import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgList = [img, img, imgGray, img, imgGray, img,imgGray, img, img]
    stackedImg = opencvzone.stackImages(imgList, 3, 0.4)

    cv2.imshow("stackedImg", stackedImg)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

</pre>

<hr>

### Corner Rectangle

<hr>

<p align="center">
  <img width="640" height="360" src="https://github.com/cvzone/cvzone/blob/master/Results/cornerRect.jpg">
</p>

<hr>

<pre>
import opencvzone
import cv2

cap = cv2.VideoCapture(0)
detector = opencvzone.HandDetector()

while True:
    # Get image frame
    success, img = cap.read()

    # Find the hand and its landmarks
    img = detector.findHands(img, draw=False)
    lmList, bbox = detector.findPosition(img, draw=False)
    if bbox:
        # Draw  Corner Rectangle
        cvzone.cornerRect(img, bbox)

    # Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)
</pre>

### FPS

<hr>

<p align="center">
  <img width="640" height="360" src="https://github.com/cvzone/cvzone/blob/master/Results/FPS.jpg">
</p>

<pre>
import opencvzone
import cv2

fpsReader = opencvzone.FPS()
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

while True:
    success, img = cap.read()
    fps, img = fpsReader.update(img,pos=(50,80),color=(0,255,0),scale=5,thickness=5)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
</pre>


### Gesture Volume Control

<hr>

<p align="center">
  <img width="640" height="360" src="https://github.com/cvzone/cvzone/blob/master/Results/FPS.jpg">
</p>

<pre>
import opencvzone
import cv2
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

wCam, hCam = 640, 480

cap = cv2.VideoCapture(1)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = opencvzone.HandDetector(detectionCon=0.5, maxHands=1)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volBar = 400
volPer = 0
area = 0
colorVol = (255, 0, 0)

while True:
    success, img = cap.read()

    # Find Hand
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img, draw=True)
    if len(lmList) != 0:

        # Filter based on size
        area = (bbox[2] - bbox[0]) * (bbox[3] - bbox[1]) // 100
        # print(area)
        if 250 < area < 1000:

            # Find Distance between index and Thumb
            length, img, lineInfo = detector.findDistance(4, 8, img)
            # print(length)

            # Convert Volume
            volBar = np.interp(length, [50, 200], [400, 150])
            volPer = np.interp(length, [50, 200], [0, 100])

            # Reduce Resolution to make it smoother
            smoothness = 10
            volPer = smoothness * round(volPer / smoothness)

            # Check fingers up
            fingers = detector.fingersUp()
            # print(fingers)

            # If pinky is down set volume
            if not fingers[4]:
                volume.SetMasterVolumeLevelScalar(volPer / 100, None)
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                colorVol = (0, 255, 0)
            else:
                colorVol = (255, 0, 0)

    # Drawings
    cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
    cv2.putText(img, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX,1, (255, 0, 0), 3)
    cVol = int(volume.GetMasterVolumeLevelScalar() * 100)
    cv2.putText(img, f'Vol Set: {int(cVol)}', (400, 50), cv2.FONT_HERSHEY_COMPLEX,1, colorVol, 3)

    # Frame rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX,1, (255, 0, 0), 3)

    cv2.imshow("Img", img)
    cv2.waitKey(1)
</pre>
