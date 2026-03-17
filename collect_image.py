import os
import cv2

DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 18
dataset_size = 100

#  FIXED CAMERA INDEX
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

#  Check camera opened
if not cap.isOpened():
    print(" Cannot access camera")
    exit()

for j in range(number_of_classes):
    class_path = os.path.join(DATA_DIR, str(j))
    if not os.path.exists(class_path):
        os.makedirs(class_path)

    print('Collecting data for class {}'.format(j))

    #  WAIT SCREEN
    while True:
        ret, frame = cap.read()

        if not ret:
            print(" Cannot grab frame")
            continue

        cv2.putText(frame, 'Ready? Press "Q" ! :)',
                    (100, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.3,
                    (0, 255, 0),
                    3,
                    cv2.LINE_AA)

        cv2.imshow('frame', frame)

        if cv2.waitKey(25) == ord('q'):
            break

    #  DATA COLLECTION
    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()

        if not ret:
            print(" Cannot grab frame")
            continue

        cv2.imshow('frame', frame)
        cv2.waitKey(25)

        cv2.imwrite(os.path.join(class_path, f'{counter}.jpg'), frame)

        counter += 1

cap.release()
cv2.destroyAllWindows()