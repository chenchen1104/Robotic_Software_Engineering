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

        #the position of face detected
        self.face_x=0
        self.face_y=0
        # Subscribe to the face_detection output
        rospy.Subscriber('/face_detection/faces', FaceArrayStamped, self.face_back)
  
        # the center of blue object
        self.blue_x = 0
        self.blue_width = 0
        # Subscribe to the blue_tracting output
        rospy.Subscriber('/camshift/track_box', RotatedRectStamped, self.blue_back)

        #Publish to the take_photo topic to use take_photo node
        self.take_photo = rospy.Publisher("/take_photo", String, queue_size=10)

    def blue_back(self,blue_data):
        self.blue_x = blue_data.rect.center.x 
        self.blue_width = blue_data.rect.size.width
             
    def face_back(self,face_data):
        pos = face_data.faces
        if pos:
            self.face_x=pos[0].face.x
            self.face_y=pos[0].face.y

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
	elif msg.data.find('TELL ME A JOKE')>-1:
		self.soundhandle.say("ok. What is orange and sounds like a parrot? Erm, It is a carrot. Ha ha ha",volumn=0.2)	
	elif msg.data.find('TAKE PHOTO')>-1:
             rospy.loginfo("Talkbot: OK, please stand in front of me and look at my eyes.")
             self.soundhandle.say("OK, please stand in front of me and look at my eyes.", volume=0.2)
             #rospy.sleep(1)
             while(True):
                 if self.face_x<240 and self.face_x>0:
                     if self.face_y<160 and self.face_y>0:
                         rospy.loginfo("Talkbot: Please lower your head and stand a little to the left.")
                         self.soundhandle.say("Please lower your head and stand a little to the left.", volume=0.2)
                     elif self.face_y>300:
                         rospy.loginfo("Talkbot: Sorry, you are a little lower than my camera, please stand up, and stand a little to the left.")
                         self.soundhandle.say("Sorry, you are a little lower than my camera, please stand up, and stand a little to the left.", volume=0.2)
                     else:
                         rospy.loginfo("Talkbot: Please stand a little to the left.")
                         self.soundhandle.say("Please stand a little to the left.", volume=0.2)
                     self.face_x=0 
                     self.face_y=0
                     rospy.sleep(1)
                 elif self.face_x>420:
                     if self.face_y<160 and self.face_y>0:
                         rospy.loginfo("Talkbot: Please lower your head and stand a little to the right.")
                         self.soundhandle.say("Please lower your head and stand a little to the right.", volume=0.2)
                     elif self.face_y>300:
                         rospy.loginfo("Talkbot: Sorry, you are a little lower than my camera, please stand up, and stand a little to the right.")
                         self.soundhandle.say("Sorry, you are a little lower than my camera, please stand up, and stand a little to the right.", volume=0.2)
                     else:
                         rospy.loginfo("Talkbot: Please stand a little to the right.")
                         self.soundhandle.say("Please stand a little to the right.", volume=0.2)
                     self.face_x=0
                     self.face_y=0
                     rospy.sleep(1)
                 elif self.face_x>=240 and self.face_x<=420:
                     if self.face_y<160 and self.face_y>0:
                         rospy.loginfo("Talkbot: Please lower your head.")
                         self.soundhandle.say("Please lower your head.", volume=0.2)
                         self.face_x=0
                         self.face_y=0
                         rospy.sleep(1)
                     elif self.face_y>300:
                         rospy.loginfo("Talkbot: Sorry, you are a little lower than my camera, please stand up.")
                         self.soundhandle.say("Sorry, you are a little lower than my camera, please stand up.", volume=0.2)
                         self.face_x=0
                         self.face_y=0
                         rospy.sleep(1)
                     else:
                         rospy.loginfo("Talkbot: OK, please don't move.")
                         self.soundhandle.say("OK, please don't move.", volume=0.1)
                         break
                 elif self.face_x==0 or self.face_y==0:
                     rospy.loginfo("Talkbot: I can't catch your face, please stand and face to me.")
                     self.soundhandle.say("I can't catch your face, please stand and face to me.", volume=0.2)
             rospy.loginfo("Talkbot: 3! 2! 1!")
             self.soundhandle.say("3! 2! 1!", volume=0.2)
             self.take_photo.publish("take photo")
             rospy.loginfo("Talkbot: You can see this photo.")
             self.soundhandle.say("You can see this photo.", volume=0.2)

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
