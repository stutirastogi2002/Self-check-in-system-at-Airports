
# Self Check-in System at Airports

This project is about a self-checking system at airport which uses facial recognition for verification of passengers.
## Tech Stack



## **Python**  

***Libraries used***

- open cv

- face_recognition : for face recognition

- Tkinter :  for GUI

- sys

- numpy

- Pillow

- os

- mysql-connector :  connecting the database

## **MySQL database**

- to store data of passengers





##  Working

1)  (a)User is asked to enter pnr no. if it exists then we proceed to facial verification.
         
    (b)If pnr no. doesn’t match, user is asked to enter again


 2) A photo of user is captured and is sent to model for recognition.
    
    (a)If face is recognized origin_airport  and day of flight are checked
         
         (i)If they are correct the user is verified and they can proceed.
         
         (ii)If they doesn’t match the user cannot proceed.
    
    (b)If face is not recognized the user is not verified, hence cannot proceed.

## Features

- Every passenger should have a valid PNR number
    - Passenger cannot proceed without it.

- If face is not verified, s/he has to proceed for manual verification.
- If face is verified/recognised, but arrives at wrong origin airport or day, s/he cannot proceed.


## Things to be done to run project

### System Requirements

- Clone the repository and open the project folder in Pycharm or any Python code editor.
- Install all the required libraries mentioned.
- System should have installed MYSQL database.

### How to run

- After opening the project, run the main file.
- Enter PNR number (usually it is of 6 digits but here we 3 digit PNR number).
- For face recognition, use photos from phone gallery since original person is not available.

#### Remarks

- Details of passengers are stored inside the database.
- Queries to create table and insert records are present inside the database.py file.
- Images are fetched from images folder and are coonected to databasse through their name which is the primary key in database and PNR number.
- To add more records, queries are required as well as their images with name as PNR number should be added to images folder.

## Screenshots

![App Screenshot](https://drive.google.com/file/d/1ujLbV1Iwool6rVcjzaHiR7wxV7iGhlbJ/view?usp=sharing)
![App Screenshot](https://drive.google.com/file/d/17JnKzUL6vJwNR4Fj62yQ8caYMfdIgd1n/view?usp=sharing)
![App Screenshot](https://drive.google.com/file/d/1oiWtiGOWpPUzvVRPR3v3o0KMCmRMlb8p/view?usp=sharing)
![App Screenshot](https://drive.google.com/file/d/1JPqZBirlVlNzbGm4jHRCWu9tUPUxbYB1/view?usp=sharing)
