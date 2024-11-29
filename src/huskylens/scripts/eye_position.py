import random
import time
import subprocess
import json
from huskylib import HuskyLensLibrary

huskylens = HuskyLensLibrary("I2C","", address=0x32)


def eye_tracking():
    # Captura os blocos continuamente
            while True:
                try:
                    block = huskylens.blocks()
                    x_husky, y_husky = block.x, block.y       
                    z=1 #flag para colocar os olhos do robo em modo de seguir o objeto
                    #Superior e Inferior
                    if (140 <= x_husky <= 180):
                        # Superior
                        if( 0 <= y_husky <= 100):                            
                            x = 0
                            y = 28  # 8 meio + 20 de abaixo
                            return x,y,z
                        # Inferior
                        if (140 <= y_husky <= 240):
                            x=0
                            y=-20# -20 abaixo 
                            return x,y,z                       
                    #Lateral Direita (superior,meio,inferior)
                    if(180 <= x_husky <= 340):
                        # Lateral Superior Direita
                        if(0<=y_husky<=100):
                            x=14
                            y=28
                            return x,y,z                       
                        # Lateral Inferior Direita
                        if(140<=y_husky<=240):
                            x=14
                            y=-20
                            return x,y,z                       
                        #Lateral Meio Direita
                        else:
                            x=14
                            y=8
                            return x,y,z                       
                    #Lateral Esquerda (superior,meio,inferior)
                    if(0 <= x_husky <= 140):
                        # Lateral Superior Esquerda
                        if(0<=y_husky<=100):
                            x=-28
                            y=28
                            return x,y,z                       
                        # Lateral Inferior Direita
                        if(140<=y_husky<=240):
                            x=-28
                            y=-20       
                            return x,y,z  
                        #Lateral Meio Direita                     
                        else:
                            x=-28
                            y=8
                            return x,y,z     
                    #Meio                
                    else:
                        x=0
                        y=8
                        return x,y,z 
                    #return x,y,z              
                except Exception as e:
                    #continue
                    x=0
                    y=0
                    z=0  #flag para colocar os olhos do robo em modo aleatorio
                    return x, y, z              
                except KeyboardInterrupt:
                    print("\nQUITING")
                    break
                    quit()


# def printObjectNicely(obj):
#     count=1

#     #SE FOR UMA LISTA DE OBJETOS
#     if(type(obj)==list):
#         for i in obj:
#             print("\t "+ ("BLOCK_" if i.type=="BLOCK" else "ARROW_")+str(count)+" : "+ json.dumps(i.__dict__))
#             count+=1
    
#     #SE FOR UM UNICO OBJETO
#     else:
#         #print("\t "+ ("BLOCK_" if obj.type=="BLOCK" else "ARROW_")+str(count)+" : "+ json.dumps(obj.__dict__))
#         print("(x,y): " + str(obj.x) + ", " + str(obj.y) )
#         #+ " | Width: " + str(obj.width) + " | Height: " + str(obj.height) + " | ID: " + str(obj.ID) + " | Type: " + str(obj.type) + " | Angle: " + str(obj.angle) + " | Confidence: " + str(obj.confidence) + " |")

