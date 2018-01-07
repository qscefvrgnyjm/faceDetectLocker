import requests,json
import time
import cv2
import numpy
import serial
arduino=serial.Serial('com13',9600)
from json import JSONDecoder
http_url='https://api-cn.faceplusplus.com/facepp/v3/compare'
key = "Fn1QM4LuKANpi6l4ehA7x2A4NZxKoR8P"
secret = "c7LboSUdXAtkVpOckLNVjmbOU_nKF5h5"

cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    # Our operations on the frame come here

# Display the resulting frame
    cv2.imshow('frame',frame)
    #try:
    if cv2.waitKey(1) & 0xFF == ord('p'):
            cv2.imwrite("test.jpg",frame)
            filepath1 = r"syy.jpg"
            filepath2 = r"test.jpg"
            data = {"api_key": key, "api_secret": secret,}
            files = {"image_file1": open(filepath1, "rb"),"image_file2": open(filepath2, "rb")}
            response = requests.post(http_url, data=data, files=files)
            req_con = response.content.decode('utf-8')
            result = json.loads(req_con)
            try:
                print result["confidence"]
                if result["confidence"]>80:
                    arduino.write("A")

                else:
                    arduino.write("B")
            except:
                print "no face"
            #if result>90:
                #print ("mmp")
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #except:
       # print("no face")
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


# req_dict = JSONDecoder().decode'(reAq_con)
