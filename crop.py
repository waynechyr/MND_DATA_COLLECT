import cv2
import numpy as np
import os

def find_homography():
    # RGB and Thermal Four corners
    # pts_RGB     = np.array([[164,291],[375,284],[376,252],[184,222]]) # 餐廳前
    # pts_Thermal = np.array([[224,306],[414,285],[414,256],[240,244]])
    # pts_RGB     = np.array([[148,301],[424,295],[423,242],[160,206]]) # 餐廳前test
    # pts_Thermal = np.array([[210,316],[458,294],[454,250],[209,234]])
    # pts_RGB     = np.array([[148,301],[424,295],[423,242],[160,206]]) # 餐廳前test
    # pts_Thermal = np.array([[220,316],[458,294],[454,250],[219,234]])

    pts_RGB     = np.array([[164,291],[375,284],[376,252],[184,222]]) #公館
    pts_Thermal = np.array([[220,306],[402,285],[402,256],[236,244]])
    h, status = cv2.findHomography(pts_Thermal,pts_RGB)
    return h

if __name__=="__main__":
    if not os.path.exists('finalvideo'):
        os.makedirs('finalvideo')
    cap_rgb = cv2.VideoCapture('/home/wayne/Desktop/國防部/result/公館1/night.mp4')
    cap_trm = cv2.VideoCapture('/home/wayne/Desktop/國防部/result/公館1/thermal.mp4')

    h = find_homography()
    counter = 0
    wait = 1

    for i in range(3):
        ret_trm, frame_trm = cap_trm.read()

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    # out_rgb = cv2.VideoWriter(os.path.join('finalvideo', 'rgb.mp4'), fourcc, 20, (318, 325))  # 填入裁切後影片的寬高
    # out_trm = cv2.VideoWriter(os.path.join('finalvideo', 'trm.mp4'), fourcc, 20, (318, 325))
    # out_add = cv2.VideoWriter(os.path.join('finalvideo', 'add.mp4'), fourcc, 20, (318, 325))
    out_rgb = cv2.VideoWriter(os.path.join('finalvideo', 'rgb.mp4'), fourcc, 20, (324, 318))  # 填入裁切後影片的寬高
    out_trm = cv2.VideoWriter(os.path.join('finalvideo', 'trm.mp4'), fourcc, 20, (324, 318))
    out_add = cv2.VideoWriter(os.path.join('finalvideo', 'add.mp4'), fourcc, 20, (324, 318))
    
    while cap_rgb.isOpened() and cap_trm.isOpened():
        ret_trm, frame_trm = cap_trm.read()
        ret_rgb, frame_rgb = cap_rgb.read()

        if not ret_rgb or not ret_trm:
            print('finish')
            break
        img_rgb = frame_rgb
        img_trm = frame_trm

        img_trm_homo = cv2.warpPerspective(img_trm, h, (img_rgb.shape[1], img_rgb.shape[0])) 
        img_trm_jet = cv2.applyColorMap(img_trm_homo, cv2.COLORMAP_JET)

        img_add_rgbtrm = cv2.addWeighted(img_rgb, 0.6, img_trm_jet, 0.4, gamma = 0)
        print(frame_rgb.shape)
        # cropped_img_rgb = frame_rgb[97:422, 136:454, :]
        # cropped_img_trm_homo = img_trm_homo[97:422, 136:454, :]
        # cropped_img_add_rgbtrm = img_add_rgbtrm[97:422, 136:454, :]
        cropped_img_rgb = frame_rgb[136:454, 98:422, :]
        cropped_img_trm_homo = img_trm_homo[136:454, 98:422, :]
        cropped_img_add_rgbtrm = img_add_rgbtrm[136:454, 98:422, :]
        out_rgb.write(cropped_img_rgb)
        out_trm.write(cropped_img_trm_homo)
        out_add.write(cropped_img_add_rgbtrm)

        if cv2.waitKey(wait) & 0xFF == ord('q'):
            break
        elif cv2.waitKey(wait) & 0xFF == ord('w'):
            wait = 0
        elif cv2.waitKey(wait) & 0xFF == ord('e'):
            wait = 1
        counter += 1 

cv2.destroyAllWindows()
cap_rgb.release()
cap_trm.release()
out_rgb.release()
out_trm.release()
out_add.release()


