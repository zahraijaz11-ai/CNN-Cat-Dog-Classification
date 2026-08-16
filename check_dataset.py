from PIL import Image
import os

dataset_path = "dataset/PetImages"

bad_images = []

for category in ["Cat", "Dog"]:
    folder = os.path.join(dataset_path, category)

    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)

        if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
            continue

        try:
            with Image.open(filepath) as img:
                img.verify()

        except Exception:
            bad_images.append(filepath)

print("Total bad images:", len(bad_images))

for image in bad_images:
    print("Bad image:", image)