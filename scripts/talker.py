#!/usr/bin/env python
# coding: utf-8
import rospy
from std_msgs.msg import String

def talker():
    #Publisherを作成('トピック名',型,サイズ)
    pub = rospy.Publisher('chatter', String, queue_size=10)
    #おまじない　ノード名の宣言
    rospy.init_node('talker', anonymous=True)
    #ループの周期．
    rate = rospy.Rate(10) 
    
    print("0: right, 1:left")

    while not rospy.is_shutdown():
        #標準入力からkeyを入力
        key=input()
        msg =str()

        #keyによって指令値を決める
        if key =='0':
            msg = '3000'
    
        elif key =='1':
            msg = '-3000'

        print("0: right, 1:left")
        #指令値を記録する
        #rospy.loginfo(msg)
        #指令値をパブリッシュする
        pub.publish(msg)
        rate.sleep()
    

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
