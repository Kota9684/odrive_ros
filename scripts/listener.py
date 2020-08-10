#!/usr/bin/env python
# coding: utf-8
import rospy
from std_msgs.msg import String
#odriveのパッケージを読み込む
import odrive
from odrive.enums import *
#その他の利用パッケージ
import time

#起動しているodriveを見つけて太郎と名付ける
taro=odrive.find_any()
print("太郎発見・セットアップします") 
time.sleep(10)
#キャリブレーションする
taro.axis1.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE
time.sleep(20)
#閉ループ回路に設定する
taro.axis1.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
time.sleep(10)
#コントロールモードを指定
taro.axis1.controller.config.control_mode=CTRL_MODE_VELOCITY_CONTROL
time.sleep(10)
#ポジションゲインを10に設定する
taro.axis1.controller.config.pos_gain = 10.0
time.sleep(10)
print("太郎準備完了")


def callback(data):
    #subscriberのID　rospy.get_caller_id()
    #subscrineしたデータの中身　data.data
    rospy.loginfo(rospy.get_caller_id() + 'データきたー %s', data.data)

    #太郎の制御
    taro.axis1.controller.vel_setpoint=int(data.data)

def listener():
    #おまじない　ノード名を宣言
    rospy.init_node('listener', anonymous=True)
    #Subscriberを作成．トピックを読み込む．
    rospy.Subscriber('chatter', String, callback)

    #コールバック関数を繰り返す．
    rospy.spin()

if __name__ == '__main__':
    listener()
