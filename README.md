# YOLO CROP OBJECTS AROUND THE BOUNDING BOXES

## Overview
  This projects was an assignment, that uses YOLOv7 to perform detection on vehicles and crops each detection 
  and saves it.

## IDE
  You can use any IDE to run the code, but in order to maximize the operations and save time we recommend using COLAB.

[<kbd>Open in Google Colab</kbd> <img src="https://colab.research.google.com/img/colab_favicon.ico" width="16" height="16" style="vertical-align: middle;">](https://colab.research.google.com)

## Table of Contents

1. [Installation](#installation)
3. [Main](#main)

## Installation

Run the below command to install all the required packages and libraries.
```bash
pip install -r requirements.txt
```
## Main
In order to run the main.py file, one must understand the parameters that are being used. Follow the table below to understand the meaning of each command inside main.py

| Command | Description |
| --- | --- |
| `weights` | weights file. |
| `source` | validation dataset location. |
| `img` | output image size, must be 640, because the model is trained that way. |
| `conf` | is the confidence threshold, increase to get more fine detections decrease incase the model doesn't performs well. |

after following the commands, replace with the desired requirements to run the code with different resutls and variations.
