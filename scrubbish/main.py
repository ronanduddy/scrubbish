#!/usr/bin/python

# from .. import config
print(f"__file__={__file__}")
print(f"__name__={__name__}")
print(f"__package__={str(__package__)}")

import sys
import utils
from json_helper import JsonHelper


def default():
    areas = {"belfast": "belfast"}

    area_uris = utils.get_area_uris(areas)
    utils.print_uris(area_uris)
    JsonHelper("area_uris").dump(area_uris)
    utils.write_csv(area_uris)


def continue_scrape():
    start_area = sys.argv[1]
    start_index = sys.argv[2]
    json_file = sys.argv[3]
    csv_file = sys.argv[4]

    area_uris = JsonHelper(json_file).read()
    utils.continue_csv(area_uris, start_area, start_index, csv_file)


def build_distance_matrix():
    csv_file = sys.argv[1]
    json_file = sys.argv[2]
    # distance_matrix = utils.get_distances(filename)
    # JsonHelper('distance_matrix').dump(distance_matrix)
    utils.write_distances(csv_file, json_file)


if len(sys.argv) == 3:
    build_distance_matrix()
elif len(sys.argv) == 5:
    continue_scrape()
else:
    default()
