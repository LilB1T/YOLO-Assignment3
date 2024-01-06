import subprocess

if __name__ == '__main__':
    subprocess.run(["python3", "detect_and_crop.py", 
                    "--weights", "best.pt", 
                    "--source", "vehicle_1-6\\test\images\\1_jpg.rf.f1b1287e65f8bfc4f1b8002d28784836.jpg", 
                    "--img-size", "640", 
                    "--conf", "0.25"])
