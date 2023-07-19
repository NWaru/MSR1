#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def plot_belief(belief):
    
    plt.figure()
    
    ax = plt.subplot(2,1,1)
    ax.matshow(belief.reshape(1, belief.shape[0]))
    ax.set_xticks(np.arange(0, belief.shape[0],1))
    ax.xaxis.set_ticks_position("bottom")
    ax.set_yticks([])
    ax.title.set_text("Grid")
    
    ax = plt.subplot(2, 1, 2)
    ax.bar(np.arange(0, belief.shape[0]), belief)
    ax.set_xticks(np.arange(0, belief.shape[0], 1))
    ax.set_ylim([0, 1.05])
    ax.title.set_text("Histogram")


def motion_model(action, belief):
    # add code here
    if action == 'F':
        p1, p2, p3 = 0.7, 0.2, 0.1
    elif action == 'B':
        p1, p2, p3 = 0.1, 0.2, 0.7

    belief[0] = p2*belief[0] + p3*belief[1]
    belief[len(belief)-1] = p1*belief[len(belief)-2] + p2*belief[len(belief)-1]
    for i in range(1, len(belief)-1):
        belief[i] = p1*belief[i-1] + p2*belief[i] + p3*belief[i+1]

    return belief
    
# def sensor_model(observation, belief, world):
    # add code here

# def recursive_bayes_filter(actions, observations, belief, world):
    # add code here
