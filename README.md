
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

## Datasets

Currently, both the [Cornell Grasping Dataset](http://pr.cs.cornell.edu/grasping/rect_data/data.php) and
[Jacquard Dataset](https://jacquard.liris.cnrs.fr/) are supported.

### Cornell Grasping Dataset

1. Download the and extract [Cornell Grasping Dataset](http://pr.cs.cornell.edu/grasping/rect_data/data.php). 
2. Convert the PCD files to depth images by running `python -m utils.dataset_processing.generate_cornell_depth <Path To Dataset>`

### Jacquard Dataset

1. Download and extract the [Jacquard Dataset](https://jacquard.liris.cnrs.fr/).




## Running on a Robot

Our ROS implementation for running the grasping system see [https://github.com/dougsm/mvp_grasp](https://github.com/dougsm/mvp_grasp).

The original implementation for running experiments on a Kinva Mico arm can be found in the repository [https://github.com/dougsm/ggcnn_kinova_grasping](https://github.com/dougsm/ggcnn_kinova_grasping).


# The largest heading

The grasping algorithm can be run through the jupyter notebook ./catkin_ws/testbook.ipynb. A detailed discussion of the algorithm is included in the Report.pdf (not finished)

A HSR instance (simulation or real robot) needs to be running first. 

MiDas contains he depth estimation model

ggcnn contains the grasp prediction model
