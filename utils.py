import pandas as pd
import numpy as np
from scipy.spatial.transform import Rotation as R

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def apply_rotation(Lat, Lon, Z, angle_deg=45):
    rotation = R.from_euler('z', angle_deg, degrees=True)
    coords = np.vstack([Lat.flatten(), Lon.flatten(), Z.flatten()])
    rotated_coords = rotation.apply(coords.T)
    
    Lat_rotated = rotated_coords[:, 0].reshape(Lat.shape)
    Lon_rotated = rotated_coords[:, 1].reshape(Lon.shape)
    Z_rotated = rotated_coords[:, 2].reshape(Z.shape)
    
    return Lat_rotated, Lon_rotated, Z_rotated