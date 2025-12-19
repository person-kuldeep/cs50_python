import csv
import numpy as np
from PIL import Image

views_brightper_data = []
def main(): 
    with open("views.csv", "r", encoding="utf-8") as views, open("views_brightness.csv", "w", encoding="utf-8", newline='') as output:
        reader = csv.DictReader(views)
        writer = csv.DictWriter(output, fieldnames= reader.fieldnames + ["brightper"])
        writer.writeheader()
        for row in reader:
            filename = f"images/{row['id']}.jpeg"
            brightness = calculate_brightness(filename)
            brightper = f"{round((brightness*100), 2)}"
            row["brightper"] = brightper
            views_brightper_data.append(row)
            
        for line in sorted(views_brightper_data, key=lambda line: float(line["brightper"]), reverse=True):
            writer.writerow(line)

def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness


main()
