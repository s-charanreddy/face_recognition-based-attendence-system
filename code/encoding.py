
# function to find the encoding of the images

def find_encoding(images):
    import cv2
    import face_recognition
    encodelist = []
    for img in images:
        # conversion from BGR TO RGB
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # finding facial encodings
        encode = face_recognition.face_encodings(img)[0]
        print(type(encode))
        encodelist.append(encode)
    return encodelist
