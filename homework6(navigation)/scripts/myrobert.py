#!/usr/bin/env python

"""
    myrobert.py
    
"""

import rospy, os, sys
from std_msgs.msg import String
from sound_play.libsoundplay import SoundClient
from opencv_apps.msg import FaceArrayStamped
from opencv_apps.msg import RotatedRectStamped
from opencv_apps.msg import Face
from opencv_apps.msg import Rect
from opencv_apps.msg import RotatedRect
from opencv_apps.msg import Point2D


class MyRobert:
    def __init__(self, script_path):
        rospy.init_node('myrobert')

        rospy.on_shutdown(self.cleanup)
       
        self.soundhandle = SoundClient(blocking=True)
        
        # Wait a moment to let the client connect to the sound_play server
        rospy.sleep(1)
        
        # Make sure any lingering sound_play processes are stopped.
        self.soundhandle.stopAll()
        
       
        rospy.loginfo("Ready, waiting for commands...")
	self.soundhandle.say('Hello, I am PartyBot. What can I do for you?')
	#rospy.sleep(2)
       

        rospy.loginfo("Say one of the navigation commands...")

        # Subscribe to the recognizer output and set the callback function
        rospy.Subscriber('/lm_data', String, self.talkback)

        self.navi = rospy.Publisher("/navi_to_point", String, queue_size=10) 

        # Subscribe to the navigation result
        self.navigation_back=""
        rospy.Subscriber('/navigation_feed_point', String, self.naviback)

    def naviback(self, res):
         self.navigation_back=res.data

    def talkback(self, msg):
        # Print the recognized words on the screen
        #msg.data=msg.data.lower()
        rospy.loginfo(msg.data)     

	if msg.data.find('GOOD MORNING')>-1:
		self.soundhandle.say("hi,nice to meet you!")
	elif msg.data.find('YOUR NAME')>-1:
		self.soundhandle.say("I heard you ask about my name. My name is curry",volumn=0.2)
	elif msg.data.find('HOW OLD ARE YOU')>-1:
		self.soundhandle.say("I heard you ask about my age. I am five years old.",volumn=0.2)
	elif msg.data.find('ARE YOU FROM')>-1:
		self.soundhandle.say("I heard you ask about my hometown. I am from China.",volumn=0.2)
	elif msg.data.find('CAN YOU DO')>-1:
		self.soundhandle.say("I heard you ask me what can I do? I am a home robot. I am good at singing and dancing.",volumn=0.2)
	elif msg.data.find('TELL A JOKE')>-1:
		self.soundhandle.say("ok. What is orange and sounds like a parrot? Erm, It is a carrot. Ha ha ha",volumn=0.2)	
	elif msg.data.find('GO-TO-THE-BOOKSHELF')>-1:
             rospy.loginfo("I am going to the bookshelf.")
             self.soundhandle.say("I am going to the bookshelf.", volume=0.2)
             self.navi.publish('go to the bookshelf')
             while (True):
                 if self.navigation_back == "Reached the bookshelf":
                     self.soundhandle.say("I reached the bookshelf.", volume=0.2)
                     break
             #rospy.sleep(5)
	elif msg.data.find('GO TO THE BEDROOM')>-1:
             rospy.loginfo("I am going to the bedroom.")
             self.soundhandle.say("I am going to the bedroom.", volume=0.2)
             self.navi.publish('go to the bedroom')
             while (True):
                 if self.navigation_back == "reached the bedroom":
                     self.soundhandle.say("I reached the bedroom.", volume=0.2)
                     break
             #rospy.sleep(5)
	elif msg.data.find('GO TO THE KITCHEN')>-1:
             rospy.loginfo("I am going to the kitchen.")
             self.soundhandle.say("I am going to the kitchen.", volume=0.2)
             self.navi.publish('go to the kitchen')
             while (True):
                 if self.navigation_back == "reached the kitchen":
                     self.soundhandle.say("I reached the kitchen.", volume=0.2)
                     break
             #rospy.sleep(5)
	elif msg.data.find('GO TO THE TABLE')>-1:
             rospy.loginfo("I am going to the table.")
             self.soundhandle.say("I am going to the table.", volume=0.2)
             self.navi.publish('go to the table')
             while (True):
                 if self.navigation_back == "reached the table":
                     self.soundhandle.say("I reached the table.", volume=0.2)
                     break
             #rospy.sleep(5)
	elif msg.data.find('TALKING TO ME')>-1:
		self.soundhandle.say("you are welcome.see you next time!",volumn=0.2)
            	#rospy.sleep(1)

    def cleanup(self):
        self.soundhandle.stopAll()
        rospy.loginfo("Shutting down partybot node...")

if __name__=="__main__":
    try:
        MyRobert(sys.path[0])
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo("MyRobert node terminated.")
