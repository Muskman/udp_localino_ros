#!/usr/bin/python
import socket
from udp_localino_ros.msg import localino
import rospy
UDP_IP= ""
UDP_PORT=10000

def process(data,pub):
    localino_msg = localino()
    res = data.split(",")
    anchor_id_num = int(res[0]) % 2000
    tag_id_num = int(res[1]) % 1000
    dist = float(res[2])

    localino_msg.header.stamp = rospy.Time.now()
    localino_msg.header.frame_id = "localino"
    localino_msg.Anchor_Number = anchor_id_num
    localino_msg.Tag_Number = tag_id_num
    localino_msg.AT_dist = dist

    pub.publish(localino_msg)

if __name__ == "__main__":
    rospy.init_node("Localino_Node")
    pub = rospy.Publisher("localino_distances", localino , queue_size = 1)
    rospy.loginfo("Starting Localino node")
    sock = socket.socket(socket.AF_INET ,  socket.SOCK_DGRAM)
    sock.bind((UDP_IP,UDP_PORT))
    while True:
        data, addr = sock.recvfrom(1024)
        process(data,pub)

