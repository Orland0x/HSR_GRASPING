#Loading grasp variables
import csv
import numpy as np


def get_grasp(grasp_file):
    
    with open(grasp_file,'r') as f: 
        Reader=csv.reader(f) 
        rows=list(Reader)
        grasp = rows[-1]

    depth = float(grasp[1])
    u = int(grasp[2])
    v = int(grasp[3])
    angle = float(grasp[4])
    width = float(grasp[5])

    top = 138
    left = 228
    #Switching back to uncropped coordinates
    #max_pixel = ((480-300)/2 + int(u), (640-300)/2 + int(v))
    max_pixel = (top+int(u), left+int(v))

    #Defining Camera intrinsic parameters in image pixel space
    f_x = 205.47
    f_y = 205.47
    c_x = 240.5
    c_y = 320.5

    depth=0.2
    #Transforming grasp from 2D image space to 3D camera space
    x = (max_pixel[0] - c_x)/(f_x) * depth
    y = (max_pixel[1] - c_y)/(f_y) * depth
    z = depth
    width = width/(f_x) * depth
    camera_p = np.array([x,y,z,1]).transpose() #defined in homogenous coordinates
    #print(x,y,z,angle)



    #Transforming from 3D image space to the palm of the hand coordinate system using extrinsic camera parameters.
    #Tranform obtained via command - rosrun tf tf_echo hand_camera_frame hand_palm_link
    Rt_matrix = np.array([[1,0,0,-0.039],[0,1,0,0],[0,0,1,0.004],[0,0,0,1]])
    grasp_position_homogenous = np.matmul(Rt_matrix,camera_p)

    #convert from homogenous to cartesian:
    grasp_position = grasp_position_homogenous[0:3]
    #append angle and width
    grasp_vector = np.append(grasp_position, [angle, width])
    return grasp_vector