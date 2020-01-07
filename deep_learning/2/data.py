import cv2, os
from sklearn.model_selection import train_test_split

data_dimensions = (50,50)

data_dir = "data\\"
raw_dir = "raw\\"

raw_index = [raw_dir+filename for filename in os.listdir(raw_dir)]
data_index = [data_dir+filename for filename in os.listdir(data_dir)]

if len(data_index) == 0:
    print("przetwarzanie obrazów...")
    for filename in raw_index:
        image = cv2.resize(cv2.imread(filename), data_dimensions, interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(filename.replace(raw_dir,data_dir),image)
    data_index = [data_dir+filename for filename in os.listdir(data_dir)]

data = list()
classes = list()

print("wczytywanie obrazów...")
for filename in data_index:
    data.append(cv2.imread(filename))
    if "cat" in filename:
        classes.append(0)
    elif "dog" in filename:
        classes.append(1)
    else:
        raise ValueError("nie można określić klasy obrazka")

print(f"{len(data)}, {len(classes)}")


train_data, test_data, train_classes, test_classes = train_test_split(data,classes, test_size=0.2, random_state=1)

