from mesh_to_sdf import mesh_to_voxels

import os
import trimesh
import skimage
import skimage.measure

# Showing specific model in specific folder
folder = '02818832'
model = '10c15151ebe3d237240ea0cdca7b391a'

filename = os.path.join('data', folder, model, 'models', 'model_normalized.obj')
mesh = trimesh.load(filename)
voxels = mesh_to_voxels(mesh, 64, pad=True)

vrtcs, fcs, nrmls, _ = skimage.measure.marching_cubes_lewiner(voxels, level=0)
mesh = trimesh.Trimesh(vertices=vrtcs, faces=fcs, vertex_normals=nrmls)
mesh.show()
