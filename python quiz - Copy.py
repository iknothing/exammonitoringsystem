def facecheck():
    import cv2
    import time
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') 
    cap = cv2.VideoCapture(0)
    while 1: 
      
        
        ret, img = cap.read() 
      
       
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      
        
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        print('no of faces detected currently:',len(faces))
        time.sleep(10)
        
        for (x,y,w,h) in faces:
            
            roi_gray = gray[y:y+h, x:x+w]
            
        
            eyes = eye_cascade.detectMultiScale(roi_gray)
      
        
        
        if len(faces) > 1:
            print('warning: more than 1 face detected')
            print("please show an overview of the room you are sitting in, so that we can detect if anyone is there in the room")
            time.sleep(2)
   
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
      
    
    cap.release()
      
    cv2.destroyAllWindows()
facecheck()
