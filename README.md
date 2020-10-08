# HSR Grasping
This algorithm allows a HSR robot to execute grasps of fine objects such as pens or cutlery using the hand RGB camera for feedback. The approach uses 2 fully convolutional neural networks, one to estimate a depth map, and the other to predict the optimal grasp from the depth map. These algorithms are elaborated on i more detail in the report pdf document.  

**Contact**

Any questions or comments contact [Orlando Fraser](mailto:orlando.fraser@oriel.ox.ac.uk).

## Installation

This code was developed with Python 3.6 on Ubuntu 18.04.  Python requirements can installed by:

```bash
pip install -r requirements.txt
```

## Running on the HSR simulation

An instance of the HSR simulation needs to be running first. The HSR simulation requires a Python 2 environment, so one need to activate that before launching.  We have provided a basic test setup that can be launched via:

```bash
roslaunch catkin_ws/launch/test_world.launch
```

We interact with the simulation via the Python API. A grasping pipeline has been developed for the test setup and can be executed through the jupyter notebook at ./catkin_ws/testbook.ipynb. This code can serve as as template, to be modified for any particular task where the grasping algorithm is required. 

## Demo

A video is attatched which shows a demo of the pipeline with the test environment. 
