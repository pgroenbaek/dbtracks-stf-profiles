import bpy

def get_selected_vertices():
    mode = bpy.context.active_object.mode
    bpy.ops.object.mode_set(mode='OBJECT')
    selected_verts = [v.co for v in bpy.context.active_object.data.vertices if v.select]
    print(selected_verts)
    bpy.ops.object.mode_set(mode=mode)

get_selected_vertices()