这是一个利用gazebo和rviz进行导航仿真的ros包，相关依赖包为turtle机器人包<br>

实现功能：通过语音控制机器人，使其到达预先设定的四个地点。<br>

(1)launch文件夹下有2个文件：_world.launch用于启动gazebo界面并加载环境；navibot2.launch用于启动机器人语音和导航的相关结点。<br>

(2)scripts文件夹下有2个文件：myrobert.py定义navibot结点调用语音控制相关结点，实现与机器人的语音交互；navigation.py定义了导航结点navi_point，实现自主导航功能。

(3)maps文件夹下包含3个文件：my_map.pgm和my_map.yaml，是机器人扫描生成的地图文件。<br>


navibot结点和navi_point结点的通信：/navi_to_point话题 和 /navigation_feed_point话题<br>
