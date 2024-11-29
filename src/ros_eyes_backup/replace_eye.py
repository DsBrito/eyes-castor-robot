#!/usr/bin/env python

import os
import rospy
import time
from std_msgs.msg import String
from geometry_msgs.msg import Point
from std_msgs.msg import Bool

class eyesNode(object):
	def _init_(self, name):
		self.name = name
		rospy.init_node(self.name)
		self.rate = rospy.Rate(10) # 10hz
		self.initSubscribers()
		self.initVariables()

	def initSubscribers(self):
		self.subEmotions = rospy.Subscriber('/emotions', String, self.callbackEmotions)
		self.subStopTalk = rospy.Subscriber('/stopTalk', Bool, self.callbackStopTalk)
		self.blinkSub = rospy.Subscriber("/blink", Bool, self.blink_callback)
		self.crazyEyesSub = rospy.Subscriber("/crazyEyes", Bool, self.crazy_eyes_callback)
        self.moveEyes_s = rospy.Subscriber("/moveEyes", Point, self.moveEyes_callback)
		return

	def initVariables(self):
		while not os.path.exists('/tmp/conf.txt'):
			pass

		with open('/tmp/conf.txt', 'r') as file:
			self.eyesConfig = file.readlines()
        	# print(self.eyesConfig)
		self.changeEmotions = False
		self.stopTalk = Bool()
		self.emotionsDict = {
		"happy": self.set_happy,
		"sad": self.set_sad,
		"surprise": self.set_surprise,
		"angry": self.set_angry,
		"neutral": self.set_neutral,
		"talk": self.talk
		}
		return
		
        
    def husky(self,x,y,z):
		self.eyesConfig[0] = str(size_pupils) + '\n'
		self.eyesConfig[1] = 'False\n'
		self.eyesConfig[2] = 'False\n'
		self.eyesConfig[3] = str(x) + '\n'
		self.eyesConfig[4] = str(y) + '\n'
		with open('/tmp/conf.txt', 'w') as file:
			file.writelines(self.eyesConfig)
		return
	# Emotions
	def set_happy(self):
		x = 0
		y = 8
		size_pupils = 0.7
		self.eyesConfig[0] = str(size_pupils) + '\n'
		self.eyesConfig[1] = 'False\n'
		self.eyesConfig[2] = 'False\n'
		self.eyesConfig[3] = str(x) + '\n'
		self.eyesConfig[4] = str(y) + '\n'
		with open('/tmp/conf.txt', 'w') as file:
			file.writelines(self.eyesConfig)
		return

	def set_sad(self):
		x = 0
		y = -20
		size_pupils = 0.4
		self.eyesConfig[0] = str(size_pupils) + '\n'
		self.eyesConfig[1] = 'False\n'
		self.eyesConfig[2] = 'False\n'
		self.eyesConfig[3] = str(x) + '\n'
		self.eyesConfig[4] = str(y) + '\n'
		with open('/tmp/conf.txt', 'w') as file:
			file.writelines(self.eyesConfig)
		return

	def set_surprise(self):
		x = 0
		y = 15
		size_pupils = 0.3
		self.eyesConfig[0] = str(size_pupils) + '\n'
		self.eyesConfig[1] = 'False\n'
		self.eyesConfig[2] = 'False\n'
		self.eyesConfig[3] = str(x) + '\n'
		self.eyesConfig[4] = str(y) + '\n'
		with open('/tmp/conf.txt', 'w') as file:
			file.writelines(self.eyesConfig)
		return

	def set_angry(self):
		x = 0
		y = 0
		size_pupils = 0.5
		self.eyesConfig[0] = str(size_pupils) + '\n'
		self.eyesConfig[1] = 'False\n'
		self.eyesConfig[2] = 'False\n'
		self.eyesConfig[3] = str(x) + '\n'
		self.eyesConfig[4] = str(y) + '\n'
		with open('/tmp/conf.txt', 'w') as file:
			file.writelines(self.eyesConfig)
		return

	def set_neutral(self):
		self.eyesConfig[1] = 'True\n'
		self.eyesConfig[2] = 'True\n'
		with open('/tmp/conf.txt', 'w') as file:
			file.writelines(self.eyesConfig)
		return
	
	def talk(self):
		self.eyesConfig[0] = str(msg.data) + '\n'
		self.eyesConfig[1] = 'False\n'
		self.eyesConfig[2] = 'False\n'
		self.eyesConfig[3] = str(msg.x) + '\n'
		self.eyesConfig[4] = str(msg.y) + '\n'
		with open('/tmp/conf.txt', 'w') as file:
			file.writelines(self.eyesConfig)
		return

	def callbackEmotions(self, msg):
		self.emotion = msg.data
		self.changeEmotions = True
		return
        
    def moveEyes_callback(self, msg):
		self.moveEyes = msg.data
		self.changePosition = True
		return

	def callbackStopTalk(self, msg):
		self.stopTalk = msg.data
		return

	def blink_callback(self, msg):
		if msg.data:
			self.eyesConfig[5] = 'True\n'
		else:
			self.eyesConfig[5] = 'False\n'
		with open('/tmp/conf.txt', 'w') as file:
			file.writelines(self.eyesConfig)
		return

	def crazy_eyes_callback(self, msg):
		if msg.data:
			self.eyesConfig[6] = 'True'
		else:
			self.eyesConfig[6] = 'False'
		with open('/tmp/conf.txt', 'w') as file:
			file.writelines(self.eyesConfig)
		return

	def main(self):
		rospy.loginfo("[%s] ROS Eyes node started ok", self.name)
		while not (rospy.is_shutdown()):
			if self.changeEmotions:
				self.set_neutral()
				if self.emotion == "talk":
					self.stopTalk = False
				self.emotionsDict[self.emotion]()
				self.changeEmotions = False
		self.rate.sleep()
		return

if _name_ == '_main_':
	eyes = eyesNode("eyesNode")
	eyes .main()