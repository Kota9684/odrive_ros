# odrive_ros
[ODrive motor](https://odriverobotics.com/)を動かすROSパッケージ．  
位置制御と速度制御の切り替え，指令値の送信． 位置と速度のリアルタイムプロット．
[![](https://img.youtube.com/vi/7yh7Y6mzf2o/0.jpg)](https://www.youtube.com/watch?v=7yh7Y6mzf2o)

# 環境
1. [Ubuntu 16.04 LTS](https://wiki.ubuntu.com/XenialXerus/ReleaseNotes/Ja#Ubuntu_16.04.2BMG4wwDCmMPMw7TD8MMk-)
2. [ROS kinetic](http://wiki.ros.org/ja/kinetic/Installation/Ubuntu)
3. [odrive 0.4.12](https://pypi.org/project/odrive/)

# 使い方
1. [ROSワークスペースの作成](http://wiki.ros.org/ja/ROS/Tutorials/InstallingandConfiguringROSEnvironment)
```
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
catkin_init_workspace
cd ~/catkin_ws/
catkin_make
```
2. [odrive_rosリポジトリのクローン](https://git-scm.com/book/ja/v2/Git-%E3%81%AE%E5%9F%BA%E6%9C%AC-Git-%E3%83%AA%E3%83%9D%E3%82%B8%E3%83%88%E3%83%AA%E3%81%AE%E5%8F%96%E5%BE%97)
```
cd ~/catkin_ws/src
git clone clone URL
cd odrive_ros
pip install -e.
```
3. 起動
```
cd ~/catkin_ws
catkin_make #catkinパッケージをビルド
roscore 

#別のターミナルを開く
rosrun odrive_ros listener.py
#起動と同時にODriveの初期設定をする．(1分ぐらい待つ)
#太郎準備完了ってでたらOK

#別のターミナルを開く
rosrun odrive_ros talker.py
#ここで指令値および，制御方法の切り替えを行う
```
4. コマンド
- vel：速度制御に切替
- pos：位置制御に切替
- plot：位置と速度をプロット
- stop：停止

# 参考
- [ODrive Documentation](https://docs.odriverobotics.com/)
- [neomanic/odrive_ros](https://github.com/neomanic/odrive_ros)
- [Raspberry Pi Mouse Simulator's Tutorial](https://raspimouse-sim-tutorial.gitbook.io/project/)
- [ROS Melodic Moreniaを使ってPub/Subでサーボモータを動かす](https://tkrel.com/9301)

