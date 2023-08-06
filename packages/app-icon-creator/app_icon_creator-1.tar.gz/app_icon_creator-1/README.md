## Installation 
    pip install app_icon_creator
    or run setup.py install

## Intro
    This is a simple tool for resizing a base icon to match the android and ios formats.
    There are other tools out there for this and most of them are better, but I needed ideas for portfolio projects.

## Usage
    app_icon_creator --base_icon {MYICONPATH}
    This will take your base icon and convert it to all of the necessary dimensions.

## Optional Args

    --output_path, default = ./output, help = The directory to drop your icons.
    --icon_name,default = "",help = Optional name to use to rename the generated icons. If empty we will use the name of the base icon + the new size.
    --extension,default = ".png",help = The file extension to use.

## Requirements
    PIL (pip install pillow)