Hello!
# Karolina Fic's Security System NVIDIA
This project detects whether Karolina (me), a package, or something unrecognized is in the view of the camera.
This project worls by classifying images with ImageNet. To view the image or live video from the camera, you will need to scp it to your host computer. Initially, I collected 300 images (100 per class - Karolina, package, unrecognized) and retrained a model. After retraining the model and exporting, it was ready to work! I tested it with a random image from my data. Then I tested it again with live video. (Both will be attached below.)
