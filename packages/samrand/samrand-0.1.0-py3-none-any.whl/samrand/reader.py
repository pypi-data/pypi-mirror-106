import csv
import json


def read_csv(path, with_header):
    """Reads a CSV file's contents into an array of arrays to facilitate sampling.

    :param path: Path to the file containing the dataset in CSV format.
    :type path: str
    :param with_header: Flag specifying if the CSV dataset's first row is a header.
    :type with_header: bool
    :return: A tuple where the first entry is the processed dataset, and the second is the header (if there is one).
    :type return: tuple
    """
    read_result = []
    with open(path, 'r') as csv_in:
        csv_reader = csv.reader(csv_in)
        for row in csv_reader:
            read_result.append(row)
    if with_header:
        return (read_result[1:], read_result[0])
    else:
        return (read_result, None)


def read_json(path):
    """Reads a JSON file's contents into an array of arrays to facilitate sampling.

    :param path: Path to the file containing the dataset in JSON format.
    :type path: str
    :return: A tuple where the first entry is the processed dataset, and the second is the header.
    :type return: tuple
    """
    read_result = []
    header = []
    dataset = []
    with open(path, 'r') as json_in:
        read_result = json.load(json_in)
    if type(read_result) is not list:
        raise TypeError('Expected a JSON list.')
    if len(read_result) == 0:
        raise ValueError('Expected a list with at least one entry.')
    # Build header from keys (assume all entries have the same keys)
    for key in read_result[0].keys():
        header.append(key)
    # Build dataset from entries and align with header
    for entry in read_result:
        row = []
        for key in header:
            row.append(entry[key])
        dataset.append(row)
    return (dataset, header)

