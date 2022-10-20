import os
import cv2

video_path = 'C:/Users/yagmur.kaya/PycharmProjects/ygmr_tez/Framextract2folder/inputP'

output_path = 'C:/Users/yagmur.kaya/PycharmProjects/ygmr_tez/Framextract2folder/outputP'

input_file_list = os.listdir(video_path)
print("input_file_list listele: ", *input_file_list, sep="\n")
sep = '.'

for i in input_file_list:
    print("her bir klasör adı:", i)
    klasor_isim = i.split(sep, 1)[0]
    print("klasör ismi .dan ayrılmış hali:", klasor_isim)
    yeni_path = os.path.join(output_path, klasor_isim)
    print("image isminden oluşan yeni/son dosya yolu: ", yeni_path)
   # os.mkdir(yeni_path)
    if not os.path.exists(yeni_path):
        os.mkdir(yeni_path)
    else:
        print("Klasör zaten var, oluşturmaya gerek yok")

    yolyolu = os.path.join(video_path, i)
    print("input yolu:", yolyolu)
    cap = cv2.VideoCapture(yolyolu)
    index = 0

    while cap.isOpened():
        Ret, frame = cap.read()

        if Ret:
            index += 1
            if index % 24 != 0:
                continue
            cv2.imwrite(yeni_path + '/' + 'Frame_' + str(index) + '.png', frame)
        else:
            break
    cap.release()



