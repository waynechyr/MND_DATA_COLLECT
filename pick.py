import os
import shutil

def classify_images(add_folder, night_folder, thermal_folder, original_night_folder, original_thermal_folder):
    add_files = os.listdir(add_folder)
    night_files = os.listdir(original_night_folder)
    thermal_files = os.listdir(original_thermal_folder)

    for file in add_files:
        if file in night_files:
            shutil.copy(os.path.join(original_night_folder, file), os.path.join(night_folder, file))
            shutil.copy(os.path.join(original_thermal_folder, file), os.path.join(thermal_folder, file))

# 設定資料夾路徑
original_night_folder = '/home/wayne/Desktop/國防部/finalvideo/公館3/night'#
original_thermal_folder= '/home/wayne/Desktop/國防部/finalvideo/公館3/thermal'
add_folder = '/home/wayne/Desktop/國防部/finalresult/add'
night_folder = '/home/wayne/Desktop/國防部/finalresult/night5'
thermal_folder = '/home/wayne/Desktop/國防部/finalresult/thermal5'

# 執行分類
classify_images(add_folder, night_folder, thermal_folder, original_night_folder, original_thermal_folder)