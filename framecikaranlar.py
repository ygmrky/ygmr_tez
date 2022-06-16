import os

import cv2

video_path = 'C:/Users/yagmur.kaya/PycharmProjects/ygmr_project1/Framextract2folder/inputP'

output_path = 'C:/Users/yagmur.kaya/PycharmProjects/ygmr_project1/Framextract2folder/outputP'

input_file_list = os.listdir(video_path)

sep = '.'
print(input_file_list)

for i in input_file_list:
    print(i)
    iyi = i.split(sep, 1)[0]
    print("yeni iiiimiz", iyi)
    salih = os.path.join(output_path, iyi)
    print(salih)
   # os.mkdir(salih)
    if not os.path.exists(salih):
        os.mkdir(salih)
    else:
        print("Kıf kıf o klasör zaten var ki")

    yolyolu = os.path.join(video_path, i)
    print("yol yolu:", yolyolu)
    cap = cv2.VideoCapture(yolyolu)
    index = 0

    while cap.isOpened():
        Ret, frame = cap.read()

        if Ret:
            index += 1
            if index % 24 != 0:
                continue
            cv2.imwrite(salih + '/' + 'Frame_' + str(index) + '.png', frame)
        else:
            break
    cap.release()


'''


for items in list:

path = os.path.join(output_path, items)

pwdpath)



from pathlib import Path


dir = '/path/to/some/file.txt'

print(Path(dir).stem)



sep = '...'

stripped = text.split(sep, 1)[0]



'''
