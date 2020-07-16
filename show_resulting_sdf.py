from mesh_to_sdf import sample_sdf_near_surface

import os
import trimesh
import pyrender
import pandas as pd
import numpy as np

#mesh = trimesh.load('chair.obj')
#points, sdf = sample_sdf_near_surface(mesh, number_of_points=250000)

# getting resulting points
folder = '02818832'
model = '10c15151ebe3d237240ea0cdca7b391a'

df = pd.read_csv(os.path.join('data', folder, model, 'models', 'result.csv'))
df = df[df['sdf'] > 0.01]

points = df[['x', 'y', 'z']].to_numpy()
sdf = df['sdf'].to_numpy()

colors = np.zeros(points.shape)
colors[sdf < 0, 2] = 1
colors[sdf > 0, 0] = 1
cloud = pyrender.Mesh.from_points(points, colors=colors)
scene = pyrender.Scene()
scene.add(cloud)
viewer = pyrender.Viewer(scene, use_raymond_lighting=True, point_size=2)
