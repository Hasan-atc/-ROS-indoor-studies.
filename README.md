# ROS-indoor-studies.
Hello researchers. In this project, I will present my works that I have done in real environment and gazebo simulation environment using Turtlebot3 and Turtlebot2. Many systems such as mapping, positioning, use of sensor data are explained in the project.


![ezgif com-gif-maker](https://user-images.githubusercontent.com/74008306/183645587-671d7a6b-ccf2-4266-ab20-527f4ff657f3.gif)

# Requirements 💻
``` Ubuntu 20.04 (I used this version)```

``` ROS Noetic ```

``` Turtlebot3  or Turtlebot2```

``` Python and My choice Spyder IDE ```


# Initialization ⭐
!! Before starting this phase, you should make sure that the above requirements are fully met !!

!! After installing ROS and Turtlebot3, do not forget to make catkin_make in the catkin_ws file !!

!!Then you can locate the labirent_ortam.launch file wherever you want and run it with roslaunch. I preferably put it in turtlebot3_simulations/turtlebot3_gazebo/launch file !!

1️⃣ Let's run the Gazebo environment
````
cd catkin_ws
rosluanch turtlebot3_gazebo labirent_ortam.launch
````
2️⃣ Let's do mapping through Rviz

Turtlebot2 :  
````
-> roslaunch turtlebot_navigation gmapping_demo.launch
-> roslaunch turtlebot_rviz_launchers view_navigation.launch (Don't forget to replace the map in view_navigation.launch with your own map's .yaml file.)
-> roslaunch turtlebot_teleop turtlebot_teleop_key.launch
````

Turtlebot3 :
````
-> roslaunch turtlebot3_bringup turtlebot3_robot.launch
-> roslaunch turtlebot3_slam turtlebot3_slam.launch
-> roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
````

<img width="520" alt="Ekran Resmi 2022-08-09 12 26 57" src="https://user-images.githubusercontent.com/74008306/183614635-b5b51b56-cf69-4a07-96b4-532eba9a0b3f.png">

3️⃣ Save the map
Turtlebot3 and Turtlebot2 :
````
$ rosrun map_server map_saver -f ~/map
````
<img width="178" alt="Ekran Resmi 2022-08-09 12 30 13" src="https://user-images.githubusercontent.com/74008306/183615289-2901ff61-ab11-43d8-baf7-97befe44dfef.png">


# Using the extracted Map 🗺️
````
roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/map.yaml  (Show the location of the map you saved)
````

# Navigation Algorithm 🤖
First of all, in this project, I keep my codes under the catkin_ws/src/codes/scripts file. You can find the pyqt5 design files in the ui_file file.
````
roslaunch turtlebot3_gazebo labirent_ortam.launch
roslaunch turtlebot3_navigation turtlebot3_navigation.launch (Don't forget to replace the map in view_navigation.launch with your own map's .yaml file.)
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch (The robot needs to go around a full turn in order to fully understand its location)
````
````
cd catkin_ws/src/codes/scripts
chmod +x robot_control.py
python3 robot_control.py (If you are using Python 3.x version)
python robot_control.py (If you are using Python 2.x version)
````
<img width="991" alt="Ekran Resmi 2022-08-09 14 29 27" src="https://user-images.githubusercontent.com/74008306/183636859-97386050-c0e6-4309-bc79-a34deef54de1.png">


# Finish 🔚
After completing the task assigned to the robot, it will send feedback to the place where Tour Information is written. 
You are now ready to use the system 🎊 🎊 🎊

# Resources 🤝
✔️ https://emanual.robotis.com/docs/en/platform/turtlebot3/navigation/

✔️ https://www.ros.org/

✔️ https://gist.github.com/jeremyfix/0c5973aba508ee8b6e8d3c3077c6db1e (Noetic install Turtlebot2)

# Coming Soon 🥇
✅ Fleet management : I will be working on multiple robots.

✅ Full coverage path planner : I will have the robot go to each point of the map in one go.
