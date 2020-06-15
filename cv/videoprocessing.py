import numpy as np
import cv2

import cv.constants as constants

CaptureProperties = {
    0: 'CV_CAP_PROP_POS_MSEC',
    1: 'CV_CAP_PROP_POS_FRAMES',
    2: 'CV_CAP_PROP_POS_AVI_RATIO',
    3: 'CV_CAP_PROP_FRAME_WIDTH',
    4: 'CV_CAP_PROP_FRAME_HEIGHT',
    5: 'CV_CAP_PROP_FPS',
    6: 'CV_CAP_PROP_FOURCC',
    7: 'CV_CAP_PROP_FRAME_COUNT',
    8: 'CV_CAP_PROP_FORMAT',
    9: 'CV_CAP_PROP_MODE',
    10: 'CV_CAP_PROP_BRIGHTNESS',
    11: 'CV_CAP_PROP_CONTRAST',
    12: 'CV_CAP_PROP_SATURATION',
    13: 'CV_CAP_PROP_HUE',
    14: 'CV_CAP_PROP_GAIN',
    21: 'CV_CAP_PROP_AUTO_EXPOSURE',
    15: 'CV_CAP_PROP_EXPOSURE',
    16: 'CV_CAP_PROP_CONVERT_RGB',
    17: 'CV_CAP_PROP_WHITE_BALANCE',
    20: 'CV_CAP_PROP_SHARPNESS',
    22: 'CV_CAP_PROP_GAMMA',
    32: 'CV_CAP_PROP_BACKLIGHT',
}


def run():
    cap = cv2.VideoCapture(constants.VideoSource)

    print(f'Using video source {constants.VideoSource}')
    for i, prop in CaptureProperties.items():
        print(f'{prop}: {cap.get(i)}')

    ret, frame = cap.read()

    while(True):
        ret, frame = cap.read()
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
