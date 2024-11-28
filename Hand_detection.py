import cv2
import mediapipe
hand_model = mediapipe.solutions.hands
hand_drawing = mediapipe.solutions.drawing_utils
cap = cv2.VideoCapture(0)
with hand_model.Hands(min_tracking_confidence=0.5,min_detection_confidence=0.5) as hand:
    while True :
        control,webcam = cap.read()
        rgb= cv2.cvtColor(webcam,cv2.COLOR_BGR2RGB)
        result= hand.process(rgb)
        if result.multi_hand_landmarks:
            for hand_landmark in result.multi_hand_landmarks:
                hand_drawing.draw_landmarks(webcam,hand_landmark,hand_model.HAND_CONNECTIONS)
        cv2.imshow("hand model",webcam)
        if cv2.waitKey(15) == 27:
            break




























