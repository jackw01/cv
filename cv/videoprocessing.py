import math
import logging
from colorama import init, Fore, Style
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


def run(args):
    init()
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s.%(msecs)03dZ %(levelname)s: %(message)s',
                        datefmt='%Y-%m-%dT%H:%M:%S')

    logging.addLevelName(logging.CRITICAL, Fore.RED + 'critical' + Style.RESET_ALL)
    logging.addLevelName(logging.ERROR, Fore.RED + 'error' + Style.RESET_ALL)
    logging.addLevelName(logging.WARNING, Fore.YELLOW + 'warn' + Style.RESET_ALL)
    logging.addLevelName(logging.INFO, Fore.GREEN + 'info' + Style.RESET_ALL)

    cap = cv2.VideoCapture(args.video_source, cv2.CAP_DSHOW)
    cap.set(3, args.width)
    cap.set(4, args.height)

    logging.info(f'Using video source {args.video_source}')
    for i, prop in CaptureProperties.items():
        logging.info(f'{prop}: {cap.get(i)}')

    horizontal_fov = math.degrees(math.atan(
        math.tan(math.radians(args.diagonal_fov) / 2)
        * args.width / math.hypot(args.width, args.height)) * 2)
    logging.info(f'Calculated horizontal FOV: {horizontal_fov}')

    last_status = True
    while(True):
        ret, frame = cap.read()
        if ret:
            cv2.imshow('Video', frame)
        elif ret != last_status:
            logging.warn('Video stream lost')

        last_status = ret

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
