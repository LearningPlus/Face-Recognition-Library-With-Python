import face_recognition

image = face_recognition.load_image_file("team.jpg")
face_locations = face_recognition.face_locations(image)

# Array of coordinates of each image
# print(face_locations)
print("There are {} people in the image".format(len(face_locations)))