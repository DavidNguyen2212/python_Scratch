# Cài đặt opencv-python và dlib
import cv2 # opencv-python
import dlib
import os



# read the image
os.chdir(r"C:\Users\DELL\Documents\Python3\Nhan_dien_khuon_mat")
img = cv2.imread("skdd.jpg")
# chuyển đen trắng (gray scale), vì ảnh màu RGB: 3 chiều, trắng đen: 2D. Nhận diện km ko cần 3 chiều
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

# dlib: load face recognition detector
face_detector = dlib.get_frontal_face_detector()
faces = face_detector(gray)
print(len(faces)) # 2 khuon mat

# load the predictor
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Vẽ khung xác định khuôn mặt
for face in faces:
    # chuẩn bị tọa độ 2 góc của hcn
    x1 = face.left()
    y1 = face.top()
    x2 = face.right()
    y2 = face.bottom()

    # vẽ hcn
    cv2.rectangle(img=img, pt1=(x1,y1), pt2=(x2,y2), color=(0,255,0), thickness=2)
    face_68_point = predictor(image=gray, box=face)     # HÀM TRẢ VỀ 68 ĐIỂM KHUÔN MẶT
    for n in range(68):
        x = face_68_point.part(n).x     # trích xuất x, y của từng điểm (part)
        y = face_68_point.part(n).y 
        cv2.circle(img=img, center=(x,y), radius=2, color=(0,0,255), thickness=1)   # thickness phải là int

cv2.imshow(winname="Face Recognition App", mat=img)
cv2.waitKey(delay=0)    # delay = 0 thì phải nhấn nút mới đóng cửa sổ
cv2.destroyAllWindows()
