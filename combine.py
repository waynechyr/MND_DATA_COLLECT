import os
import shutil

# # 設定五個資料夾的路徑
# folders = [
#     '/home/wayne/Desktop/國防部/finalresult/thermal1',
#     '/home/wayne/Desktop/國防部/finalresult/thermal2',
#     '/home/wayne/Desktop/國防部/finalresult/thermal3',
#     '/home/wayne/Desktop/國防部/finalresult/thermal4',
#     '/home/wayne/Desktop/國防部/finalresult/thermal5'
# ]

# # 設定目標資料夾的路徑
target_folder = '/home/wayne/Desktop/國防部/finalresult/dataset/thermal'

# # 建立目標資料夾
# os.makedirs(target_folder, exist_ok=True)

# 初始化圖片計數器
frame_counter = 0

# 遍歷五個資料夾，將照片複製到目標資料夾中，並重新命名文件
# for folder in folders:
#     for file in os.listdir(folder):
#         if file.lower().endswith(('.jpg', '.png')):
#             src_file = os.path.join(folder, file)
#             dst_file = os.path.join(target_folder, f'frame {frame_counter}.jpg')
#             shutil.copy(src_file, dst_file)
#             frame_counter += 1for folder in f:
for file in os.listdir(target_folder):
    if file.lower().endswith(('.jpg', '.png')):
        old = os.path.join(target_folder, file)
        new = os.path.join(target_folder, f'frame_{frame_counter}.jpg')
        os.rename(old, new)
        frame_counter += 1