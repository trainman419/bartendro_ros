#!/usr/bin/env python

import rospy
from bartendro_msgs.msg import *

class DriverBackend:

    def __init__(self, uri):
        self.uri = uri
        # TODO: initialize some sort of HTTP library

    def get_ingredients(self):
        # stub
        return []

    def get_drinks(self):
        # stub
        return []

    def dispense(self, drink_id, progress_callback=None):
        # stub
        return None

class Driver:

    def __init__(self, uri, backend=DriverBackend):
        self.backend = backend(uri)
        self.ingredient_pub = rospy.Publisher("~ingredients", Ingredients, 
            latch=True)
        self.drink_pub = rospy.Publisher("~drinks", Drinks, latch=True)

        # TODO: register actionlib server for dispense
        # TODO: start up a thread to do run()

    def run(self):
        while not rospy.is_shutdown():
            rospy.sleep(1)
            self.ingredient_pub.publish(self.backend.get_ingredients())
            self.drink_pub.publish(self.backend.get_drinks())

if __name__ == '__main__':
    rospy.init_node('bartendro')
    driver = Driver("http://127.0.0.1")
    driver.run()
