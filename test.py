import requests,json
import time
import cv2
import numpy

from json import JSONDecoder
http_url='https://api-cn.faceplusplus.com/facepp/v3/detect'
key = "Fn1QM4LuKANpi6l4ehA7x2A4NZxKoR8P"
secret = "c7LboSUdXAtkVpOckLNVjmbOU_nKF5h5"

cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    # Our operations on the frame come here

# Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('p'):
        cv2.imwrite("test.jpg",frame)
        filepath = r"test.jpg"
        data = {"api_key": key, "api_secret": secret, "return_attributes": "emotion,beauty,gender"}
        files = {"image_file": open(filepath, "rb")}
        response = requests.post(http_url, data=data, files=files)

        req_con = response.content.decode('utf-8')
        result = json.loads(req_con)

        try:
            gender = result["faces"][0]["attributes"]["gender"]["value"]
            beauty = result["faces"][0]["attributes"]["beauty"]["male_score"]
            anger = float(result["faces"][0]["attributes"]["emotion"]["anger"])
            disgust = float(result["faces"][0]["attributes"]["emotion"]["disgust"])
            fear = float(result["faces"][0]["attributes"]["emotion"]["fear"])
            happiness = float(result["faces"][0]["attributes"]["emotion"]["happiness"])
            neutral = float(result["faces"][0]["attributes"]["emotion"]["neutral"])
            sadness = float(result["faces"][0]["attributes"]["emotion"]["sadness"])
            suprise = float(result["faces"][0]["attributes"]["emotion"]["surprise"])
            print result
            print beauty
            print gender
            if happiness > 50:
                print("happy")
            if anger > 50:
                print("anger")
            if disgust > 50:
                print("disgust")
            if fear > 50:
                print("fear")
            if neutral > 50:
                print("neutral")
            if sadness > 50:
                print("sadness")
            if  suprise > 50:
                print(" suprise")
            #print(emotion)
        except:
            print("no face")
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


# req_dict = JSONDecoder().decode'(req_con)
