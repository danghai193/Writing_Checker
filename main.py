# Nhập thư viện, bao gồm path để lấy đường dẫn; randint để lặp ngẫu nhiên; Translator để dịch
from os import path
from random import randint
from googletrans import Translator

USER_FOLDER = path.expanduser('~')+"\TASK 2.txt"
TITLE_NUMBER = '0 6 12 20 27 33 40 47 54 60 68 75 82 89 96 103 110 117 123 130 135 142 149 156 163 170 177 184 191 198 205 212 219 226 233 239 246 253'.split()

f = open(USER_FOLDER, 'r')
a = f.readlines() # Đọc cả file
#NOT IDEAL, TEMPORARY THING
f.close()

#DichCaDoan
def writeParagraph(paraNo):
    # Lấy đoạn Tiếng Anh
    temp2 = a[paraNo].split('.')
    # Biến đếm số câu
    sentenceNo = 1
    # Khởi tạo Trình Dịch & Dịch
    phienDichVien = Translator()
    translatedText = phienDichVien.translate(text = a[paraNo][3:], dest='vi')
    # Tách kết quả thành các câu
    temp = translatedText.text.split('.')
    # Lặp với đoạn Introduction
    for i in range(len(temp)):
        # Kiểm tra xem có phải dòng trống không
        if all([temp[i] != '\n',temp[i] != ' \n',temp[i] != '']):
            # In dòng đã dịch
            print(f'CÂU {sentenceNo}: {temp[i]}')
            input('--USER--> ')
            # In câu trả lời
            print('-ANSWER->', temp2[i])
            print()
            sentenceNo += 1
    print('HẾT ĐOẠN!'.center(40, '-'))
    
    # Lặp với các đoạn còn lại
    for j in range(1,4):
        # Lấy đoạn tiếng Anh
        temp2 = a[paraNo+j].split('.')
        # Dịch đoạn văn
        translatedText = phienDichVien.translate(text = a[paraNo+j], dest='vi')
        # Tách câu
        temp = translatedText.text.split('.')
        for i in range(len(temp)):
            # Kiểm tra dòng trống & In Đáp án
            if all([temp[i] != '\n',temp[i] != ' \n',temp[i] != '']):
                print(f'CÂU {sentenceNo}: {temp[i]}')
                input('--USER--> ')
                print('-ANSWER->', temp2[i])
                print()
                sentenceNo += 1
        print('HẾT ĐOẠN!'.center(40, '-'))
        
print('Welcome to Writing Checker!'.center(40, '-'))
while True:
    # Lấy số của tên bài
    x = randint(0, len(TITLE_NUMBER)-1)
    print('ĐỀ BÀI: '+ a[int(TITLE_NUMBER[x])][4:])
    if input("Đã làm bài này chưa? (Y/N): ".center(40, '-') + ' ') in ["N",'n']:
        writeParagraph(int(TITLE_NUMBER[x])+1)
        break

