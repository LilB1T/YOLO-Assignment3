import subprocess

if __name__ == '__main__':
    subprocess.run(["python3", "detect_and_crop.py", 
                    "--weights", "yolov7.pt", 
                    "--source", "vehicle_1-6\\valid\\images\\3_jpg.rf.66aa78b82b9e75754dfbf61170177f7f.jpg", 
                    "--img-size", "640", 
                    "--conf", "0.25"])
#weights --> weights file.
#source  --> validation dataset location.
#img     --> output image size, must be 640, because the model is trained that way.
#conf    --> is the confidence threshold, increase to get more fine detections decrease
           # incase the model doesn't performs well.