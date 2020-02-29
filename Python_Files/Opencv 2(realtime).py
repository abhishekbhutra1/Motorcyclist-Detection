import cv2

cap = cv2.VideoCapture(0);

ret, frame = cap.read();

while(True):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);
    blur = cv2.GaussianBlur(frame,(5,5), 0);
    cv2.imshow('frame', frame);
    ret1, frame1 = cap.read();

    cv2.imshow('frame1', frame);
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY);
    blur1 = cv2.GaussianBlur(frame1, (5, 5), 0);


    frame2 = cv2.absdiff(blur1,blur);
    cv2.imshow('frame2',frame);
    if cv2.waitKey(1) == ord('q'):
        break

cap.release();
cv2.destroyAllWindows();