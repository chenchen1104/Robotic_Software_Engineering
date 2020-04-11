此程序包将语音交流与人脸检测结合起来，实现拍照功能。

1、功能详述<br>
首先向机器人发布“take photo”的语音命令，机器人识别到语音做出反映，开始进行拍照。机器人检测到人脸的位置后，会判断人脸的位置是否位于图片的正中央。如果偏下，机器人会说：Sorry, you are a little lower than my camera.偏上、偏左、偏右机器人同样会提醒。<br>

2、所用节点<br>
（1）myrobert : 主结点，实现人机语音交互，接受“take photo”的命令，并完成拍照功能<br>
（2）audio_control : 语音识别<br>
（3）soundplaynode : 语音输出<br>
（4）usb_cam ：调用摄像头<br>
（5）take_photo_sub ： 实现拍照功能<br>
（6）face_detection ： 进行人脸检测<br>

节点间的关系另附图片
