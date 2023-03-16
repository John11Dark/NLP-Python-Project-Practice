# Tutorial 7 – OCR

# 1. Create an array containing the 4 correct symptoms

# 2. create a function that returns back a list that is containing the common words found in two lists given as input.

# 3.	In a loop, read each image and use OCR to convert the student’s answer to text.

# 4.	Use the wordpunct nltk tokeniser to tokenise the student’s answer.

# 5.	Use the intersection function how many of the 4 symptoms he/she mentioned.

# 6.	For each student, print in the console the answer he/she gave, as well as the marks he/she got.

symptoms = ["Headache", "Fever", "Fatigue", "Cough"]


def intersection(listOne, listTwo):
    return [value for value in listOne if value in listTwo]


import pytesseract
from PIL import Image
from nltk.tokenize import wordpunct_tokenize

pytesseract.pytesseract.tesseract_cmd = r"D:\Program Files\tesseract-ocr\tesseract.exe"
for i in range(1, 5):
    image = Image.open("Images/student" + str(i) + ".png")
    # print("Student " + str(i) + " image: ", image)
    text = pytesseract.image_to_string(image)
    tokens = wordpunct_tokenize(text)
    common = intersection(symptoms, tokens)
    print("Student " + str(i) + " answer: " + text)
    print("Student " + str(i) + " marks: " + str(len(common)) + "/4")
