本程序包实现功能为：通过和机器人进行语音交流，利用gazebo和rviz进行导航仿真,使其到达预先设定的四个地点bookshelf,bedroom,kitchen,table。<br>
===============

本程序包包含四部分内容：<br>
--------------------------
(1)launch文件夹下有2个文件：turtlebot_world.launch用于启动gazebo内已经搭建好的环境；navigation.launch用于启动机器人语音和导航的相关结点。<br>
(2)scripts文件夹下有2个文件：myrobert.py定义myrobert结点调用语音控制相关结点，实现与机器人的语音交互；navigation.py定义了导航结点navi_point，实现自主导航功能。<br>
(3)maps文件夹下包含3个文件：my_map.pgm和my_map.yaml，是机器人扫描生成的地图文件。my_map.jpg是对地图中位置的含义进行解释。<br>
(4)myrobert文件夹是机器人的语音数据库。<br>

myrobert结点和navi_point结点的通信：/navi_to_point话题 和 /navigation_feed_point话题。<br>
----------------------------------------------------------------------------------------
（1）myrobert结点识别人的语音命令，向/navi_to_point话题发布命令，告知将要去的地址的名字。navi_point结点订阅该话题，使机器人前往目的地。<br>
（2）navi_point结点完成命令后，向/navigation_feed_point话题发布反馈信息，告知myrobert节点已经到达指定位置。<br>


终端运行命令：<br>
-----------------
roslaunch turtlebot_gazebo turtlebot_world.launch<br>
roslaunch turtlebot_rviz_launchers view_navigation.launch<br>
roslaunch turtlebot_gazebo amcl_demo.launch map_file:=/home/liuchenchen/my_map.yaml<br>
roslaunch rchomeedu_navigation  navigation.launch <br>
