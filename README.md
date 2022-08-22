Hello!
# Karolina Fic's Security System NVIDIA
This project detects whether Karolina (me), a package, or something unrecognized is in the view of the camera. The security system and package identifier can help people know when an unwanted person is at their house, they can see who it is and call the police. The package identifier is useful for people who want to know exactly when their package arrived without having to check constantly.
### The Algorithm and Running the Project
This project works by classifying images with ImageNet. For this image classification project, I have retrained my own network that is very similar to the thumbs classification project. I trained the network with 300 images (100 per class - Karolina, package, unrecognized).After retraining and exporting the model, it was ready to work! I tested it with an image from my data (link attached below). Then I tested it again with live video. To view the image or live video from the camera, you will need to scp it to your host computer. The security system needs a camera, my downloaded data set, and my trained model. It uses the detectnet network, resnet18 network, and imagenet network. 
https://imgur.com/aeqM2eO
### Video Demonstration
https://youtu.be/je6TdX9q98I
