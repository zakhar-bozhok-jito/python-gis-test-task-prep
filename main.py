import geopandas as gpd
import matplotlib.pyplot as plt
import random

def create_subplot():
    _, axes = plt.subplots(figsize=(12, 12))
    return axes

def render_axes(axes, title, output_path):
    axes.set_title(title, fontsize=14)
    plt.grid(True)
    plt.savefig(output_path, dpi=600, bbox_inches='tight')
    print(f"Plotted sublines saved as {output_path}")

def get_random_color():
    return (random.random(), random.random(), random.random())

def plot_sublines(gdf: gpd.GeoDataFrame, output_path: str = None):
    axes = create_subplot()
    for _, row in gdf.iterrows():
        if row.geometry.geom_type == "LineString":
            for i in range(len(row.geometry.xy[0]) - 1):
                axes.plot(
                    [row.geometry.xy[0][i], row.geometry.xy[0][i+1]], 
                    [row.geometry.xy[1][i], row.geometry.xy[1][i+1]], 
                    color=get_random_color(), 
                    linewidth=2
                )
    render_axes(axes, f"Visualization of {output_path} - all sublines", output_path)

def plot_lines_as_is(gdf: gpd.GeoDataFrame, output_path: str = None):
    axes = create_subplot()
    for _, row in gdf.iterrows():
        if row.geometry.geom_type == "LineString":
            axes.plot(
                row.geometry.xy[0],
                row.geometry.xy[1],
                color=get_random_color(),
                linewidth=2
            )
    render_axes(axes, f"Visualization of {output_path} - lines as they are", output_path)

if __name__ == "__main__":
    # Example of how to read & visualize a shapefile.
    # Given shapefile has line objects, which consist of multiple sublines.
    # Below code will plot each subline separately and all lines as they are.
    # Current code renders the shapefile into .png files.
    gdf = gpd.read_file("sample/roads.shp")
    plot_sublines(gdf, "output/sublines.png")
    plot_lines_as_is(gdf, "output/lines.png")