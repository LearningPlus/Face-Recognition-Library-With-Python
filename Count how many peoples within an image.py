import face_recognition

image_of_obama = face_recognition.load_image_file("./know/Barack_Obama.jpg")
obama_face_encoding = face_recognition.face_encodings(image_of_obama)[0]

unknow_image = face_recognition.load_image_file("./unknown/Barack_Obama_2.jpg")
unknown_face_encoding = face_recognition.face_encodings(unknow_image)[0]

result = face_recognition.compare_faces([obama_face_encoding], unknown_face_encoding)
print(result[0])