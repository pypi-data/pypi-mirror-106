import numpy as np
import geopandas as gpd
from shapely.geometry import Polygon



def hexagon_corners(center, w):
    """
    w -> distance_between polygons (width in the pointy arrangement)
    https://github.com/McJazzy/hexagonpy/blob/master/image.py
    """
    #x = center[0]
    #y = center[1]
    
    # he inner radius is equal to (sqrt(3) /2) times the outer radius
    #inner_radius = (math.sqrt(3) / 2) * size
    # w = 2*inner_radius
    # w = distance_between_hexagons
    # size = (distance_between_hexagons / 2) / math.sqrt(3)
     
    size = w / np.sqrt(3)
    h = 2 * size
    
    angles_in_radians = np.deg2rad([60 * i + 30 for i in range(6)])
    x = center[0] + size * np.cos(angles_in_radians)
    y = center[1] + size * np.sin(angles_in_radians)
    
    ## points = np.round(np.vstack([x, y]).T)
    corners_points = np.vstack([x, y]).T
    return corners_points
    

    #return [ 
    #    (x - w / 2, y - h / 4),
    #    (x, y - h /2),
    #    (x + w/2, y - h / 4),
    #    (x + w/2, y + h/4),
    #    (x, y + h/2),
    #    (x - w / 2, y + h/4)
    #]

    

def rectangle_corners(center, w, h):
    x = center[0]
    y = center[1]

    return [
        (x - w/2, y - h/2),
        (x + w/2 , y - h/2),
        (x +w/2, y + h/2),
        (x -w /2, y + h/2)
    ]



def build_hexagon_grid(roi:gpd.GeoDataFrame, seed_point:tuple, distance_between_hexagons: int = 500)->gpd.GeoDataFrame:
    """Generates an hexagon grid, starting from the seed_point (x,y) 
    
    :params roi:
    :params seed_point:
    :params distance_between_hexagons: Equals to the width of a pointy hexagon.
    
    """
    
    w = distance_between_hexagons
    # size = (distance_between_hexagons / 2) / math.sqrt(3)
    hexagon_size = w / np.sqrt(3)
    h = 2 * hexagon_size
    
    roi_width = int(roi.bounds['maxx'][0]) - int(roi.bounds['minx'][0])
    roi_height = int(roi.bounds['maxy'][0]) - int(roi.bounds['miny'][0])
    # 'width: {}, height: {}'.format(roi_width, roi_height)
    
    # number of hexagons horizontally and vertically
    # The size is given as a 2-tuple (width, height)
    num_hor = int(roi_width / w) + 2
    num_ver = int(roi_height / h * 4 / 3) + 2
    num_hor, num_ver

    #
    hexes = []
    for j in range(-num_ver, num_ver):
        for i in range(0, num_hor): # num_hor*num_ver
            column = i % num_hor
            row = j # i // num_hor
            even = row % 2  # the even rows of hexagons has w/2 offset on the x-axis compared to odd rows.    

            p = Polygon(hexagon_corners(( (column*w + even * w/2)+ seed_point[0], (row*h * 3/4)+seed_point[1]), w = w))
            if p.centroid.within(roi.unary_union):    # roi.envelope.unary_union    
                hexes.append(p)

        for i in range(1, num_hor): # num_hor*num_ver
            column = i % num_hor * -1
            row = j # i // num_hor
            even = row % 2  # the even rows of hexagons has w/2 offset on the x-axis compared to odd rows.    

            p = Polygon(hexagon_corners(( (column*w + even * w/2)+ seed_point[0], (row*h * 3/4)+seed_point[1]), w = w))
            if p.centroid.within(roi.unary_union):        
                hexes.append(p)
    # hexagon_grid            
    return gpd.GeoDataFrame(index=range(0, len(hexes)), crs=roi.crs, geometry=hexes)


def generate_random_seed_point_within_polygon(roi:gpd.GeoDataFrame)->tuple:
    """
    Generate one random.uniform seed, within the roi polygon.
    Used to feed the `seed_point` to the hexagon grid.
    
    return
    """
    x_min, y_min, x_max, y_max = roi.total_bounds
    # set sample size
    n = 1
    gdf_points = None
    is_in_polygon = False
    while not is_in_polygon:
        # We iterate as the random ppoint may fall outside the target polygon but within its boundaries.
        # generate random data within the bounds, assumes Euclidean distances.
        x = np.random.uniform(x_min, x_max, n)
        y = np.random.uniform(y_min, y_max, n)

        # convert them to a points GeoSeries
        gdf_points = gpd.GeoSeries(gpd.points_from_xy(x, y))
        # only keep those points within polygons
        gdf_points = gdf_points[gdf_points.within(roi.unary_union)]
        if len(gdf_points)>0:
            is_in_polygon = True
    # '{}, {}'.format(int(gdf_points[gdf_points.keys()[0]].x), int(gdf_points[gdf_points.keys()[0]].y))
    return (int(gdf_points[gdf_points.keys()[0]].x), int(gdf_points[gdf_points.keys()[0]].y))