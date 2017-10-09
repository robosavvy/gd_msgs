#!/usr/bin/env python
# -*- coding: latin-1 -*-
import rospy
import os.path

#Ros
from std_msgs.msg import *
#~ from ctt_manager_msgs.msg import *
#~ from ctt_manager_msgs.srv import *
from time import sleep
import std_srvs.srv
import gd_msgs.msg
import gd_msgs.srv

global height_pub
global center_pub
global height
global center
global input_cmd


pub_matA = None
pub_matB = None
pub_matK = None
pub_matL = None
height_cm = 0

def readFile():
    global pub_matA
    global pub_matB
    global pub_matK
    global pub_matL
    global file_directory
    global height_cm
    
    if not os.path.exists("./matrices.txt"):
        print "Error - the matrices.txt file is not in gd_scripts directory"
        exit(1)
    matrixArray = [line.rstrip('\n') for line in open("matrices.txt", 'r')]
    
    if len(matrixArray) != 5:
        print "Error - The matrices.txt file is not correct"
        exit(1)
    
    for matS in xrange(0,len(matrixArray)):
        matSArray = matrixArray[matS].split(',')
        f = []
        for value_mat in matSArray:
            try:
                f.append(float(value_mat.replace(" ", "")))
            except:
                print "Error - The matrices.txt file is not correct"
                exit(1)
            
        my_array_for_publishing = Float32MultiArray(data=f)
            
        if matS == 0:
            if len(f) != 7:
                print "Error - The matrices.txt file is not correct"
                exit(1)
            pub_matA.publish(my_array_for_publishing)
        elif matS == 1:
            if len(f) != 22:
                print "Error - The matrices.txt file is not correct"
                exit(1)
            pub_matB.publish(my_array_for_publishing)
        elif matS == 2:
            if len(f) != 16:
                print "Error - The matrices.txt file is not correct"
                exit(1)
            pub_matK.publish(my_array_for_publishing)
        elif matS == 3:
            if len(f) != 20:
                print "Error - The matrices.txt file is not correct"
                exit(1)
            pub_matL.publish(my_array_for_publishing)
        elif matS == 4:
            if len(f) != 2:
                print "Error - The matrices.txt file is not correct"
                exit(1)
            height_cm = (f[0] + f[1])/2
            
        f = [] #clear matrix again

    
def main():
    global height_pub
    global center_pub
    global height
    global center
    global input_cmd
    global pub_matA
    global pub_matB
    global pub_matK
    global pub_matL
    global isReset
    global height_cm
    
    #~ rospy.init_node('db_manager', anonymous=True)
    rospy.init_node('configure_params')

    #configure publishers
    #~ pub_session = rospy.Publisher("/db/current_session", String, queue_size=10)
    height_pub = rospy.Publisher("/cmd_height", std_msgs.msg.Float32, queue_size=10)
    center_pub = rospy.Publisher("/calib_center", std_msgs.msg.Float32, queue_size=10)
    
    pub_matA = rospy.Publisher("/matrixA", Float32MultiArray, queue_size=10)
    pub_matB = rospy.Publisher("/matrixB", Float32MultiArray, queue_size=10)
    pub_matK = rospy.Publisher("/matrixK", Float32MultiArray, queue_size=10)
    pub_matL = rospy.Publisher("/matrixL", Float32MultiArray, queue_size=10)
    
    #configure services
    #~ id_alert_srv = rospy.ServiceProxy('/db/open_alert', ctt_manager_msgs.srv.AlertId)
    #~ srv_rsp = id_alert_srv(json_data)
    set_input_srv = rospy.ServiceProxy('/set_input', gd_msgs.srv.SetInput)
    init_balance_srv = rospy.ServiceProxy('/init_balance', std_srvs.srv.Empty)
    
    
    #Init
    rospy.sleep(0.2)
    readFile()
    height_pub.publish(height_cm)
    #print height_cm
    center_pub.publish(center) 
    #call services
    # from PC
    rospy.sleep(2)
    set_input_rsp = set_input_srv(input_cmd)
    # from RC
    #~ srv_rsp = set_input_srv({data: 1})
    init_balance_rsp = init_balance_srv()
     
    
    rospy.sleep(2) 
    
    #~ rospy.spin()
    

if __name__ == '__main__':

    if len(sys.argv) == 3:
        #height = float(sys.argv[1])
        center = float(sys.argv[1])
        input_cmd = float(sys.argv[2])
    else: 
        print "Error - The script needs 2 argv: <IMU-Calibration> <PC(0)/RC(1)>"
        sys.exit(1)
    main()


