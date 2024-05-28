import cv2

path = r'C:\Users\luciv\OneDrive\Documents\Rastreio\videoTeste.mp4'

rastreador = cv2.TrackerCSRT_create()

video = cv2.VideoCapture(path)

ok, frame = video.read()

bbox = cv2.selectROI(frame)

ok = rastreador.init(frame, bbox)

while True:

    ok, frame = video.read()

    if not ok:
        break
    
    ok, bbox = rastreador.update(frame)

    if ok:

        (x, y, w, h) = [int(v) for v in bbox]

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), 2, 1)

    else:
        cv2.putText(frame, 'Falha ao rastrear', (10,20), 2, 1.2, (0, 255, 0), 2, 1)

    cv2.imshow('Rastreando', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

