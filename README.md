
# Generative Grasping CNN (GG-CNN)

The GG-CNN is a lightweight, fully-convolutional network which predicts the quality and pose of antipodal grasps at every pixel in an input depth image.  The lightweight and single-pass generative nature of GG-CNN allows for fast execution and closed-loop control, enabling accurate grasping in dynamic environments where objects are moved during the grasp attempt.

This repository contains the implementation of the Generative Grasping Convolutional Neural Network (GG-CNN) from the paper:

**Closing the Loop for Robotic Grasping: A Real-time, Generative Grasp Synthesis Approach**

*[Douglas Morrison](http://dougsm.com), [Peter Corke](http://petercorke.com), [Jürgen Leitner](http://juxi.net)*

Robotics: Science and Systems (RSS) 2018

[arXiv](https://arxiv.org/abs/1804.05172) | [Video](https://www.youtube.com/watch?v=7nOoxuGEcxA)

If you use this work, please cite:

```text
@inproceedings{morrison2018closing,
	title={{Closing the Loop for Robotic Grasping: A Real-time, Generative Grasp Synthesis Approach}},
	author={Morrison, Douglas and Corke, Peter and Leitner, J\"urgen},
	booktitle={Proc.\ of Robotics: Science and Systems (RSS)},
	year={2018}
}
```

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

