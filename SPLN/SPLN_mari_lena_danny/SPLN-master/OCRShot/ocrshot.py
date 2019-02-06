#!/usr/bin/python3
#------------------------------------------------------------------------------
"""Ferramenta para recolha e análise de texto de imagens usando OCR (Google's Tesseract). """

import subprocess
import argparse
import time
import os
import pytesseract
import cv2
import yaml
import tempfile
import regex as re
import pyautogui
import inotify.adapters
import matplotlib.pyplot as plt
from nltk.tree import Tree
from io import StringIO
from scitools.StringFunction import StringFunction
from PIL import Image
import datetime

# Parse program arguments
ap = argparse.ArgumentParser()

ap.add_argument("-i", "--image", help="Path to image you wish to be OCRd")
ap.add_argument("-p", "--preprocess", type=str,
                help="Type of preprocessing to be done")
ap.add_argument("-l", "--lang", default="por", help="Language of text to be OCRd")

args = vars(ap.parse_args())

# Opening YAML 
with open('ocrshot.yml', 'r') as stream:
    data = yaml.load(stream)

# Configurations
if data['definicoes']['path']:
    prt_sc_path = data['definicoes']['path']
else:
    prt_sc_path = os.getenv("HOME") + '/Pictures'

# Load the image and convert it to grayscale
if args["image"]:
    image = cv2.imread(args["image"])
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    filename = args["image"]
    extensao = os.path.splitext(filename)[1]
    now = datetime.datetime.now()
else:
    i = inotify.adapters.Inotify()
    i.add_watch(prt_sc_path)
    pyautogui.hotkey('shift', 'prtscr')

    for event in i.event_gen(yield_nones=False):
        (_, type_names, path, filename) = event
        filename = path + "/" + filename
        break

    now = datetime.datetime.now()
    time.sleep(1)

    image = cv2.imread(filename)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    extensao = os.path.splitext(filename)[1]

# Check to see if we should apply thresholding to make the image
# binary or median blurring to remove noise and make it grayscale
if args["preprocess"] == "thresh":
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
elif args["preprocess"] == "blur":
    gray = cv2.medianBlur(gray, 3)

# Write the grayscale image to disk as a temporary file so we can
# apply OCR to it
tmp_file = "{}.png".format(os.getpid())
cv2.imwrite(tmp_file, gray)


# Load the image as a Pillow image, apply OCR, and then delete
# the temporary file
text = pytesseract.image_to_string(Image.open(tmp_file), lang=args["lang"])

# Correct text
text = re.sub(r'(?<!.;:?!)\n\s*(?=["\p{Ll}])', r' ', text)
text = re.sub(r'\n\n+', r'\n\n', text)

# Show temporary image to correct
image = cv2.imread(tmp_file)
plt.ion()
plt.imshow(image)
plt.show()
plt.pause(0.1)

# Show text to correct
with tempfile.NamedTemporaryFile(suffix=".tmp") as tmp:

  tmp.write(text.encode("utf-8"))
  tmp.flush()
  subprocess.call(["vi", tmp.name])

  tmp.seek(0)
  text = tmp.read().decode("utf-8")

  # Close image when saving text altered
  plt.close()

# Remove temporary file
os.remove(tmp_file)

# Reading metadata and creating dictionary for it
metadata = dict()
value_s = []

for item in data['metadados']:

    if isinstance(item, str):
        inp = input(item + ": ")
        metadata[item] = inp
    elif isinstance(item, dict):
        item = dict(item)
        key, value = list(item.items())[0]
        if key == "Classe":
            value_s = value
            while(True):
                inp = input(key + " [" + ', '.join(value_s) + "]: ")
                if inp not in value:
                    print("Opção não válida!")
                else: break
        metadata[key] = inp

new_name = metadata['Título'] + now.strftime("_%d-%m-%Y_%H:%M") + extensao

# Post processing
if "Classe" not in metadata:
    if not os.path.exists("default"):
        os.makedirs("default")
    
    if args['image']:
        subprocess.run(["cp", filename, "default/" + new_name])
    else: 
        subprocess.run(["mv", filename, "default/"] + new_name)
    print("O texto não foi pós-processado, uma vez que não foi indicada uma classe")
else:
    if not os.path.exists(metadata.get("Classe")):
        os.makedirs(metadata.get("Classe"))
    if args['image']:
        subprocess.run(["cp", filename, metadata.get("Classe") + "/" + new_name])
    else: 
        subprocess.run(["mv", filename, metadata.get("Classe") + "/" + new_name])
    print("A pós-processar...")
    exec(data['funcoes'][metadata.get("Classe")], globals()) 
