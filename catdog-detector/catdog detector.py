from multiprocessing.dummy import Pool as ThreadPool
import keras
import time
import requests
from pathlib import Path
import os
import numpy
import cv2


def download_url(link):
    name = link.split("/")
    animal = "dog"
    files = []
    try:
        headers = {}
        if "cat" in link:
            animal = "cat"
            headers = {"Content-Type": "application/json", "x-api-key": "778eb3c5-62b0-4f21-bd5a-c2a1c54fba0a"}
        bin_data = requests.get(link, headers=headers)
        path = "CNNImages/train/{}/{}".format(animal, name[-1])
        if path not in files:
            with open(path, "wb") as file:
                file.write(bin_data.content)

    except:
        print("Encountered an error for url: {}\n".format(link))


def get_images_links(url):
    links = []
    content = requests.get("https://dog.ceo/api/breeds/image/random/50")
    links += (content.json()['message'])    # add 50 dog image links
    headers = {"Content-Type": "application/json", "x-api-key": "778eb3c5-62b0-4f21-bd5a-c2a1c54fba0a"}
    content = requests.get(url, headers=headers)    # add 50 cat image links
    links += [i["url"] for i in content.json()]

    return links


def download_in_parallel(download_size=500):
    download_links_lst = []
    Path("CNNImages/train/cat/").mkdir(parents=True, exist_ok=True)     # create dir if doesnt exist
    Path("CNNImages/train/dog").mkdir(parents=True, exist_ok=True)
    Path("CNNImages/valid/cat/").mkdir(parents=True, exist_ok=True)
    Path("CNNImages/valid/dog/").mkdir(parents=True, exist_ok=True)
    print("Searching for images of cats and dogs now\n.\n.\n.\n")

    pool = ThreadPool(7)
    download_links_lst += pool.map(get_images_links, ["https://api.thecatapi.com/v1/images/search?mime_types=jpg%2Cpng&limit=50"
                                                       for _ in range(download_size//50)])
    pool.close()
    pool.join()
    links = []
    for link_lst in download_links_lst:
        links.extend(link_lst)
    start = time.time()

    print("Starting download of all {} images now\n.\n.\n.\n".format(len(links)))

    pool = ThreadPool(4)
    pool.map(download_url, links)

    total_time = time.time() - start

    print("Full download of {} images took {} seconds.\n".format(len(links), total_time))
    for index in range(download_size//5):
        down_cats, down_dogs = os.listdir("CNNImages/train/cat"), os.listdir("CNNImages/train/dog")
        os.rename("CNNImages/train/cat/{}".format(down_cats[index]), "CNNImages/valid/cat/{}".format(down_cats[index]))
        os.rename("CNNImages/train/dog/{}".format(down_dogs[index]), "CNNImages/valid/dog/{}".format(down_dogs[index]))


def preprocess_image(path_image):
    img = keras.preprocessing.image.load_img(path_image, target_size=(224, 224))
    img_array = keras.preprocessing.image.image.img_to_array(img)
    img_array = numpy.expand_dims(img_array, axis=0)
    img_array = keras.applications.resnet50.preprocess_input(img_array)

    return img_array


def resnet50_model():
    start = time.time()
    resnet = keras.applications.resnet50.ResNet50()
    new_layer = keras.layers.Dense(2, activation="softmax")(resnet.output)
    full_model = keras.models.Model(inputs=resnet.input, outputs=new_layer)

    for layers in full_model.layers[:-2]:
        layers.trainable = False

    image_batch = keras.preprocessing.image.ImageDataGenerator().flow_from_directory("CNNImages/train",
                                                                                        target_size=(224, 224), classes=["cat", "dog"],
                                                                                        batch_size=10, shuffle=True)
    valid_batch = keras.preprocessing.image.ImageDataGenerator().flow_from_directory("CNNImages/valid",
                                                                                        target_size=(224, 224), classes=["cat", "dog"],
                                                                                        batch_size=10, shuffle=True)


    full_model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
    full_model.fit_generator(image_batch, epochs=5, verbose=2, validation_data=valid_batch)
    full_model.save("cats-dogs-model.h5")
    diff = time.time() - start

    print("Saved model successfully as cats-dogs-model.h5 and full training took {} seconds.\n".format(round(diff, 4)))


def sort_images(path_image, image_name):
    class_indices = {"cat": 0, "dog": 1}
    loaded_model = keras.models.load_model("cats-dogs-model.h5")
t    prepared_image = preprocess_image(path_image+"/"+image_name)
    score = loaded_model.predict(prepared_image).argmax()   # basically says if 1 or 0 for dog and cat, not probability
    for keys, value in class_indices.items():
        if value == score:
            print("I predict image {} is a {} :)\n".format(image_name, keys))


if __name__ == '__main__':
    train_or_predict = input("Would you like me to predict cats or dogs for you or instead train me if you haven't"
                             " yet?\n[Predict/Train]\n").lower()
    if train_or_predict == "predict":
        # try:
        image_path = input("Please paste the path of the image or folder of images you want to detect?\n")
        if os.path.isdir(image_path):
            for f_name in os.listdir(image_path):
                sort_images(image_path, f_name)
        else:
            sort_images(image_path, image_path.split("/")[-1])
        # except:
        #     print("Encountered an error. Invalid input.\nPlease try again")

    elif train_or_predict == "train":
        download_images_prompt = input("Do you already have a CNNImages folder with train and valid subfolders "
                                       "containing cat and dog images in it or would you like to start downloading"
                                       " the required data for training?  [Y/N]\n").lower()
        if download_images_prompt == "y":
            if "CNNImages" in os.listdir(os.getcwd()):
                resnet50_model()
            else:
                print("We can't find the required folders of data to train on. Please try again and choose No "
                      "to the above question so we can download it for you.\n")
        else:
            data_size = input("Great. Now how many photos would you like to train me on in *total*? (1000 is a good start; 500 each)\n")
            download_in_parallel(int(data_size)//2)
            resnet50_model()
        print("Fantastic. You have successfully trained me with all the images we downloaded.\nYou can now"
              " use me to predict cats and dogs for you by choosing the predict option at the start. Have fun :)\n")
    else:
        print("That wasn't part of the options...\n")


    print("Thank you for using my services :)")
