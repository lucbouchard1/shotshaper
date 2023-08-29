# -*- coding: utf-8 -*-
"""
Example showing a single disc throw.
"""

from shotshaper.projectile import DiscGolfDisc
import matplotlib.pyplot as pl
from matplotlib import cm
import matplotlib
import numpy as np

baseline_velocity = 24.2
initial_energy = 0.5 * 0.17 * (baseline_velocity**2) # Use kinetic energy from 170 gram disc at 24.2 m/s
omega = 116.8
z0 = 1.3
pos = np.array((0,0,z0))
pitch = 15.5
nose = 0.0
roll = 14.7


masses = np.linspace(0.05, 0.3, 100)
release_vels = np.linspace(15, 35, 50)
optimal_masses = []

for speed in release_vels:
    optimal_mass = 0
    optimal_distance = 0
    last_distance = 0
    for mass in masses:
        d = DiscGolfDisc('dd2', mass=mass)
        shot = d.shoot(speed=speed, omega=omega, pitch=pitch, 
                    position=pos, nose_angle=nose, roll_angle=roll)

        arc,alphas,betas,lifts,drags,moms,rolls = d.post_process(shot, omega)

        if arc[-1] > optimal_distance:
            optimal_distance = arc[-1]
            optimal_mass = mass
    
        if last_distance > arc[-1]:
            break # Can stop searching when distances start decreasing
        last_distance = arc[-1]

    optimal_masses.append(optimal_mass)

pl.plot(release_vels * 2.23694, np.array(optimal_masses)*1000)
pl.xlabel("Release Velocity (mph)")
pl.ylabel("Optimal Disc Mass (g)")
pl.show()