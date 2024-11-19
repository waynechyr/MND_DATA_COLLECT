import cv2
import numpy as np
import os
import datetime

def find_homography():
    # RGB and Thermal Four corners
    pts_RGB     = np.array([[287,164],[445,166],[287,238],[445,238]])
    pts_Thermal = np.array([[190,156],[432,164],[190,266],[432,269]])
    h, status = cv2.findHomography(pts_Thermal, pts_RGB)
    return h

def main():
    # 設置攝像頭索引
    camera_rgb_index = 0  # RGB攝像頭索引
    camera_trm_index = 2  # 熱成像攝像頭索引

    # 打開攝像頭
    cap_rgb = cv2.VideoCapture(camera_rgb_index)
    cap_trm = cv2.VideoCapture(camera_trm_index)

    # 檢查攝像頭是否成功打開
    if not cap_rgb.isOpened() or not cap_trm.isOpened():
        print("無法開啟攝像頭。")
        return

    # 定義保存的資料夾
    result_folder = "result"
    if not os.path.exists(result_folder):
        os.makedirs(result_folder)

    folder_name = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    folder_path = os.path.join(result_folder, folder_name)
    os.makedirs(folder_path)

    # 定義影片寫入器
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out_rgb = cv2.VideoWriter(os.path.join(folder_path, f"night.mp4"), fourcc, 20.0, (640, 480))
    out_trm = cv2.VideoWriter(os.path.join(folder_path, f"thermal.mp4"), fourcc, 20.0, (640, 512))
    out_homo = cv2.VideoWriter(os.path.join(folder_path, f"overlay.mp4"), fourcc, 20.0, (640, 480))

    # 獲取Homography矩陣
    h = find_homography()

    while True:
        ret_rgb, frame_rgb = cap_rgb.read()
        ret_trm, frame_trm = cap_trm.read()

        if not ret_rgb or not ret_trm:
            print("攝像頭讀取失敗。")
            break

        # 對熱成像攝像頭應用Homography
        frame_trm_homo = cv2.warpPerspective(frame_trm, h, (frame_rgb.shape[1], frame_rgb.shape[0]))

        # 將兩個畫面結合
        frame_combined = cv2.addWeighted(frame_rgb, 0.6, frame_trm_homo, 0.4, 0)

        # 顯示畫面
        cv2.imshow('RGB', frame_rgb)
        cv2.imshow('Thermal', frame_trm)
        # cv2.imshow('Overlay', frame_combined)

        # 影片寫入
        out_rgb.write(frame_rgb)
        out_trm.write(frame_trm)
        out_homo.write(frame_combined)

        # 按下 'q' 鍵退出迴圈
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 釋放資源
    cap_rgb.release()
    cap_trm.release()
    out_rgb.release()
    out_trm.release()
    out_homo.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
