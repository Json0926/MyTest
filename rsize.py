import cv2
pic = cv2.imread('./data/000064.png')
pic = cv2.resize(pic, (20, 20), interpolation=cv2.INTER_CUBIC)
cv2.imshow('', pic)
cv2.waitKey()
cv2.destroyAllWindows()