import cv2
import time
import PostEstimationModule as pem
from pynput.keyboard import Key, Controller
import pygetwindow as gw
import pyautogui

def focus_game_window(window_title):
    windows = gw.getWindowsWithTitle(window_title)
    if windows:
        windows[0].activate()
    else:
        print(f"Window with title '{window_title}' not found.")

def main():
    cap = cv2.VideoCapture(0)
    detector = pem.poseDetector()
    keyboard = Controller()
    counter = 0
    window_title = "Temple Run"  # Adjust this to match the exact window title of the game

    while True:
        success, img = cap.read()
        img = cv2.resize(img, (750, 550))
        img = cv2.flip(img, 1)
        detector.findPose(img, draw=False)
        lmList = detector.getPosition(img, draw=False)
        if lmList:
            p1, p2 = lmList[1][1:], lmList[23][1:]
            left, right = lmList[18][1:], lmList[19][1:]
            l, _, _ = detector.findDistance(p1, p2)
            l1, _, _ = detector.findDistance(left, right)

            focus_game_window(window_title)  # Ensure game window is focused

            if l1 < 80:
                if counter == 0:
                    print("Up key pressed")
                    keyboard.press(Key.up)
                    keyboard.release(Key.up)
                    time.sleep(0.1)  # Add delay
            if p1[1] > 250:
                if counter == 0:
                    print("Down key pressed")
                    keyboard.press(Key.down)
                    keyboard.release(Key.down)
                    time.sleep(0.1)  # Add delay
            if left[0] < 150:
                print("Left key pressed")
                keyboard.press(Key.left)
                keyboard.release(Key.left)
                time.sleep(0.1)  # Add delay
            if right[0] > 600:
                print("Right key pressed")
                keyboard.press(Key.right)
                keyboard.release(Key.right)
                time.sleep(0.1)  # Add delay
            counter += 1
        if counter == 11:
            counter = 0
        cv2.imshow("Temple Run", img)
        cv2.waitKey(1)

if __name__ == '__main__':
    main()
