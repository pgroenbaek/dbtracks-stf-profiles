import re

# TODO dlevel regex does not work, so don't even try using this. Getting the normals from the shape is not really necessary anyways.

def read_s_file(s_filepath):
    with open(s_filepath, 'r') as file:
        return file.read()

def parse_s_file(s_text):
    points_pattern = r'point\s*\(([^)]+)\)'
    uv_pattern = r'uv_point\s*\(([^)]+)\)'
    normals_pattern = r'vector\s*\(([^)]+)\)'

    lod_pattern = r'LOD\s*\{([^}]+)\}'
    vertex_pattern = r'vertex\s*\(([^)]+)\)'
    tris_idx_pattern = r'tristate_idx\s*\(([^)]+)\)'

    points = re.findall(points_pattern, s_text)
    uv_points = re.findall(uv_pattern, s_text)
    normals = re.findall(normals_pattern, s_text)
    lods = re.findall(lod_pattern, s_text)

    dlevels = parse_lod_controls(s_text)
    print(dlevels)

    points = [tuple(map(float, point.split())) for point in points]
    uv_points = [tuple(map(float, uv.split())) for uv in uv_points]
    normals = [tuple(map(float, normal.split())) for normal in normals]

    lod_data = []
    for lod in lods:
        vertices = re.findall(vertex_pattern, lod)
        tris_idx = re.findall(tris_idx_pattern, lod)
        lod_data.append({
            'vertices': [list(map(int, vertex.split())) for vertex in vertices],
            'tris_idx': [list(map(int, idx.split())) for idx in tris_idx],
        })
    return points, uv_points, normals, lod_data, dlevels

def parse_lod_controls(s_text):
    dlevel_pattern = r'dlevel_selection'#r'dlevel_selection\s*\(\s*(\d+)\s*\)'
    matches = re.findall(dlevel_pattern, s_text)
    dlevels = [int(match) for match in matches]

    return dlevels

def find_lod_for_dlevel(lod_data, dlevels, dlevel_selection):
    if dlevel_selection not in dlevels:
        raise ValueError(f"LOD for dlevel {dlevel_selection} not found.")

    if len(lod_data) != len(dlevels):
        raise ValueError(f"Mismatch between LOD data and dlevel data. Found {len(lod_data)} LODs and {len(dlevels)} dlevels.")
    
    lod_index = dlevels.index(dlevel_selection)
    return lod_data[lod_index]

def get_uv_and_normal_for_point(lod_data, uv_points, normals, points, point_index, dlevel_selection, dlevels):
    lod = find_lod_for_dlevel(lod_data, dlevels, dlevel_selection)
    
    if lod is None:
        raise ValueError(f"LOD for dlevel {dlevel_selection} not found.")
    
    if point_index < 0 or point_index >= len(points):
        raise IndexError("Point index out of range.")
    
    target_point = points[point_index]
    for vertex_index, vertex in enumerate(lod['vertices']):
        if target_point == tuple(points[i] for i in vertex):
            uv = uv_points[vertex_index] if vertex_index < len(uv_points) else None
            normal = normals[vertex_index] if vertex_index < len(normals) else None
            return uv, normal
    
    return None, None


if __name__ == "__main__":
    s_filepath = 'D:\\Games\\Open Rails\\Tools\\sfm\\DB3_a1t10mStrt.s'
    s_text = read_s_file(s_filepath)
  
    points, uv_points, normals, lod_data, dlevels = parse_s_file(s_text)

    dlevel_selection = 2000
    point_index = 4
    
    uv, normal = get_uv_and_normal_for_point(lod_data, uv_points, normals, points, point_index, dlevel_selection, dlevels)

    print(f"Point {point_index} at dlevel {dlevel_selection}")
    print(f"UV: {uv}")
    print(f"Normal: {normal}")