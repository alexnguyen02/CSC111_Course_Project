"""
This file is for filtering the four datasets, WHO-COVID-19-global-data, COVID-19-data-from-2023-02-01.csv, routes.csv
and airports.csv
"""
import csv
from datetime import datetime


def csv_airports_dict(file: str) -> dict[str, list[str]]:
    """
    This Takes the airports.csv and returns a dict with key values of countries in the file
    and then the associated value is the airports within that country

    :param file:
    :return:
    """
    # Accumalator Dict
    dict_so_far = {}

    # Opens airport.csv
    with open(file) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader)
        for row in reader:
            # country name
            country = row[3]
            # associated airport code
            airports = row[4]

            # Checks if country is already in accumaltor to not get duplicates
            if country not in dict_so_far:
                dict_so_far[country] = [airports]
            # By this point, country should be in accumalator and should add assosiated
            # airport code to country in dict
            else:
                assert country in dict_so_far
                dict_so_far[country].append(airports)
    return dict_so_far


def test(file: str) -> None:
    """

    :param file:
    :return:
    """
    with open(file) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader)
        for row in reader:
            assert len(row[2]) == 3 and len(row[4]) == 3


def new_csv(file: str, country_dict: dict[str, list[tuple[str, str]]], output_file='data/new_routes_with_countries'):
    """

    :param aiports:
    :param output_file:
    :return:
    """
    with open(file, mode='r') as main_file:
        reader = csv.reader(main_file)
        next(reader)

        with open(output_file, mode='w') as filter_data:
            writer = csv.writer(filter_data, delimiter=',')
            for row in reader:
                source = row[2]
                dest = row[4]
                source_country = ''
                dest_country = ''
                for k, v_list in country_dict.items():
                    for airport in v_list:
                        if airport == source:
                            source_country = k
                        elif airport == dest:
                            dest_country = k

                if source_country == dest_country:
                    pass
                elif source_country == '' and dest_country != '':
                    pass
                elif dest_country == '' and source_country != '':
                    pass
                else:
                    row_to_write = [source_country, dest_country]
                    writer.writerow(row_to_write)


