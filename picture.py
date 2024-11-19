import cv2
import os

def save_frames_from_video(video_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()
    count = 0
    
    while success:
        cv2.imwrite(os.path.join(output_folder, "frame%d.jpg" % count), image)  # save frame as JPEG file      
        success, image = vidcap.read()
        print('Read a new frame from {}: {}'.format(video_path, success))
        count += 1
    
    vidcap.release()

if __name__ == "__main__":
    video_files = ['/home/wayne/Desktop/國防部/finalvideo/公館3/rgb.mp4', '/home/wayne/Desktop/國防部/finalvideo/公館3/trm.mp4', '/home/wayne/Desktop/國防部/finalvideo/公館3/add.mp4']
    output_folders = ['./finalvideo/night', './finalvideo/thermal', './finalvideo/add']

    for video_file, output_folder in zip(video_files, output_folders):
        save_frames_from_video(video_file, output_folder)
