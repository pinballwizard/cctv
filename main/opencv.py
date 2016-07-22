import cv2
import datetime as dt
import time

# Зададим параметры работы - как писать, с каким интервалом и куда
record = 'photo'
get_time = 1
record_path = '/home/itadmin/detects/'
text = "AHTUNG!!!"

# Системные переменные, нужны для работы
photo_date = 0
delta_time = 0
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
fgbg = cv2.createBackgroundSubtractorMOG2()
firstFrame = None


# Функция "сделать фоточку" с датой в png формате
def take_a_photo(src):
    params = list()
    params.append(cv2.IMWRITE_PNG_COMPRESSION )
    params.append(100)
    cv2.imwrite('%sdetect at %s.png' %(record_path, cur_date), src, params)

# Функция "сделать видео" с датой в png формате
def take_a_video(src):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('%soutput %s.avi' %(record_path, cur_date), fourcc, 20.0, (640, 480))
    out.write(src)

# Указываем источник видеопотока
camera = cv2.VideoCapture(0)

while True:
# Считываем кадр и извлекаем задний фон
    firstFrame, frame = camera.read()
    fgmask = fgbg.apply(frame)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
# Определяем область интересов
    frameDelta = cv2.absdiff(firstFrame, fgmask)
    thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)
# Обводим ее в зеленый прямоугольник и пишем похабные надписи
    (_, cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in cnts:
        if cv2.contourArea(c) < 600:
            continue
        (x,y,w,h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cur_date = dt.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        cv2.putText(frame, "Room Status: {}".format(text), (10, 25), cv2.FONT_ITALIC, 0.7, (0, 0, 255), 1)
        cv2.putText(frame, "Time when detected: {}".format(cur_date), (10, 55), cv2.FONT_ITALIC, 0.65, (0, 255, 255), 1)

# Отсчитываем get_time секунд, перед тем как сделать новую фотку
        if record == 'photo':
            cdate = time.time()
            delta_time = cdate - photo_date
            if delta_time > get_time:
                take_a_photo(frame)
                photo_date = time.time()
            else:
                continue
        # надо переписать чтобы делал видеопоток, а не писал конкретный кадр в видео\сек
        elif record == 'video':
            cdate = time.time()
            delta_time = cdate - photo_date
            if delta_time > get_time:
                take_a_video(frame)
                photo_date = time.time()
            else:
                continue

# Выведем картинку на экран
    #cv2.imshow("In grayscale mask", fgmask)
    cv2.imshow("In grayscale with thresh", thresh)
    #cv2.imshow("DeltaFrame", frameDelta)
    cv2.imshow("Security Feed", frame)

# Ждем кнопку q для выхода из цикла
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# Освобождаем камеру, убиваем окна
camera.release()
cv2.destroyAllWindows()
