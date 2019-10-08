import numpy as np
import cv2
from scipy.ndimage import gaussian_filter


track_window = (0, 0, 20, 20)

# порог saturation и value должен быть больше, чтобы отфильтровать шум от теней и освещения
lower_bound = np.array([0.05, 0.15, 0.15])
upper_bound = np.array([1.0, 1.0, 1.0])

cap = cv2.VideoCapture('bus.avi')
ret, frame = cap.read()
background = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) / 255.0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # вычитаем фон и берем абсолютное значение
    delta = np.abs(cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) / 255.0 - background)
    cv2.imshow('delta #1', delta)
    cv2.moveWindow('delta #1', 100, 100)

    # фильтруем цветовой шум
    delta = cv2.inRange(delta, lower_bound, upper_bound) / 255.0
    cv2.imshow('delta #2', delta)
    cv2.moveWindow('delta #2', 420, 100)

    # размываем изображение, чтобы остались только крупные объекты
    # чем больше sigma, тем больше размытие
    delta = gaussian_filter(delta, 2.5)
    cv2.imshow('delta #3', delta)
    cv2.moveWindow('delta #3', 740, 100)

    # снова фильтруем шум
    delta = cv2.inRange(delta, 0.3, 1) / 255.0
    cv2.imshow('delta #4', delta)
    cv2.moveWindow('delta #4', 1060, 100)

    # определяем границы объекта
    points = np.argwhere(delta > 0)
    if len(points):
        top_left = np.amin(points, 0)[::-1]
        bottom_right = np.amax(points, 0)[::-1]
    else:
        top_left = np.zeros(2)
        bottom_right = np.zeros(2)

    # рисуем результат
    center = 0.5 * (top_left + bottom_right)
    size = bottom_right - top_left
    pts = cv2.boxPoints((center, size, 0.0))
    pts = np.int0(pts)
    image = cv2.polylines(frame, [pts], True, 255, 2)
    cv2.imshow('result', image)
    cv2.moveWindow('result', 580, 400)

    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
