import cv2

# Load ảnh luôn đưa về dạng BGR blue -green -red
img = cv2.imread("19_opencv/cat.jpg")

if img is None:
    print("Can not load Image")
else:
    # chuyển ảnh về grayscale
    # img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # # print("data type", type(img_gray))
    # # print("shape", img_gray.shape)

    # # # Đợi đến khi nhấn 1 phím
    # cv2.imshow("window", img_gray)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # resize ảnh
    new_width = 300
    new_height = 400
    new_size = (new_width, new_height)

    resize_img = cv2.resize(img, new_size, interpolation=cv2.INTER_LINEAR)
    cv2.imshow("imf", resize_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
