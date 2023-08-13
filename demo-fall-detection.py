from PIL import Image
from fall_prediction import Fall_prediction

img8 = Image.open("Images/fall_img_8.png")
img9 = Image.open("Images/fall_img_9.png")


response = Fall_prediction(img8, img9)

if response:
    print("There is", response['category'])
    print("Confidence :", response['confidence'])
    print("Angle : ", response['angle'])
    print("Keypoint_corr :", response['keypoint_corr'])
else:
     print("There is no fall detetcion...")
