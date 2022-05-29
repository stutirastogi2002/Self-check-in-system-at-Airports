import sys
import cv2
import numpy as np
from tkinter import *
from PIL import Image, ImageTk
import face_recognition
import os
from database import DBHelper

# object of class DBHelper is created
db = DBHelper()
today = "Sunday"
place = "New Delhi"
text = "NA"


# command function for proceed button
def nextPage():
    l1.pack_forget()
    l2.pack_forget()
    inputBox.pack_forget()
    enterButton.pack_forget()
    l5.pack_forget()
    matchFace()


# command function for exit button
def func():
    sys.exit()


# variable defining path to images folder
path = 'Images'
images = []
classNames = []
myList = os.listdir(path)  # here names of images with extension are inserted to myList
print(myList)

# here names of images or pasId of person from is fetched from name of image by removing extension
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)


# function to find encodings of stored images
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


# command function which takes input from text box after we enter PNR number
def getInput():
    inputText = inputBox.get(1.0, "end-1c")
    global text
    text = db.fetch(inputText)
    if inputText.upper() == text:
        l2.configure(text="PNR number matched")
        inputBox.pack_forget()
        l5.pack(pady=20)
        enterButton.configure(text="Proceed", command=nextPage)
        l3.pack_forget()

    else:
        l3.pack(pady=10)


# declaration and definiton of root window
root = Tk()
root.title("SELF CHECK-IN SYSTEM")
root.geometry("1250x600+0+0")
root.configure(bg="#32C8FA")
labelImage = Label(root, bg="red")
l1 = Label(root, text="Welcome Dear Customer", font=("new times roman", 30), bg="#c2d94e", fg="#9c22a1")
l2 = Label(root, text="Please Enter the PNR Number", font=("new times roman", 30), bg='pink', fg="blue")
l3 = Label(root, text="PNR number not found", font=("new times roman", 20), fg="pink", bg='blue')
inputBox = Text(root, height=1, width=10, font=("new times roman", 50))
enterButton = Button(root, text="NEXT", font=("new times roman", 20), command=getInput)
exitButton = Button(root, text="EXIT", font=25, command=func)
exitButton.pack(side="bottom")
l4 = Label(root, text="Please validate your face before proceeding Camera is starting", font=100, fg="pink", bg='blue')
l5 = Label(root, text="Click on the proceed to continue to Face Validation", font=("tmes new roman", 30), fg="#166b33",bg="#cbf7f4")
frame = Frame(root, bg="#32C8FA", width=600, height=600, borderwidth=1, relief="flat")

# variables declared to hold information about passengers
fName = "NA"
lName = "NA"
origin_airport = "NA"
destination_airport = "NA"
flight_day = "NA"

# labels declared to hold the details of passengers
t1 = Label(frame, text="NAME", font=("new times roman", 16, "bold"), fg="#151f75", bg="#32C8FA")
t2 = Label(frame, text=str(fName), font=("new times roman", 16), fg="#66128c", bg="#32C8FA")
t3 = Label(frame, text="Last Name", font=("new times roman", 16, "bold"), fg="#151f75", bg="#32C8FA")
t4 = Label(frame, text=str(lName), font=("new times roman", 16), fg="#66128c", bg="#32C8FA")


# packs the contents of welcome frame
def frame1():
    l1.pack(pady=40)
    l2.pack(pady=60)
    inputBox.pack(pady=10)
    enterButton.configure(text="NEXT")
    exitButton.configure(command=func)
    enterButton.pack()
    exitButton.pack(side="bottom")


# function which captures image of passenger and matches it with images from database
def matchFace():
    i = 50
    cap = cv2.VideoCapture(1)
    while i >= 0:
        i = i - 1

        success, img = cap.read()
        imgS = cv2.resize(img, (0, 0), None, 0.75, 0.75)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                print("matched")
                img = ImageTk.PhotoImage(Image.fromarray(img))
                nl = Label(root, image=img)
                nl.pack(side="left")
                label1 = Label(root, text="Face Verified", font=("times new roman", 40), fg="#166b33", bg="#cbf7f4")
                label1.pack(side="bottom", pady=50)
                db.fetch(name)
                pnr = db.getPnr()
                if text.upper() != pnr:
                    label4 = Label(root, text="PNR number entered not matched", font=("times new roman", 25))
                    label5 = Label(root, text="Correct PNR is " + pnr, font=("times new roman", 25), bg="blue")
                    label4.pack()
                    label5.pack()

                fName = db.getFirstName()
                lName = db.getLastName()
                origin_airport = db.getOrigin()
                flight_day = db.getFDay()

                t2.configure(text=fName)
                t4.configure(text=lName)

                t1.pack(pady=5)
                t2.pack(pady=5)
                t3.pack(pady=5)
                t4.pack(pady=5)
                frame.pack(pady=20)
                f1 = 0
                f2 = 0
                label2 = Label(root, text="na", font=("new times roman", 20), fg="blue", bg="grey")
                if today.upper() == flight_day.upper():
                    f1 = 1
                if place.upper() == origin_airport.upper():
                    f2 = 1
                label3 = Label(root, text="Happy Journey", font=("new times roman", 30), fg="#9c22a1", bg="#f2cd66")
                if f1 and f2:
                    label2.configure(text="You arrived at the correct airport", fg="#166b33", bg="#cbf7f4")
                    label2.pack(pady=20)
                    label3.pack(pady=20)
                elif f1:
                    label2.configure(text="You arrived at the wrong airport", fg="#f50a50", bg="#0abef5")
                    label2.pack(pady=20)
                elif f2:
                    label2.configure(text="Your Flight is not scheduled today", fg="#f50a50", bg="#0abef5")
                    label2.pack(pady=20)
                else:
                    label2.configure(text="You arrived at wrong airport and on wrong day", fg="#f50a50", bg="#0abef5")
                    label2.pack(pady=20)

            else:
                print("not matched")

                img = ImageTk.PhotoImage(Image.fromarray(img))
                nl = Label(root, image=img)
                nl.pack(side="left")
                label1 = Label(root, text="Face Not Verified", font=("times new roman", 38), fg="#ba1152", bg="#4399f0")
                label2 = Label(root, text="Please proceed to manual verification", font=("times new roman", 30),
                               fg="#ba1152", bg="#4399f0")
                label2.pack(side="bottom", pady=30)
                label1.pack(pady=30)

            img = ImageTk.PhotoImage(Image.fromarray(img))
            labelImage.configure(image=img)

    cap.release()


def main():
    frame1()
    root.mainloop()


encodeListKnown = findEncodings(images)  # function encode list is invoked
print('Encoding Complete')

if __name__ == '__main__':
    main()
