import pandas as pd
import numpy as np
import plotly.graph_objects as go
from scipy.interpolate import Rbf
from utils import load_data, apply_rotation

data = load_data('data/terrain_data.csv')

latitudes = data['latitude'].values
longitudes = data['longitude'].values
elevations = data['elevation'].values

rbf_functions = ["multiquadric", "inverse", "gaussian", "thin_plate"]

figs = []

for func in rbf_functions:
    rbf = Rbf(latitudes, longitudes, elevations, function=func, epsilon=2)

    lat_grid = np.linspace(min(latitudes), max(latitudes), 100)
    lon_grid = np.linspace(min(longitudes), max(longitudes), 100)
    Lat, Lon = np.meshgrid(lat_grid, lon_grid)

    Z = rbf(Lat, Lon)

    scatter = go.Scatter3d(
        x=latitudes, y=longitudes, z=elevations,
        mode='markers', marker=dict(size=5, color='red', opacity=0.8)
    )

    surface = go.Surface(
        x=Lat, y=Lon, z=Z,
        colorscale='Viridis', opacity=0.8
    )

    fig = go.Figure(data=[surface, scatter])
    fig.update_layout(
        title=f"RBF Interpolation ({func})",
        scene=dict(
            xaxis_title="Latitude",
            yaxis_title="Longitude",
            zaxis_title="Elevation"
        ),
        autosize=True
    )

    figs.append(fig)

for fig in figs:
    fig.show()