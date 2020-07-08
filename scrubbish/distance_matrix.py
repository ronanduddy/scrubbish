import config
from .request import Request

class DistanceMatrix:
    def __init__(self, origin):
        self.distance_matrix_url = config.DISTANCE_MATRIX_URL
        self.api_key = config.DISTANCE_MATRIX_API_KEY
        self.modes = ['driving', 'bicycling']

        self.city_hall = 'Belfast City Hall, Search Results Donegall Square N, Belfast BT1 5GS'
        self.boulder_world = 'Boulder World, Unit 1 Boucher Business Centre, Apollo Rd, Belfast BT12 6HP'

        self.origin = origin
        self.request = Request(self.distance_matrix_url)

    @classmethod
    def to_h(cls, distance_matrix):
        result = {}
        for mode in distance_matrix:
            elements = distance_matrix[mode]['rows'][0]['elements']

            city_hall = elements[0]
            result[f'to_city_hall_{mode}_distance'] = city_hall['distance']['text']
            result[f'to_city_hall_{mode}_duration'] = city_hall['duration']['text']

            boulder_world = elements[1]
            result[f'to_boulder_world_{mode}_distance'] = boulder_world['distance']['text']
            result[f'to_boulder_world_{mode}_duration'] = boulder_world['duration']['text']

        return result

    def get(self, dry_run=True):
        mode_distance_matrix = {}
        for mode in self.modes:
            params = {
                'mode': mode,
                'units':'imperial',
                'origins': self.origin,
                'destinations': self._destinations(),
                'key': self.api_key
            }

            if dry_run:
                mode_distance_matrix[mode] = {'dry': 'run'}
            else:
                sleep = .200
                self.request.params = params
                response = self.request.get(sleep)
                mode_distance_matrix[mode] = response.json()

        return mode_distance_matrix

    def _destinations(self):
        return '|'.join([self.city_hall, self.boulder_world])
