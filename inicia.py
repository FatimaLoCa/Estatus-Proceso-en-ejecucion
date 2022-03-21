import os
import subprocess
import time



while(True):
    output = os.popen('wmic process get description').read()

    if ("main" in output) == False:
        p = subprocess.Popen(["C:/Users/lopez/Documents/INCO/9. noveno 2022A/Tolerante a fallas/Programas/Perceptron Checkpoint/dist/main/main.exe",
        "C:/Users/lopez/Documents/INCO/9. noveno 2022A/Tolerante a fallas/Programas/Perceptron Checkpoint/dist/main/dataset_Perceptron.txt" ])

    else:
        print("Ya se está ejecutando ")
    time.sleep(5)
