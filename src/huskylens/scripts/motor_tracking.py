import random
import time
import subprocess
import json
from huskylib import HuskyLensLibrary

huskylens = HuskyLensLibrary("I2C","", address=0x32)


def motor_tracking():
    # Captura os blocos continuamente
            while True:
                try:
                    block = huskylens.blocks()
                    x_husky= block.x
                    angle = 650     
                    z=1 #flag para colocar os olhos do robo em modo de seguir o objeto
                    #Neutro
                    if (140 <= x_husky <= 180):
                         angle= 650  
                         return angle         
                    # Esqueda
                    if(180 <= x_husky <= 340):
                         angle= angle-50  
                         return angle   
                    #Direita
                    if(0 <= x_husky <= 140):
                         angle= angle+50  
                         return angle           
                   
                except Exception as e:
                    #continue
                        angle= 650  
                        return angle                      
                except KeyboardInterrupt:
                    print("\nQUITING")
                    break
                    quit()
