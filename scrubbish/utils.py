import time
from properties import Properties
from property import Property
from json_helper import JsonHelper
from csv_helper import CsvHelper
from distance_matrix import DistanceMatrix
from postal import Postal

def get_area_uris(areas):
    area_uris = {}
    for area in areas:
        uris = []
        properties = Properties(areas[area])
        print(properties.pagination())

        index = 0
        while properties.more():
            uri = properties.next_uri()
            id = uri.split('/')[-1]

            if id[0] == 'd':
                print('skipping:', uri)
                continue

            uris.append({index: uri})
            index += 1

        area_uris[area] = uris

    return area_uris

def print_uris(area_uris):
    total_uris = 0
    for area in area_uris:
        num = len(area_uris[area])
        total_uris += num
        print(f'{area} uris:', num)

    print('total uris:', total_uris)

def write_csv(area_uris):
    for area in area_uris:
       uris = area_uris[area]
       csv_file = CsvHelper(f'{area}_properties')

       try:
           index = 0
           for uri in uris:
               property = Property(uri[index])
               csv_file.write(property.to_h())

               print(f'({index}/{len(uris)})')
               index += 1
       finally:
           csv_file.file.close()

def continue_csv(area_uris, start_area, start_index, csv_file):
    csv_file = CsvHelper(csv_file)
    try:
        seek = True

        for area, uris in area_uris.items():
            if area != start_area and seek:
                continue
            elif area == start_area:
                seek == False

            index = int(start_index)
            while index < len(uris)-1:
                id = str(index)
                uri = uris[index][id]
                csv_file.append(Property(uri).to_h())

                print(f'({index}/{len(uris)})')
                index += 1
    finally:
        csv_file.file.close()

def get_distances(csv_file):
    csv_file = CsvHelper(csv_file)
    try:
        url_index = 0
        price_index = 1
        address_index = 10

        distance_matrix = {}
        for index, row in enumerate(csv_file.read()):
            if index == 0:
                continue

            url = row[url_index]
            price = int(row[price_index].replace('£', '').replace('$', '').replace('€', '').replace(',', ''))
            address = row[address_index]

            if price > 200000:
                continue

            print('distance matrix:', url)
            distance_matrix[index] = DistanceMatrix(address).get()
    finally:
        csv_file.file.close()

    return distance_matrix

def write_distances(csv_file, json_file):
    original_csv_file = CsvHelper(csv_file)
    new_csv_file = CsvHelper(f'new_props_{time.time()}')
    distance_matrix = JsonHelper(json_file).read()

    try:
        for index, row in enumerate(original_csv_file.read()):
            key = str(index+1)

            if key in distance_matrix:
                result = DistanceMatrix.to_h(distance_matrix[key])

                price = int(row['Price'].replace('£', '').replace('$', '').replace('€', '').replace(',', ''))
                row['Price'] = price
                address_index = 10

                row_keys = list(row.keys())
                row_values = list(row.values())

                postal_info = Postal(row['Address']).info()
                postal_length = len(postal_info)

                postal_keys = list(postal_info.keys())
                for index, key in enumerate(postal_keys):
                    offset_index = address_index + index + 1
                    row_keys.insert(offset_index, key)


                postal_values = list(postal_info.values())
                for index, value in enumerate(postal_values):
                    offset_index = address_index + index + 1
                    row_values.insert(offset_index, value)

                keys = list(result.keys())
                for index, key in enumerate(keys):
                    offset_index = address_index + postal_length + index + 1
                    row_keys.insert(offset_index, key)

                values = list(result.values())
                for index, value in enumerate(values):
                    offset_index = address_index + postal_length + index + 1
                    row_values.insert(offset_index, value)

                new_row = dict(zip(row_keys, row_values))
                new_csv_file.write(new_row)
    finally:
        original_csv_file.file.close()
        new_csv_file.file.close()
