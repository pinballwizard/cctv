import cv2
import datetime as dt
import time

class videocam(object):
    firstFrame = None

    def __init__(self, rec_src, rec_type, rec_int, rec_path, alarm_text):
        self.rec_src = rec_src
        self.rec_type = rec_type
        self.rec_int = rec_int
        self.rec_path = rec_path
        self.alarm_text = alarm_text

    def take_a_photo(self):
        params = list()
        params.append(cv2.IMWRITE_PNG_COMPRESSION)
        params.append(100)
        cur_date = dt.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        cv2.imwrite('{0}detect at {1}.png'.format(self.rec_path, cur_date), self.frame, params)

    def show_record(self):
        camera = cv2.VideoCapture(self.rec_src)

        while True:
            firstFrame, self.frame = camera.read()
            cv2.imshow("Security test", self.frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
        camera.release()
        cv2.destroyAllWindows()

    def motion_detect(self):

        photo_date = 0
        delta_time = 0
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        fgbg = cv2.createBackgroundSubtractorMOG2()
        camera = cv2.VideoCapture(self.rec_src)

        while True:
# Считываем кадр и извлекаем задний фон
            firstFrame, self.frame = camera.read()
            fgmask = fgbg.apply(self.frame)
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
                (x, y, w, h) = cv2.boundingRect(c)
                cv2.rectangle(self.frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cur_date = dt.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
                cv2.putText(self.frame, "Room Status: {}".format(self.alarm_text), (10, 25), cv2.FONT_ITALIC, 0.7, (0, 0, 255), 1)
                cv2.putText(self.frame, "Time when detected: {}".format(cur_date), (10, 55), cv2.FONT_ITALIC, 0.65, (0, 255, 255), 1)

# Отсчитываем get_time секунд, перед тем как сделать новую фотку
                if self.rec_type == 'photo':
                    cdate = time.time()
                    delta_time = cdate - photo_date
                    if delta_time > self.rec_int:
                        videocam.take_a_photo(self)
                        photo_date = time.time()
                    else:
                        continue
# надо переписать чтобы делал видеопоток, а не писал конкретный кадр в видео\сек
#                elif self.rec_type == 'video':
#                    cdate = time.time()
#                    delta_time = cdate - photo_date
#                    if delta_time > self.rec_int:
#                        videocam.take_a_video(self.rec_frame)
#                        photo_date = time.time()
#                    else:
#                        continue

# Выведем картинку на экран
            # cv2.imshow("In grayscale mask", fgmask)
            cv2.imshow("In grayscale with thresh", thresh)
            # cv2.imshow("DeltaFrame", frameDelta)
            cv2.imshow("Security Feed", self.frame)

            # Ждем кнопку q для выхода из цикла
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break

# Освобождаем камеру, убиваем окна
        camera.release()
        cv2.destroyAllWindows()


logitech = videocam(0, 'photo', 1, '/home/itadmin/detects/', 'alarm!')
logitech.show_record()
logitech.motion_detect()
