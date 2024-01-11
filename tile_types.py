from typing import Tuple

import numpy as np

"""
graphic data type consist of 
    ch: Character in integer format which will be translated to Unicode
    fg: foreground represented as 3 unsigned byte and are the RGB color code
    bg: background, same as foreground
"""
graphic_dt = np.dtype([
    ("ch", np.int32),
    ("fg", "3B"),
    ("bg", "3B")
])

"""
tile data type consist of
    walkable: True if a tile can walked over
    transparent: True if this tile does not block FOV
    dark: Graphics for when this tile is not in FOV
"""
tile_dt = np.dtype([
    ("walkable", np.bool),
    ("transparent", np.bool),
    ("dark", graphic_dt),
])
"""

"""
def new_tile(
    walkable: int,
    transparent: int,
    dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
)-> np.ndarray:
    return np.array((walkable, transparent, dark), dtype=tile_dt)

def new_tile(
        walkable: int,
        transparent: int,
        dark: Tuple[int, Tuple[int,int,int], Tuple[int, int, int]],
) -> np.ndarray:
    return np.array((walkable, transparent, dark), dtype=tile_dt)

floor = new_tile(
    walkable = True, transparent = True, dark=(ord(" ", (255, 255, 255),(50, 50, 150))),
)
wall = new_tile(
    walkable = False, transparent = False, dark=(ord(" "),(255, 255, 255),(0, 0, 100)),
)