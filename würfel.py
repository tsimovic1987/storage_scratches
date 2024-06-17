import bpy
import math
import random

# Funktion, um eine Würfel-Animation zu erstellen
def animate_rolling_cube(cube_name):
    # Objekt aus der Szene referenzieren
    cube = bpy.data.objects.get(cube_name)
    if cube is None:
        print(f"Object named '{cube_name}' not found.")
        return

    # Setzen Sie den Start- und Endframe
    start_frame = 1
    end_frame = 15
    
    # Zufällige Endrotation und Position
    end_rotation = (
        math.radians(random.uniform(0, 720)),  # X-Rotation
        math.radians(random.uniform(0, 720)),  # Y-Rotation
        math.radians(random.uniform(0, 720))   # Z-Rotation
    )
    end_position = (
        random.uniform(-5, 5),  # X-Position
        random.uniform(-5, 5),  # Y-Position
        0                       # Z-Position (auf dem Boden)
    )
    
    # Setzen Sie die Startposition und -rotation (in der Luft)
    cube.location = (0, 0, 5)
    cube.rotation_euler = (0, 0, 0)
    cube.keyframe_insert(data_path="location", frame=start_frame)
    cube.keyframe_insert(data_path="rotation_euler", frame=start_frame)
    
    # Setzen Sie die Endposition und -rotation (auf dem Boden, zufällig rotiert)
    cube.location = end_position
    cube.rotation_euler = end_rotation
    cube.keyframe_insert(data_path="location", frame=end_frame)
    cube.keyframe_insert(data_path="rotation_euler", frame=end_frame)
    
    # Zwischenframes für realistischere Animation
    mid_frame = (start_frame + end_frame) // 2
    cube.location = (
        (cube.location[0] + end_position[0]) / 2,
        (cube.location[1] + end_position[1]) / 2,
        10  # kurz in die Luft
    )
    cube.rotation_euler = (
        end_rotation[0] / 2,
        end_rotation[1] / 2,
        end_rotation[2] / 2
    )
    cube.keyframe_insert(data_path="location", frame=mid_frame)
    cube.keyframe_insert(data_path="rotation_euler", frame=mid_frame)

# Animation für den vorhandenen Würfel mit dem Namen "Cube" hinzufügen
animate_rolling_cube("Cube")