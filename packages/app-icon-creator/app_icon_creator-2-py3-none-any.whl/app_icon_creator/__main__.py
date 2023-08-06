import argparse,os
from PIL import Image
from zipfile import ZipFile

#Create parser.
parser = argparse.ArgumentParser(description = "App icon args")
parser.add_argument("--base_icon",default = "",help ="The icon to resize.")
parser.add_argument("--output_path",default = "./output",help = "The path to drop the new icons.")
parser.add_argument("--icon_name",default = "",help = "Optional name to use to rename the generated icons. If empty we will use the name of the base icon + the new size.")
parser.add_argument("--extension",default = ".png",help = "The file extension to use.")
parser.add_argument("--cleanup",default = False,help = "If true, the program will clean all generated images outside of the zip file.")

#Image sizes.
SIZES = [
    (16,16),
    (20,20),
    (29,29),
    (32,32),
    (36,36),
    (40,40),
    (48,48),
    (50,50),
    (55,55),
    (57,57),
    (58,58),
    (60,60),
    (64,64),
    (72,72),
    (76,76),
    (80,80),
    (87,87),
    (88,88),
    (96,96),
    (100,100),
    (114,114),
    (120,120),
    (128,128),
    (144,144),
    (152,152),
    (167,167),
    (172,172),
    (180,180),
    (196,196),
    (256,256),
    (512,512),
    (1024,1024),
    (2048,2048),
    (4096,4096)
]

#Set vars.
args = vars(parser.parse_args())
icon = args["base_icon"]
out_path = args["output_path"]
base_name = args["icon_name"]

#Get base name if needed.
if base_name == "":
    path,name = os.path.split(icon)
    base_name,ext = os.path.splitext(name)

ext = args["extension"]

if not os.path.exists(out_path):
    os.makedirs(out_path)

im = Image.open(icon)

images = []

#Resize images.
for size in SIZES:
    out = im.resize(size)
    new_name = f"{out_path}/{base_name}_{size}.{ext}"
    out.save(new_name)
    images.append(new_name)

#Zip everything up.
with ZipFile(f"{out_path}/{base_name}.zip",'w') as zip:
    for value in images:
        zip.write(value)

#Remove the loose images if cleanup option is true.
if args["cleanup"]:
    for fil in images:
        os.remove(fil)
