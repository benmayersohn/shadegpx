import gpxpy
import numpy as np
import pysolar.solar as solar
from datetime import timedelta

def shade_factor(lat_deg, lon_deg, dx, dy, t):
    altitude = np.pi * solar.get_altitude(lat_deg, lon_deg, t) / 180.
    azimuth = np.pi * solar.get_azimuth(lat_deg, lon_deg, t) / 180.
    theta_a = np.zeros(dx.shape)
    theta_a[dx >= 0] = np.arctan2(dy[dx >= 0], dx[dx >= 0])
    theta_a[dx < 0] = np.pi - np.arctan2(dy[dx < 0], np.abs(dx[dx < 0]))
    return 0.5 * (1 - np.sin(theta_a + azimuth)) * np.cos(altitude)

def shade_calc(filename, start_time, end_time):

    # open GPX
    with open(filename) as the_file:
        gpx = gpxpy.parse(the_file)

    # we will compute a vector of directions by using gpx coordinates
    points = gpx.tracks[0].segments[0].points
    num_trackpoints = len(points)
    lat_deg = np.array([points[i].latitude for i in range(num_trackpoints)])
    lon_deg = np.array([points[i].longitude for i in range(num_trackpoints)])
    lats = np.pi * lat_deg / 180.
    lons = np.pi * lon_deg / 180.
    elevations = np.array([points[i].elevation for i in range(num_trackpoints)])  # in meters

    # convert elevations to miles
    # these are insignificant
    elevations *= 0.000621371
    de = np.zeros_like(elevations)
    de[:-1] = elevations[1:] - elevations[:-1]
    de[-1] = de[-2]

    earth_radius = 3963  # miles

    lat_avg = (lats[0] + lats[-1]) / 2

    # this is the most important thing
    # where is sun coming from relative to point?
    dlat = np.zeros_like(lats)
    dlon = np.zeros_like(lons)
    dlat[:-1] = lats[1:] - lats[:-1]
    dlon[:-1] = lons[1:] - lons[:-1]
    dlon[-1] = dlon[-2]
    dlat[-1] = dlat[-2]

    dx = dlon * earth_radius * np.cos(lat_avg)
    dy = dlat * earth_radius

    x = np.zeros_like(lats)
    y = np.zeros_like(lons)
    miles = np.zeros_like(lats)
    colors = np.zeros_like(lats)

    spacing = 1  # in minutes

    d = timedelta(minutes=spacing)
    for i in range(1, len(x)):
        x[i] = x[i-1] + dx[i-1]
        y[i] = y[i-1] + dy[i-1]
        miles[i] = miles[i-1] + np.sqrt(dx[i-1]**2 + dy[i-1]**2 + de[i-1]**2)

    colors = list()
    time = start_time
    mins = list()
    count = 0
    while (time < end_time):
        current_shade = shade_factor(lat_deg, lon_deg, dx, dy, time)
        colors.append(current_shade.tolist())
        time += d
        mins.append(count * spacing)  # minutes
        count += 1
    
    avg_color = np.mean(colors, axis=0)

    return x, y, avg_color