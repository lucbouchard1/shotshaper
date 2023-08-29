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


masses = np.linspace(0.1, 0.2, 50)
distances = []
release_vels = []

# Plot trajectory
pl.figure(1)
cmap = matplotlib.colormaps['viridis']

for mass in masses:
    speed = np.sqrt(2 * initial_energy / mass)
    release_vels.append(speed)

    d = DiscGolfDisc('dd2', mass=mass)
    shot = d.shoot(speed=speed, omega=omega, pitch=pitch, 
                position=pos, nose_angle=nose, roll_angle=roll)

    x,y,z = shot.position
    pl.plot(x,y, c=cmap((mass/0.2) - 0.1))

    # Plot other parameters
    arc,alphas,betas,lifts,drags,moms,rolls = d.post_process(shot, omega)
    distances.append(arc[-1])

pl.title("Top Down of Flight")
pl.xlabel('Distance (m)')
pl.ylabel('Drift (m)')
pl.axis('equal')
sm = pl.cm.ScalarMappable(cmap=cmap, norm=pl.Normalize(vmin=0.1, vmax=0.2))
cbar = pl.colorbar(sm, ax=pl.gca())
cbar.set_label('Disc Mass (Kg)', rotation=270)

pl.figure()

pl.subplot(2, 1, 1)
pl.plot(masses, distances)
pl.ylabel("Distance (m)")
pl.subplot(2, 1, 2)
pl.ylabel("Release Speed (m/s)")
pl.plot(masses, release_vels)
pl.xlabel('Mass (Kg)')
pl.show()