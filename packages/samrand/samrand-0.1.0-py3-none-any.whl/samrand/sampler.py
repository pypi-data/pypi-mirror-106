import numpy as np
import random
from copy import deepcopy


def get_bins(record_set, dimension):
    """Creates bins of records based on the chosen dimension.

    :param record_set: The dataset from which the records are to be split (should be a list of lists with the inner-level representing rows).
    :type record_set: list
    :param dimension: The index of the column along which to make the split (starts at 0).
    :type dimension: int
    :return: A list of lists with the inner lists representing bins of datasets.
    :type return: list
    """
    bin_dict = dict()
    result = []
    for index, entry in enumerate(record_set):
        if entry[dimension] not in bin_dict.keys():
            bin_dict[entry[dimension]] = []
        bin_dict[entry[dimension]].append(entry)
    for key in bin_dict.keys():
        result.append(bin_dict[key])
    return result


def get_least_diverse_dimension(record_set):
    """Returns the dimension with the least variability as calculated by statistical variance.

    :param recrod_set: The dataset from which the dimension with the least variability is to be identified (should be a list of lists with the inner-level representing rows).
    :type record_set: list
    :return: An integer representing the dimension's index (starting from 0).
    :type return: int
    """
    dimensions = []
    min_variance = 1000
    min_dimension = -1
    for dimension in record_set[0]:
        dimensions.append([dimension])
    for entry in record_set[1:]:
        for dim_index, dim_value in enumerate(entry):
            dimensions[dim_index].append(dim_value)
    for index, dimension in enumerate(dimensions):
        processed_dim = []
        # Check to see if we're dealing with numbers, text, or textual numbers
        if type(dimension[0]) is str:
            try:
                float(dimension[0])  # It's a number
                processed_dim = [float(x) for x in dimension]
            except ValueError:  # It's not a number, we need to encode it
                uniques = list(np.unique(dimension))
                uniques_map = dict()  # Build our own little ordinal encoder
                counter = 1
                for unique in uniques:
                    uniques_map[unique] = counter
                    counter += 1
                processed_dim = [uniques_map[x] for x in dimension]
        else:  # It's already numbers
            processed_dim = dimension
        dim_variance = np.var(processed_dim)
        if dim_variance < min_variance:
            min_variance = dim_variance
            min_dimension = index
    return min_dimension


def get_random_subset(entry_set, n, replacement):
    """Extracts a random sample from a set with or without replacement.

    :param entry_set: The set from which the sample is to be extracted. Expects a list of lists where the inner lists represent rows.
    :type entry_set: list
    :param replacement: A flag to indicate whether to extract the sample with replacement or not.
    :type replacement: bool
    :return: A list of lists containing the extracted sample.
    :type return: list
    """
    random.seed()
    entry_set_copy = deepcopy(entry_set)
    result = []
    if n > len(entry_set):
        n = len(entry_set)
    while len(result) < n:
        index = random.randint(0, len(entry_set_copy) - 1)
        result.append(deepcopy(entry_set_copy[index]))
        if not replacement:
            del entry_set_copy[index]
    return result


def sample(dataset, size, stratify=False, strata=[], replacement=False):
    """Extracts a random sample of a given size from the dataset.

    :param dataset: The dataset from which the sample is to be extracted. Expects a tuple of ([[entry 1], [entry 2], ...], []) if the dataset has a header or ([[entry 1], [entry 2], ...], None) if there is no header.
    :type dataset: tuple
    :param size: The size of the expected sample.
    :type size: int
    :param stratify: A flag to indicate whether to stratify the sample.
    :type stratify: bool
    :param strata: A list of column indices (starting from 0) to indicate which columns to use to stratification.
    :type strata: list
    :param replacement: A flag to indicate whether to sample with or without replacement. Default is without.
    :type replacement: bool
    :return: A list of lists with each list representing a row in the sample.
    :type return: list
    """
    header = dataset[1]
    entries = dataset[0]
    sample_result = []
    final_result = []

    # Add a header if there is one
    if header:
        final_result.append(header)

    if stratify and len(strata) == 0:
        # If we need stratification but without dimensions, we use single-stage cluster sampling, and create strata from the dimension with the least variance to ensure diverse strata
        dim_index = get_least_diverse_dimension(entries)
        sample_bins = get_bins(entries, dim_index)
        for sample_bin in sample_bins:
            proportion_size = 1 + round((len(sample_bin) / len(entries)) * size)
            representative_bin = get_random_subset(sample_bin, proportion_size, replacement)
            sample_result.extend(representative_bin)
    elif stratify and len(strata) == 1:
        # Similar to the previous branch, but we have a specific dimension in mind
        dim_index = strata[0]
        sample_bins = get_bins(entries, dim_index)
        for sample_bin in sample_bins:
            proportion_size = 1 + round((len(sample_bin) / len(entries)) * size)
            representative_bin = get_random_subset(sample_bin, proportion_size, replacement)
            sample_result.extend(representative_bin)
    elif stratify and len(strata) > 1:
        # We have several specific dimensions, so we use multi-stage cluster sampling and create strata based on the given dimensions
        bin_levels = dict()
        current_level = 0
        bin_levels[current_level] = get_bins(entries, strata[0])
        while current_level < len(strata):
            for grouped_bin in bin_levels[current_level]:
                lower_bins = get_bins(grouped_bin, strata[current_level])
                for lower_bin in lower_bins:
                    if (current_level + 1) not in bin_levels.keys():
                        bin_levels[current_level + 1] = []
                    bin_levels[current_level + 1].append(lower_bin)
            current_level += 1
        for sample_bin in bin_levels[len(strata)]:
            proportion_size = 1 + round((len(sample_bin) / len(entries)) * size)
            representative_bin = get_random_subset(sample_bin, proportion_size, replacement)
            sample_result.extend(representative_bin)
    else:
        # If we don't need stratification, we just sample randomly for a uniformly distributed sample
        sample_result.extend(get_random_subset(entries, size, replacement))
    # Drop extra rows at random if the result size is larger than the sample size
    result_sample_size = len(sample_result)
    if result_sample_size > size:
        difference = result_sample_size - size
        random.seed()
        for i in range(difference):
            random_index = random.randint(0, len(sample_result) - 1)
            del sample_result[random_index]
    final_result.extend(sample_result)
    return final_result
