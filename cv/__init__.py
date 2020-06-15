import argparse
import cv.videoprocessing as videoprocessing


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--video_source', type=int, default=0,
                        help='Video source')
    parser.add_argument('--width', type=int, default=1280,
                        help='Video width')
    parser.add_argument('--height', type=int, default=720,
                        help='Video height')
    parser.add_argument('--diagonal_fov', type=int, default=68.5,
                        help='Diagonal FOV of camera in degrees')
    args = parser.parse_args()

    videoprocessing.run(args)
