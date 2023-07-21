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
    new_belief = np.zeros(len(belief))
    if action == 'F':
        p1, p2, p3 = 0.7, 0.2, 0.1
    else:
        p1, p2, p3 = 0.1, 0.2, 0.7

    new_belief[0] = p2*belief[0] + p3*belief[1]
    new_belief[len(belief)-1] = p1*belief[len(belief)-2] + p2*belief[len(belief)-1]
    for i in range(1, len(belief)-1):
        new_belief[i] = p1*belief[i-1] + p2*belief[i] + p3*belief[i+1]

    return new_belief
    
def sensor_model(observation, belief, world):
    # add code here
    p_white = 0.7
    p_black = 0.9

    p_hit, p_miss = (p_black, 1-p_white) if observation == 0 else (p_white, 1-p_black)
    eta = 0
    
    for i in range(len(world)):
        if world[i] == observation:
            belief[i] *= p_hit
        else:
            belief[i] *= p_miss
        eta += belief[i]

    return belief / sum(belief)

def recursive_bayes_filter(actions, observations, belief, world):
    # add code here
    belief = sensor_model(observations[0], belief, world)
    for i, action in enumerate(actions):
            belief = motion_model(actions[i], belief)
            belief = sensor_model(observations[i+1], belief, world)
    return belief
