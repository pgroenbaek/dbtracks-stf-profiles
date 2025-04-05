import numpy as np

def calculate_normals(vertices):
    """
    Calculate the normal vectors for each segment between consecutive vertices.
    
    Parameters:
    vertices (list of tuple or list of list): A list of 2D points representing vertices.
    
    Returns:
    list of numpy.ndarray: A list of normal vectors for each segment.
    """
    normals = []
    num_vertices = len(vertices)
    
    for i in range(num_vertices - 1):
        p1 = np.array(vertices[i])
        p2 = np.array(vertices[i + 1])
        
        segment = p2 - p1
        normal = np.array([-segment[1], segment[0]])
        
        normal = normal / np.linalg.norm(normal)
        normals.append(normal)
    
    return normals


def calculate_vertex_normals(vertices, segment_normals):
    """
    Calculate the normal vectors for each vertex by averaging the adjacent segment normals.
    
    Parameters:
    vertices (list of tuple or list of list): A list of 2D points representing vertices.
    segment_normals (list of numpy.ndarray): A list of normal vectors for each segment.
    
    Returns:
    list of numpy.ndarray: A list of averaged normal vectors for each vertex.
    """
    num_vertices = len(vertices)
    vertex_normals = []
    
    is_closed = np.allclose(vertices[0], vertices[-1])
    
    for i in range(num_vertices):
        if i == 0:
            if is_closed:
                prev_normal = segment_normals[-1]
                next_normal = segment_normals[0]
                avg_normal = (prev_normal + next_normal) / 2
            else:
                avg_normal = segment_normals[0]
        elif i == num_vertices - 1:
            if is_closed:
                avg_normal = vertex_normals[0]
            else:
                avg_normal = segment_normals[-1]
        else:
            prev_normal = segment_normals[i - 1]
            next_normal = segment_normals[i]
            avg_normal = (prev_normal + next_normal) / 2
        
        avg_normal /= np.linalg.norm(avg_normal)
        vertex_normals.append(avg_normal)
    
    return vertex_normals



if __name__ == "__main__":
    polyline = [
        (-0.7450, 0.1850),
        (-0.6785, 0.1700)
    ]

    segment_normals = calculate_normals(polyline)
    vertex_normals = calculate_vertex_normals(polyline, segment_normals)

    print(vertex_normals)