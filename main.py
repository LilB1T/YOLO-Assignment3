import subprocess

if __name__ == '__main__':
    subprocess.run(["python3", "detect_and_crop.py", 
                    "--weights", "best.pt", 
                    "--source", "vehicle_1-6\\valid\\images\\3_jpg.rf.66aa78b82b9e75754dfbf61170177f7f.jpg", 
                    "--img-size", "640", 
                    "--conf", "0.25"])
