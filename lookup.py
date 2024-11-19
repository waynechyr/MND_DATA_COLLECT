# -*- coding: utf-8 -*-
import cv2

def main():
    # 設置要查看的相機數量
    num_cameras = 10

    for i in range(num_cameras):
        cap = cv2.VideoCapture(i)

        # 檢查相機是否成功打開
        if cap.isOpened():
            print("相機 {} 已成功打開".format(i))

            # 獲取相機的寬度和高度
            width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
            height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
            print("相機 {} 影像大小：{}x{}".format(i, int(width), int(height)))

            # 釋放相機資源
            cap.release()
        else:
            print("無法打開相機 {}".format(i))

if __name__ == "__main__":
    main()
