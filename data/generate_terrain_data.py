import pandas as pd
import numpy as np

num_points = 100

latitudes = np.random.uniform(34.00, 34.10, num_points)   
longitudes = np.random.uniform(-118.30, -118.20, num_points)  

elevations = np.random.uniform(50, 200, num_points) + 10 * np.sin(latitudes * 10)  

terrain_data = pd.DataFrame({
    "latitude": latitudes,
    "longitude": longitudes,
    "elevation": elevations
})

terrain_data.to_csv("data/terrain_data.csv", index=False)

print("✅ Terrain data generated and saved to 'data/terrain_data.csv'")