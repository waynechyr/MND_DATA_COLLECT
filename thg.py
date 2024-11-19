# -*- coding: utf-8 -*-
import cv2
import os
import datetime

def main():
    # 設置要讀取的相機編號
    camera_indices = [0, 3]

    # 創建結果資料夾
    result_folder = "result"
    if not os.path.exists(result_folder):
        os.makedirs(result_folder)

    # 創建以當前時間命名的資料夾
    folder_name = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    folder_path = os.path.join(result_folder, folder_name)
    os.makedirs(folder_path)

    # 逐個開啟相機
    cameras = [cv2.VideoCapture(i) for i in camera_indices]

    # 檢查相機是否成功開啟
    for i, cap in zip(camera_indices, cameras):
        if not cap.isOpened():
            print("無法開啟相機 {}".format(i))
            return

    # 定義影片保存的路徑和格式
    output_paths = [os.path.join(folder_path, 'camera{}_output.mp4'.format(i)) for i in camera_indices]
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    outputs = [cv2.VideoWriter(path, fourcc, 20.0, (640, 480)) for path in output_paths]

    # 無限迴圈，持續讀取相機影像
    while True:
        # 讀取每個相機的影像
        frames = [cap.read()[1] for cap in cameras]

        # 顯示每個相機的影像
        for i, frame in enumerate(frames):
            frame = cv2.resize(frame, (640, 480))
            cv2.imshow('Camera {}'.format(camera_indices[i]), frame)
            # 將影像寫入輸出文件
            outputs[i].write(frame)

        # 按下 'q' 鍵退出迴圈
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 釋放資源
    for cap, output in zip(cameras, outputs):
        cap.release()
        output.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