def country_list_UN() -> list[str]:

    """"""
    lst_so_far = []
    with open('data/filter_un_populations.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader)
        for row in reader:
            if row[0] not in lst_so_far:
                lst_so_far.append(row[0])
    return lst_so_far


def filter_covid(filename: str, output_file='data/COVID-19-data-from-2023-02-01.csv'):
    """Read the data in filename, and write the data - filtered by the starting date of
    2023-02-01 up to the latest date - onto the output_file.

    """
    with open(filename, mode='r') as main_file:
        reader = csv.reader(main_file)
        next(reader)

        with open(output_file, mode='w') as filter_data:
            writer = csv.writer(filter_data, delimiter=',', lineterminator="\n")

            non_un_list = ['American Samoa', 'Anguilla', 'Aruba', 'Bermuda', 'Bonaire', 'British Virgin Islands',
                           'Cayman Islands', 'Cook Islands', 'Curaçao', 'Falkland Islands (Malvinas)', 'Faroe Islands',
                           'French Guiana', 'French Polynesia', 'Gibraltar', 'Greenland', 'Guadeloupe', 'Guam',
                           'Guernsey',
                           'Holy See', 'Isle of Man', 'Jersey', 'Kosovo[1]', 'Martinique', 'Mayotte', 'Montserrat',
                           'New Caledonia', 'Niue', 'Northern Mariana Islands (Commonwealth of the)',
                           'occupied Palestinian territory, including east Jerusalem', 'Other', 'Pitcairn Islands',
                           'Puerto Rico', 'Réunion', 'Saba', 'Saint Barthélemy',
                           'Saint Helena, Ascension and Tristan da Cunha', 'Saint Martin',
                           'Saint Pierre and Miquelon',
                           'Sint Eustatius', 'Sint Maarten', 'Tokelau', 'Turks and Caicos Islands',
                           'United States Virgin Islands', 'Wallis and Futuna']

            special_codes = ['CW', 'BL', 'RE']

            for row in reader:
                first_date = datetime(2023, 2, 1).date()
                if datetime.strptime(row[0], '%Y-%m-%d').date() >= first_date and row[2] not in non_un_list and row[1] not in special_codes:
                    if row[1] == 'TR':
                        row[2] = 'Turkiye'
                    elif row[1] == 'CI':
                        row[2] = 'Cote d\'Ivoire'

                    writer.writerow(row)


if __name__ == '__main__':
    filter_covid('data/WHO-COVID-19-global-data.csv')


def filter_routes(filename: str, output_file='data/new_routes_2.0'):
    """Read the data in filename, and write the data - filtered by the starting date of
    2023-02-01 up to the latest date - onto the output_file.

    """
    with open(filename, mode='r') as main_file:
        reader = csv.reader(main_file)
        next(reader)

        with open(output_file, mode='w') as filter_data:
            writer = csv.writer(filter_data, delimiter=',', lineterminator="\n")

            non_un_list = ['American Samoa', 'Anguilla', 'Aruba', 'Bermuda', 'Bonaire', 'British Virgin Islands',
                           'Cayman Islands', 'Cook Islands', 'Curaçao', 'Falkland Islands (Malvinas)', 'Faroe Islands',
                           'French Guiana', 'French Polynesia', 'Gibraltar', 'Greenland', 'Guadeloupe', 'Guam',
                           'Guernsey', 'Holy See', 'Hong Kong', 'Isle of Man', 'Jersey', 'Macau', 'Kosovo[1]',
                           'Martinique',
                           'Mayotte', 'Montserrat', 'Netherlands Antilles', 'New Caledonia', 'Niue',
                           'Northern Mariana Islands (Commonwealth of the)', 'Northern Mariana Islands'
                           'occupied Palestinian territory, including east Jerusalem', 'Other', 'Pitcairn Islands',
                           'Puerto Rico', 'Réunion', 'Saba', 'Saint Barthélemy',
                           'Saint Helena, Ascension and Tristan da Cunha', 'Saint Martin',
                           'Saint Pierre and Miquelon',
                           'Sint Eustatius', 'Sint Maarten', 'Taiwan', 'Tokelau', 'Turks and Caicos Islands',
                           'United States Virgin Islands', 'Wallis and Futuna']

            curr_row = '', ''

            for row in reader:
                if row[0] not in non_un_list and row[1] not in non_un_list and curr_row != row:
                    if row[0] == 'United Kingdom':
                        row[0] = 'The United Kingdom'
                    if row[1] == 'United Kingdom':
                        row[1] = 'The United Kingdom'
                    if row[0] == 'Turkey':
                        row[0] = 'Turkiye'
                    if row[1] == 'Turkey':
                        row[1] = 'Turkiye'
                    if row[0] == 'United States':
                        row[0] = 'United States of America'
                    if row[1] == 'United States':
                        row[1] = 'United States of America'
                    if row[0] == 'Venezuela':
                        row[0] = 'Venezuela (Bolivarian Republic of)'
                    if row[1] == 'Venezuela':
                        row[1] = 'Venezuela (Bolivarian Republic of)'
                    if row[0] == 'Tanzania':
                        row[0] = 'United Republic of Tanzania'
                    if row[1] == 'Tanzania':
                        row[1] = 'United Republic of Tanzania'
                    if row[0] == 'Syria':
                        row[0] = 'Syrian Arab Republic'
                    if row[1] == 'Syria':
                        row[1] = 'Syrian Arab Republic'
                    if row[0] == 'South Korea':
                        row[0] = 'Republic of Korea'
                    if row[1] == 'South Korea':
                        row[1] = 'Republic of Korea'
                    if row[0] == 'North Korea':
                        row[0] = 'Democratic People\'s Republic of Korea'
                    if row[1] == 'North Korea':
                        row[1] = 'Democratic People\'s Republic of Korea'
                    if row[0] == 'Moldova':
                        row[0] = 'Republic of Moldova'
                    if row[1] == 'Moldova':
                        row[1] = 'Republic of Moldova'
                    if row[0] == 'Micronesia':
                        row[0] = 'Micronesia (Federated States of)'
                    if row[1] == 'Micronesia':
                        row[1] = 'Micronesia (Federated States of)'
                    if row[0] == 'Laos':
                        row[0] = 'Lao People\'s Democratic Republic'
                    if row[1] == 'Laos':
                        row[1] = 'Lao People\'s Democratic Republic'
                    if row[0] == 'Iran':
                        row[0] = 'Iran (Islamic Republic of)'
                    if row[1] == 'Iran':
                        row[1] = 'Iran (Islamic Republic of)'
                    if row[0] == 'Vietnam':
                        row[0] = 'Viet Nam'
                    if row[1] == 'Vietnam':
                        row[1] = 'Viet Nam'
                    if row[0] == 'Russia':
                        row[0] = 'Russian Federation'
                    if row[1] == 'Russia':
                        row[1] = 'Russian Federation'
                    if row[0] == 'Bolivia':
                        row[0] = 'Bolivia (Plurinational State of)'
                    if row[1] == 'Bolivia':
                        row[1] = 'Bolivia (Plurinational State of)'

                    writer.writerow(row)
                    curr_row = row


if __name__ == '__main__':
    filter_routes('data/new_routes_with_countries')