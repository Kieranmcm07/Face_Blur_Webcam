# Cool face blurring script using OpenCV and dlib
# By Kieranmcm07


# Libraries Imports

import cv2
from colorama import init, Fore, Style

init(autoreset=True)

print(Fore.YELLOW + "Loading face detector...")
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

print(Fore.YELLOW + "Starting webcam...")
camera = cv2.VideoCapture(0)

last_face_count = -1

while True:
    ret, frame = camera.read()
    if not ret:
        print(Fore.RED + "Failed to grab frame.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Only print when face count changes
    if len(faces) != last_face_count:
        print(Fore.CYAN + f"Found {len(faces)} face(s).")
        last_face_count = len(faces)

    for (x, y, w, h) in faces:
        # Make the blur box a bit bigger
        pad = int(0.15 * w)
        x1 = max(x - pad, 0)
        y1 = max(y - pad, 0)
        x2 = min(x + w + pad, frame.shape[1])
        y2 = min(y + h + pad, frame.shape[0])
        face_region = frame[y1:y2, x1:x2]
        blurred = cv2.GaussianBlur(face_region, (99, 99), 30)
        frame[y1:y2, x1:x2] = blurred

    # Add exit instruction text
    cv2.putText(
        frame,
        "Press 'q' to exit",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 255),
        2,
        cv2.LINE_AA
    )

    cv2.imshow("Face Blur", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print(Fore.GREEN + "Exiting...")
        break

camera.release()
cv2.destroyAllWindows()
print(Fore.GREEN + "Camera released and windows closed.")