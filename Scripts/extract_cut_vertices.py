import bpy
import bmesh
from mathutils import Vector, Matrix

context = bpy.context
scene = context.scene
viewlayer = context.view_layer
ob = context.object
me = ob.data
bm = bmesh.new()
bm.from_mesh(me)
scale_factor = 0.1
c  = sum((Vector(b) for b in ob.bound_box), Vector()) / 8   

proj = Vector((0, 1, 0)).normalized()
T = Matrix.Translation(-c)
S = Matrix.Scale(0, 4, proj)
verts = [v for v in bm.verts if v.normal.dot(proj) > 0]
bmesh.ops.transform(bm, matrix=S, verts=verts, 
        space=Matrix.Translation(-c - scale_factor * proj))
bmesh.ops.transform(bm, matrix=S, verts=list(set(bm.verts) - set(verts)), 
        space=Matrix.Translation(-c + scale_factor * proj))

test = bmesh.ops.bisect_plane(bm, geom=bm.verts[:] + bm.edges[:] + bm.faces[:],
        plane_co=c,
        plane_no=proj,
        clear_inner=True,
        clear_outer=True)
		
[x.co for x in test['geom_cut'] if type(x) is bmesh.types.BMVert]
