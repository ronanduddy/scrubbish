import unittest
from unittest.mock import Mock
from unittest.mock import patch
from props.distance_matrix import DistanceMatrix

class TestDistanceMatrix(unittest.TestCase):
    def test_to_h(self):
        distance_matrix = {
            "driving": {
                "destination_addresses": [
                    "Donegall Square N, Belfast BT1 5GS, UK",
                    "Unit 1 Boucher Business Centre, Apollo Rd, Belfast BT12 6HP, UK"
                ],
                "origin_addresses": [
                    "x Portallo St, Belfast BT6 9BE, UK"
                ],
                "rows": [
                    {
                        "elements": [
                            {
                                "distance": {
                                    "text": "1.7 mi",
                                    "value": 2739
                                },
                                "duration": {
                                    "text": "8 mins",
                                    "value": 494
                                },
                                "status": "OK"
                            },
                            {
                                "distance": {
                                    "text": "4.9 mi",
                                    "value": 7833
                                },
                                "duration": {
                                    "text": "14 mins",
                                    "value": 856
                                },
                                "status": "OK"
                            }
                        ]
                    }
                ],
                "status": "OK"
            },
            "bicycling": {
                "destination_addresses": [
                    "Donegall Square N, Belfast BT1 5GS, UK",
                    "Unit 1 Boucher Business Centre, Apollo Rd, Belfast BT12 6HP, UK"
                ],
                "origin_addresses": [
                    "x Portallo St, Belfast BT6 9BE, UK"
                ],
                "rows": [
                    {
                        "elements": [
                            {
                                "distance": {
                                    "text": "1.7 mi",
                                    "value": 2664
                                },
                                "duration": {
                                    "text": "9 mins",
                                    "value": 550
                                },
                                "status": "OK"
                                },
                                {
                                "distance": {
                                    "text": "3.8 mi",
                                    "value": 6118
                                },
                                "duration": {
                                    "text": "23 mins",
                                    "value": 1376
                                },
                                "status": "OK"
                            }
                        ]
                    }
                ],
                "status": "OK"
            }
        }

        expected = {
            'to_boulder_world_bicycling_distance': '3.8 mi',
            'to_boulder_world_bicycling_duration': '23 mins',
            'to_boulder_world_driving_distance': '4.9 mi',
            'to_boulder_world_driving_duration': '14 mins',
            'to_city_hall_bicycling_distance': '1.7 mi',
            'to_city_hall_bicycling_duration': '9 mins',
            'to_city_hall_driving_distance': '1.7 mi',
            'to_city_hall_driving_duration': '8 mins'
        }

        result = DistanceMatrix.to_h(distance_matrix)

        self.assertEqual(result, expected)

    def test_get_as_dry_run(self):
        origin = 'Ozone, Ormeau Embankment, Belfast BT6 8LT'
        result = DistanceMatrix(origin).get()
        expected = {
            'bicycling': {'dry': 'run'},
            'driving': {'dry': 'run'}
        }

        self.assertEqual(result, expected)

    @patch('props.distance_matrix.Request', autospec=True)
    def test_get(self, request):
        attributes = {'json.return_value': {'foo': 'bar'}}
        request.return_value.get.return_value = Mock(**attributes)

        origin = 'Ozone, Ormeau Embankment, Belfast BT6 8LT'
        distance_matrix = DistanceMatrix(origin)

        result = distance_matrix.get(dry_run=False)
        expected = {
            'bicycling': {'foo': 'bar'},
            'driving': {'foo': 'bar'}
        }

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
