# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 15:07:31 2019

@author: Matthew Ma
"""

import numpy as np
import numpy.random as nprd
import matplotlib.pyplot as plt
import imageio

N = 1000
steps = 100
A = [[0,1],[0,1]]          #range of length,range of width
A0 = [[0, 1.0/2],[0,1]]    #initial range of length,range of width
ini_x = nprd.uniform(A0[0][0],A0[0][1],N)
ini_y = nprd.uniform(A0[1][0],A0[1][1],N)
particles = np.array([[ini_xi,ini_yi] for ini_xi,ini_yi in zip(ini_x,ini_y)])
ds = 0.05
filenames = []

#画隔板
range_of_wall = list(np.linspace(A[1][0],A[1][1],1000)[:451])+list( np.linspace(A[1][0],A[1][1],1000)[551:])
wall = np.array([(A[0][1]/2,i) for i in range_of_wall])
plt.plot(wall[:,0],wall[:,1],'c.')
plt.axis([0,1,0,1])

#模拟粒子运动
hole_lobd = wall[450,1] #lower bound of the hole
hole_upbd = wall[451,1] #upper bound of the hole
for step in range(steps):
    for particle in particles:
        p = nprd.random()
        if p < 0.25:
            particle[0] -= ds
            if particle[0] < A[0][0]:
                particle[0] = A[0][0] + ds
        elif p < 0.5:
            particle[0] += ds
            if particle[1] < hole_lobd or  particle[1] > hole_upbd:
                particle[0] = A[0][1]/2 - nprd.uniform(0,0.05)
            if particle[0] > A[0][1]:
                particle[0] = A[0][1] - ds
        elif p < 0.75:
            particle[1] -= ds
            if particle[1] < A[1][0]:
                particle[1] = A[1][0] + ds
        else:
            particle[1] += ds
            if particle[1] > A[1][1]:
                particle[1] = A[1][1] - ds
    plt.plot(particles[:,0],particles[:,1],'r.',)
    plt.axis([0,1,0,1])
    plt.title('Position of particles at step #%d'%(step+1))
    filename = 'step%3d.jpg'%(step+1)
    plt.savefig(filename) 
    filenames.append(filename)

outfilename = 'movement_of_gas_particles.gif'        
frames = []
for image_name in filenames:
    im = imageio.imread(image_name)           # 读取方式上存在略微区别，由于是直接读取数据，并不需要后续处理
    frames.append(im)
imageio.mimsave(outfilename, frames, 'GIF', duration=0.1)