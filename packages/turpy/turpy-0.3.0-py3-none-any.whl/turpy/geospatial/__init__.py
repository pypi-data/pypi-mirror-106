from osgeo import gdal
import rasterio
import geopandas as gpd
from shapely.geometry import Point
from typing import Union, Callable, List, Tuple
import logging
import os


logging.basicConfig(
    format=' % (asctime)s | %(name)s | %(levelname)s | %(message)s', level=40)



def geometry_centroids(
    gdf:gpd.GeoDataFrame,
    round_up_crs_list:list = ['EPSG:3006', 'EPSG:3035'] )-> List[Tuple[Point]]:
    """Returns the `centroids` of the input `GeoDataFrame`.
    WARNING: Do not add `EPSG:4326` (WGS84) or non projected coordinate systems 
    into the `round_up_crs_list` as it will decrease precision.

    The function will roundup to the nearest meter if the GeoDataFrame `crs` 
    is in the `round_up_crs_list`.

    Args:
        gdf (gpd.GeoDataFrame): [description]
        round_up_crs_list (list, optional): [description]. Defaults to ['EPSG:3006', 'EPSG:3035'].

    Returns:
        List[Tuple[Point]]: [description]
    """

    assert 'geometry' in gdf.columns
    assert gdf.crs is not None
        
    # Try to assess if we need to round up the
    if gdf.crs in round_up_crs_list:
        # NOTE: we round-up to nearest meter
        # Check type of centroids, is it a GeoSeries of Points or just a List of Points
        centroids = gdf['geometry'].apply( lambda p: Point(int(round(p.centroid.x)), int(round(p.centroid.y))))        
    else:         
        centroids = gdf['geometry'].apply( lambda p: Point(p.centroid.x, p.centroid.y))
       
    return centroids


def load_single_raster(raster_filepath:str, *args, **kwargs):
    """utility generator function to load rasters using rasterio. 
    To be used in combination with decorators.

    Args:
        raster_filepath (str): [description]

    Yields:
        [Rasterio dataset]: Dataset
    """
    assert os.path.isfile(raster_filepath)

    with rasterio.open(fp=raster_filepath, *args, **kwargs) as dataset:
        yield dataset


def extract_raster_values(xy_tuples: List[Point]):
    """Decorator to extract one or multiple raster values based on a list of `Point` `xy_tuples`.
    Expects as dataset generated from the `load_single_raster` function.

    Args:
        xy_tuples (List[Point]): [description]

    Returns:
        [List]: List of values at xy_tuples sampled Points

    The Coordinate Reference System (CRS) of the `xy_tuple` must match rasters CRS.
    """

    assert xy_tuples is not None
    assert isinstance(xy_tuples, List[Point])
    # assert isinstance(xy_tuples[0], Point)

    def get_dataset_values(func):
        def wrapper(raster_filepath, *args, **kwargs):
            extracted_values = []
            for dataset in func(raster_filepath, *args, **kwargs):
                value_generator = dataset.sample(xy_tuples)
                try:
                    for values in value_generator:
                        _value = list(values)[0]
                        extracted_values.append(_value)
                        logging.info(values)
                except Exception as msg:
                    _value = None
                    logging.exception(msg)
                return extracted_values # _value
        return wrapper
    return get_dataset_values



def extract_raster_value_at_point(raster_filepath:str, xy_tuple:tuple)->Union[float,int]:
    """Extracts raster value at point with xy_tuple coordinates, using rasterio. 

    The Coordinate Reference System (CRS) of the `xy_tuple` must match rasters CRS.
    """
    assert os.path.isfile(raster_filepath)

    with rasterio.open(raster_filepath) as dataset:
        value_generator = dataset.sample([xy_tuple])

        try:
            for values in value_generator:
                extracted_value = list(values)[0]
        except Exception as msg:
            extracted_value = None
            logging.exception(msg)
        return extracted_value