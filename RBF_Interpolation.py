import pandas as pd
import numpy as np
import plotly.graph_objects as go
from scipy.interpolate import Rbf
from utils import load_data, apply_rotation

# Step 1: Load Terrain Data
data = load_data('data/terrain_data.csv')

latitudes = data['latitude'].values
longitudes = data['longitude'].values
elevations = data['elevation'].values

# Step 2: Apply RBF Interpolation
rbf = Rbf(latitudes, longitudes, elevations, function='multiquadric', epsilon=2)

# Create a grid of latitudes and longitudes for smooth interpolation
lat_grid = np.linspace(min(latitudes), max(latitudes), 100)
lon_grid = np.linspace(min(longitudes), max(longitudes), 100)
Lat, Lon = np.meshgrid(lat_grid, lon_grid)

# Interpolate the elevation values over the grid
Z = rbf(Lat, Lon)

# Step 3: Visualize the Results
scatter = go.Scatter3d(
    x=latitudes, y=longitudes, z=elevations,
    mode='markers', marker=dict(size=5, color='red', opacity=0.8)
)

# Create a 3D surface plot for the interpolated data
surface = go.Surface(
    x=Lat, y=Lon, z=Z,
    colorscale='Viridis', opacity=0.8
)

# Create the final figure
fig = go.Figure(data=[surface, scatter])

fig.update_layout(
    title="Terrain Modeling with RBF Interpolation",
    scene=dict(
        xaxis_title="Latitude",
        yaxis_title="Longitude",
        zaxis_title="Elevation"
    ),
    autosize=True
)

# Show the plot
fig.show()

# Optional: Apply Geometric Transformation (Rotation)
# Uncomment the following to see the rotated surface
# rotated_Lat, rotated_Lon, rotated_Z = apply_rotation(Lat, Lon, Z)
# rotated_surface = go.Surface(x=rotated_Lat, y=rotated_Lon, z=rotated_Z, colorscale='Viridis')
# fig_rotated = go.Figure(data=[rotated_surface, scatter])
# fig_rotated.show()