import cv2
import numpy as np
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils


print("Sistem Hazır! Kamera açılıyor...")

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
)

# Kamera ayarları
cap = cv2.VideoCapture(0)
h_cam, w_cam = 480, 640
cap.set(3, w_cam)
cap.set(4, h_cam)

canvas = np.zeros((h_cam, w_cam, 3), np.uint8) 
px, py = 0, 0
color = (255, 0, 255) 
brush_thickness = 5
eraser_thickness = 50

while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1) 
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
   
    result = hands.process(rgb_frame)
    
    fingers = [] 

    if result.multi_hand_landmarks:
        for hand_lms in result.multi_hand_landmarks:
            
            tip_ids = [4, 8, 12, 16, 20]
            lm_list = []
            
            for id, lm in enumerate(hand_lms.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append([id, cx, cy])

            if len(lm_list) != 0:
                
                if lm_list[tip_ids[0]][1] < lm_list[tip_ids[0] - 1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)

                
                for i in range(1, 5):
                    if lm_list[tip_ids[i]][2] < lm_list[tip_ids[i] - 2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)

                total_fingers = fingers.count(1)
                x1, y1 = lm_list[8][1:] 

                # 2. MOD SEÇİMİ VE ÇİZİM
                
                if total_fingers == 5:
                    cv2.circle(frame, (x1, y1), 15, (255, 255, 255), cv2.FILLED)
                    cv2.putText(frame, "SILGI", (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
                    cv2.line(canvas, (px, py), (x1, y1), (0, 0, 0), eraser_thickness)

                
                elif total_fingers == 2:
                    color = (255, 0, 255)
                    cv2.putText(frame, "RENK: PEMBE", (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, color, 2)

               
                elif total_fingers == 3:
                    color = (255, 0, 0)
                    cv2.putText(frame, "RENK: MAVI", (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, color, 2)

                
                elif total_fingers == 1:
                    cv2.circle(frame, (x1, y1), 10, color, cv2.FILLED)
                    if px == 0 and py == 0:
                        px, py = x1, y1
                    
                    cv2.line(canvas, (px, py), (x1, y1), color, brush_thickness)
                
                
                px, py = x1, y1
            
            
            mp_draw.draw_landmarks(frame, hand_lms, mp_hands.HAND_CONNECTIONS)

   
    img_gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, img_inv = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY_INV)
    img_inv = cv2.cvtColor(img_inv, cv2.COLOR_GRAY2BGR)
    frame = cv2.bitwise_and(frame, img_inv)
    frame = cv2.bitwise_or(frame, canvas)

    cv2.imshow("El ile Cizim Uygulamasi", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

