import os
import cv2


dirs = ["doga","haber","muzik","spor"]
root_path= r'C:\Users\yagmur.kaya\PycharmProjects\ygmr_tez\Framextract2folder\ornek_dosyalar/'

output_path = r'C:\Users\yagmur.kaya\PycharmProjects\ygmr_tez\Framextract2folder\outputP'


sep = '.'
for d in dirs:
    video_path = root_path + d
    print(">> ", video_path)

    input_file_list = os.listdir(video_path)

    for file in input_file_list:
        print(">>> ", file)
        klasor_isim = file.split(sep, 1)[0]
        print("klasör ismi .dan ayrılmış hali:", klasor_isim)
        yeni_path = os.path.join(output_path, d,  klasor_isim)
        print("image isminden oluşan yeni/son klasor yolu: ", yeni_path)
        if not os.path.isdir(yeni_path):
            os.mkdir(yeni_path)

        video_yolu = os.path.join(video_path, file)
        print("video_yolu", video_yolu)


        cap = cv2.VideoCapture(video_yolu)
        index = 0

        while cap.isOpened():
            Ret, frame = cap.read()

            if Ret:
                index += 1
                if index % 24 != 0:
                    continue
                frame_path = yeni_path + '/' + 'Frame_' + str(index) + '.png'
                print(frame_path)
                cv2.imwrite(frame_path, frame)
            else:
                break

        cap.release()