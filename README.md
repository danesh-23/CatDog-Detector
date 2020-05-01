# CatDog Detector :dog: :cat:

## What is it?
CatDog Detector is a neural network based machine learning program that tries to learn what features in an image make up cats and dogs and then tries to identify them from any images.

## Getting Started
1. Download the project files as a ZIP [here](https://github.com/danesh-23/CatDog-Detector/archive/master.zip) or clone the repo by pasting the command below in your command prompt/terminal.
```
 git clone https://github.com/danesh-23/CatDog-Detector.git
```
2. Before going any further, you need a couple of external libraries to ensure the program is able to run including Keras, OpenCV and Numpy. You should download the latest version of these from their official website [Keras](https://pypi.org/project/Keras/#files), [Matplotlib](https://pypi.org/project/matplotlib/#files) and [OpenCV](https://pypi.org/project/opencv-python/).  
You may also download these using the command-line using the following commands below.  
```
pip install Keras
```
```
pip install matplotlib
```
```
pip install opencv-python
```
3. Navigate to the location you downloaded the source files to. You can follow along with the commands below if you are using a Mac.  
```
cd *PATH-OF-CATDOG-DETECTOR*
```
![](/images/instructions1.png)
4. To begin running the program, if youre using an IDE, you just need to run it and if youre using a CLI, simply call python on the file.
```
python3 catdog detector.py
```
![](/images/instructions2.png)
5. You have now entered the matrixx...haha.  
Now you have 2 options;  
i. Train and save a neural network (the option you need to choose the first time)   
ii. Use a neural network you have already trained to predict some images.  

6. If it is your first time using this program, type 'Train' and hit Enter. Then, George(my neural network, feel free to name yours) asks me if I already have a dataset of cats and dogs to train him on which you should say 'No' to, and he will then prompt for how many images you want to train him on in total.  
You can experiment on the size of images you want to download, keep in mind that the more images you train your neural-net on, the better they will perform BUT it also will take longer to download the resources required since the resources are not provided and downloaded in runtime too.  
A 1000 images is a reasonable start since it will do an even split of ~500 images for cats and dogs. 
![](/images/instructions3.png)  

7. Once you tell your neural-net how many images you want it trained on, it will start downloading images of cats and dogs to a new directory in the same directory called CNNImages and it will create respective subfolders for training later on.
![](/images/instructions4.png)

8. You need to wait for a little bit now since it needs to go and search for these images and download all of them to your machine. It will inform you once all the images have been downloaded and the time taken to download all the images as well as inform you if any errors were encountered.

9. Now, you can get to the actual heavy lifting part of this program, the machine learning part. Immediately once the images have been downloaded, it is fed to the neural network and the convolutional neural network model begins training on all this data and you will see its progress.  
This can take a while since images are complex objects to learn from so you can expect anywhere between 10-30 minutes depending on your own machine. The neural network model is saved to the same directory once it has completed learning and the results should look similar to the image below.  
![](/images/instructions5.png).  

10. George will then close the program since he has successfully prepared all the resources and trained himself for identifying cats and dogs reasonably well as we can see it reaches a 95% accuracy(which you will realise isn't great but a good start) so run the program once again like you did at the start and this time choose 'Predict' instead of 'Train'.  
![](/images/instructions6.png)

11. Voila, watch the magic happen! You now have an assistant that can help you identify those adorable puppies from the slightly less adorable kittens(in my opinion :yum: )
![](/images/instructions7.png).  

## A little about this project
I started working on creating George(neural network model) as I dove deeper into machine learning and neural networks and the differences between how neural networks learn in comparison to other machine learning methods such as Naive Bayes Classifier which I also did another project on [here](https://github.com/danesh-23/movie-recommender). I took a particular interest into how neural networks could learn from typical data we come across everyday such as images and did not require any specific compiling or ordering. The act of machines learning just from quantity is nothing short of amazing and never ceases to amaze me. The vast improvements in accuracy rate that convolutional neural networks have over standard sequential models specifically for complex image recognition tasks is another exciting topic of discussion. So, this was a small project I decided to work on to represent a practical application of neural networks that is fun. I also made a whole video compilation and edited it to the fun parts to 90 seconds with music to show my friends and family as i was so excited about it but that's a story for another day :grin:

## Reporting Bugs

To report a bug, you may use the [Bug Report template](.github/ISSUE_TEMPLATE/bug_report.md)

## Feature Request

If you have any ideas of interesting features you would like added, you may fill the [Feature Request form](.github/ISSUE_TEMPLATE/feature_request.md)

## Project maintainers

This project is maintained by Danesh Rajasolan(me). Use of this project under the [MIT License](LICENSE.md).
