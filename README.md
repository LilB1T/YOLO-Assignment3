# YOLOv7 CROP OBJECTS AROUND THE BOUNDING BOXES

## Overview
  This projects was an assignment, that uses YOLOv7 to perform detection on vehicles and crops each detection 
  and saves it.

## IDE
  You can use any IDE to run the code, but in order to maximize the operations and save time we recommend using COLAB.

[<kbd><img src="https://colab.research.google.com/img/colab_favicon.ico" width="16" height="16" style="vertical-align: middle;"></kbd> ](https://colab.research.google.com)

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
| `weights` | weights that were trained using the dataset. |
| `source` | validation dataset location. The source location for the validation dataset follows the path "vehicle_1-6\valid\images" you can select any image from the directory by simply copying the relative path and replcae it in main.py |
| `img` | output image size, must be 640, because the model is trained that way. |
| `conf` | is the confidence threshold, increase to get more fine detections decrease incase the model doesn't performs well. |

after following the commands, replace with the desired requirements to run the code with different resutls and variations.
