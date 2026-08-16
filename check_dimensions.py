import os
from PIL import Image
from collections import Counter

dataset_path = "dataset/PetImages"
sizes = []
for class_name in ["Cat", "Dog"]:
    folder_path = os.path.join(dataset_path, class_name)
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            image = Image.open(file_path)
            sizes.append(image.size)
        except:
            pass
        
print("total valid images: ", len(sizes))
size_counts = Counter(sizes)
print("Most common image sizes: ")
for size, count in size_counts.most_common(10):
    print(size, ":", count)