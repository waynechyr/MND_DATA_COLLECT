# 使用程式開啟熱影像以及夜視鏡鏡頭

1. 查找相機編號
   ```
   python lookup.py
   ```
2. 收集資料
   ```
   python thg.py
   ```
(這裡要注意相機編號是否正確，結果會保存於result，可以根據不同資料蒐集地點更改檔名)

# 資料處理
1. 執行 ```python crop.py ```將影像裁剪成適當大小，並且透過這個步驟去調整homography的值產生疊合後的影像，結果存於finalvideo
2. 執行 ```python picture.py ```將影像轉換為圖像，並存於各地點名稱的資料夾內
# 透過挑選thermal+RGB(night)的疊加影像，手動挑選出疊合效果好的資料放在add資料夾裡
1. 執行```python pick.py ```將與add資料夾裡相同檔名的night和thermal影像存於finalresult的資料夾
2. 最後先將所有地點的add, night, thermal圖像都放在同個資料夾，接著執行```python combine.py ```將檔名按照數字順序做處理

## 特別要注意的是以上程式碼裡面有關路徑檔名的部分要依照自己的需要做修改
# 最後我們是用roboflow這個網站執行標註圖像處理
https://roboflow.com/

