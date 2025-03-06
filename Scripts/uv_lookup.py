
"""
Find UV values of points in a shape based on X and Y point values.

Z values of points returned are limited to max_point_z.
"""

import math

def read_s_file(s_filepath):
    """
    Reads the contents of a shape file encoded in UTF-16.
    
    Args:
        s_filepath (str): The path to the shape file.
    
    Returns:
        str: The content of the file as a string.
    """
    with open(s_filepath, 'r', encoding='utf-16') as s_file:
        return s_file.read()


def parse_s_file(s_text):´
    """
    Parses the content of a shape file and extracts 3D model data including points, UV points, UV index mapping.
    
    Args:
        s_text (str): The content of the shape file.
    
    Returns:
        tuple: A tuple containing:
            - points (list of tuples): A list of 3D coordinate points.
            - uv_points (list of tuples): A list of 2D UV coordinates.
            - normals (list of tuples): A list of normal vectors.
            - uv_idx_mapping (dict): A dictionary mapping point indices to UV indices.
    """
    tokenized_lines = []
    points = []
    uv_points = []
    normals = []
    current_dlevel = 0
    uv_idx_mapping = {}
    
    for line in s_text.split("\n"):
        tokens = line.replace("\t", "").split(" ")
        if "\t\tpoint ( " in line:
            tokenized_lines.append(tokens)
        if "\t\tuv_point ( " in line:
            tokenized_lines.append(tokens)
        if "\t\tvector ( " in line:
            tokenized_lines.append(tokens)
        if "\t\t\t\t\tdlevel_selection ( " in line:
            tokenized_lines.append(tokens)
        if "\t\t\t\t\t\tsub_object ( " in line:
            tokenized_lines.append(tokens)
        if "\t\t\t\t\t\t\tvertex ( " in line:
            tokenized_lines.append(tokens)
        if "\t\t\t\t\t\t\t\tvertex_uvs ( " in line:
            tokenized_lines.append(tokens)
        if "\t\t\t\t\t\t\t\tvertex_idxs ( " in line:
            tokenized_lines.append(tokens)
        if "\t\t\t\t\t\t\t\tnormal_idxs ( " in line:
            tokenized_lines.append(tokens)

    for line in tokenized_lines:
        if line[0] == "point":
            points.append((float(line[2]), float(line[3]), float(line[4])))
        if line[0] == "uv_point":
            uv_points.append((float(line[2]), float(line[3])))
        if line[0] == "vector":
            normals.append((float(line[2]), float(line[3]), float(line[4])))
        if line[0] == "dlevel_selection":
            current_dlevel = int(line[2])
        if line[0] == "sub_object":
            pass
        if line[0] == "vertex" and current_dlevel == lod_distance:
            next_line_idx = tokenized_lines.index(line) + 1
            if next_line_idx:
                next_line = tokenized_lines[next_line_idx]
                if next_line[0] == "vertex_uvs":
                    point_idx = line[3]
                    uv_idx = int(next_line[3])
                    uv_idx_mapping.update({point_idx: uv_idx})
        if line[0] == "vertex_idxs" and current_dlevel == lod_distance:
            pass
        if line[0] == "normal_idxs" and current_dlevel == lod_distance:
            pass
    
    return points, uv_points, normals, uv_idx_mapping



if __name__ == "__main__":
    s_filepath = "D:\\Games\\Open Rails\\Tools\\sfm\\DB2s.s"
    max_point_z = 0.0
    lod_distance = 500
    
    s_text = read_s_file(s_filepath)
    
    points, uv_points, normals, uv_idx_mapping = parse_s_file(s_text)

    print("\n\nShape: %s" % (s_filepath))
    print("Distance level: %d" % (lod_distance))
    print("\t%d points in shape." % (len(points)))
    print("\t%d uv points in shape.\n\n" % (len(uv_points)))
    print("Only returning points with Z value less than or equal to %f.\n\n" % (max_point_z))

    while True:
        print("Enter X and Y value to search with one space in between:")
        point_xy = input()
        point_x = float(point_xy.split(" ")[0])
        point_y = float(point_xy.split(" ")[1])
        print("\n\n")
        
        distances = [math.sqrt(((x - point_x) ** 2) + ((y - point_y) ** 2)) for (x, y, z) in points]
        
        indexed_list = list(enumerate(distances))
        indexed_list = [x for x in indexed_list if points[x[0]][2] <= max_point_z]
        sorted_list = sorted(indexed_list, key=lambda x: x[1])
        smallest_items = sorted_list[:5]
        
        print("\n\nShape: %s" % (s_filepath))
        print("Distance level: %d" % (lod_distance))
        print("\t%d points in shape." % (len(points)))
        print("\t%d uv points in shape.\n\n" % (len(uv_points)))
        print("Only returning points with Z value less than or equal to %f.\n\n" % (max_point_z))
        print("Closest points:")
        for index, distance in smallest_items:
            uv_idx = uv_idx_mapping.get(str(index))
            if uv_idx is not None:
                distance_result = f"{distance:.4f}"
                point_result = ', '.join(f"{value:.4f}" for value in points[index])
                uv_point_result = ', '.join(f"{(1 + value):.4f}" for value in uv_points[uv_idx])
                print("\tDistance: %s\tPoint: (%s)\t\tUV: (%s)\t" % (distance_result, point_result, uv_point_result))
        print("\n\n")