import numpy as np
import face_recognition as fr
import cv2
from datetime import date
import xlsxwriter
import pandas as pd
import mysql.connector
import xlrd

attendance_excel_book = xlsxwriter.Workbook("attendance_sheet.xlsx")
attendance_excel_sheet = attendance_excel_book.add_worksheet("Attendance")
attendance_excel_sheet.write("A1", "Roll_No")
for i in range(2, 8):
	attendance_excel_sheet.write("A" +str(i), i - 1)
attendance_excel_sheet.write("B1", "Name")
attendance_excel_sheet.write("B2", "Saurabh")
attendance_excel_sheet.write("B3", "Shelly")
attendance_excel_sheet.write("B4", "Shivam")
attendance_excel_sheet.write("B5", "Srijan")
attendance_excel_sheet.write("B6", "Suyash")
attendance_excel_sheet.write("B7", "Shubhanshi")
attendance_excel_sheet.write("C1", str(date.today()))
video_capture = cv2.VideoCapture(0)
present_set = set()
shivam_image = fr.load_image_file("saurabh5.jpeg")
shivam_face_encoding = fr.face_encodings(shivam_image)[0]
shivam_image1 = fr.load_image_file("shivam7.jpeg")
shivam_face_encoding1 = fr.face_encodings(shivam_image1)[0]
shivam_image2 = fr.load_image_file("suyash.jpeg")
shivam_face_encoding2 = fr.face_encodings(shivam_image2)[0]
shivam_image3 = fr.load_image_file("srijan8.jpeg")
shivam_face_encoding3 = fr.face_encodings(shivam_image3)[0]
shivam_image4 = fr.load_image_file("shubhanshi7.jpeg")
shivam_face_encoding4 = fr.face_encodings(shivam_image4)[0]
shivam_image5 = fr.load_image_file("shelly8.jpeg")
shivam_face_encoding5 = fr.face_encodings(shivam_image5)[0]

known_face_encondings = [shivam_face_encoding]
known_face_names = ["Saurabh"]
known_face_encondings1 = [shivam_face_encoding1]
known_face_names1 = ["Shivam"]
known_face_encondings2 = [shivam_face_encoding2]
known_face_names2 = ["Suyash"]
known_face_encondings3 = [shivam_face_encoding3]
known_face_names3 = ["Srijan"]
known_face_encondings4 = [shivam_face_encoding4]
known_face_names4 = ["Shubhanshi"]
known_face_encondings5 = [shivam_face_encoding5]
known_face_names5 = ["Shelly"]
while True:
	key = 0
	ret, frame = video_capture.read()

	rgb_frame = frame[:, :, ::-1]

	face_locations = fr.face_locations(rgb_frame)
	face_encodings = fr.face_encodings(rgb_frame, face_locations)

	for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

		matches = fr.compare_faces(known_face_encondings, face_encoding)
		matches1 = fr.compare_faces(known_face_encondings1, face_encoding)
		matches2 = fr.compare_faces(known_face_encondings2, face_encoding)
		matches3 = fr.compare_faces(known_face_encondings3, face_encoding)
		matches4 = fr.compare_faces(known_face_encondings4, face_encoding)
		matches5 = fr.compare_faces(known_face_encondings5, face_encoding)

		name = "Unknown"

		face_distances = fr.face_distance(known_face_encondings, face_encoding)
		face_distances1 = fr.face_distance(known_face_encondings1, face_encoding)
		face_distances2 = fr.face_distance(known_face_encondings2, face_encoding)
		face_distances3 = fr.face_distance(known_face_encondings3, face_encoding)
		face_distances4 = fr.face_distance(known_face_encondings4, face_encoding)
		face_distances5 = fr.face_distance(known_face_encondings5, face_encoding)

		best_match_index = np.argmin(face_distances)
		best_match_index1 = np.argmin(face_distances1)
		best_match_index2 = np.argmin(face_distances2)
		best_match_index3 = np.argmin(face_distances3)
		best_match_index4 = np.argmin(face_distances4)
		best_match_index5 = np.argmin(face_distances5)

		if matches[best_match_index]:
			name = known_face_names[best_match_index]
			present_set.add(name)
			key = 1
		elif matches1[best_match_index1]:
			name = known_face_names1[best_match_index1]
			present_set.add(name)
			key = 1
		elif matches2[best_match_index2]:
			name = known_face_names2[best_match_index2]
			present_set.add(name)
			key = 1
		elif matches3[best_match_index3] :
			name = known_face_names3[best_match_index3]
			present_set.add(name)
			key=1

		elif matches4[best_match_index4]:
			name = known_face_names4[best_match_index4]
			present_set.add(name)
			key=1

		elif matches5[best_match_index5]:
			name = known_face_names5[best_match_index5]
			present_set.add(name)
			key = 1

		if key == 1:
			cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
			cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
		else:
			cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
			cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)

		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (0, 0, 0), 1)

	cv2.imshow('Webcam_face recognition', frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
print(present_set)
sheet = pd.read_excel("attendance_sheet.xlsx")
j = 0
for i in range(2, 8):
	if sheet.values[j][1] in present_set:
		attendance_excel_sheet.write("C" + str(i), "P")
	else:
		attendance_excel_sheet.write("C" + str(i), "A")
	j = j + 1
sheet1 = pd.read_excel("attendance_sheet.xlsx")
attendance_excel_book.close()
video_capture.release()
cv2.destroyAllWindows()
conn=mysql.connector.connect(host='localhost',user='root',password='',database='data2')
cur=conn.cursor()

loc=("C:\\Users\\DELL\\PycharmProjects\\pythonProject\\attendance_sheet.xlsx")
l=list()
a=xlrd.open_workbook(loc)
sheet=a.sheet_by_index(0)
sheet.cell_value(0,0)
for i in range(0,7):
    l.append(tuple(sheet.row_values(i)))
q="insert into student(id,name,attendence)values(%s,%s,%s)"
cur.executemany(q,l)
conn.commit()

conn.close()