""""""""""""
SamRand
""""""""""""

============
Introduction
============

SamRand is a tool designed to sample datasets and produce statistically representative samples for research purposes.

----------------
Who is this for?
----------------
I developed this primarily for researchers who deal with large datasets, and need to sample them to conduct some qualitative analysis.
While it was meant to pull samples for qualitative purposes, it could be used for quantitative purposes as well.
And even though, at the time, it was meant for researchers, there is no reason to believe that it can be used for non-research use-cases.
As such, this project is licensed under the MIT license.

----------------------------------------------------
How does SamRand sample a dataset?
----------------------------------------------------
SamRand's sampling approach differs depending on the settings you use when sampling a dataset.
These are, however, dependent on the choice of stratification:

- **No Stratification:** SamRand will select rows from the dataset at random without attempting to represent any existing groups within the dataset's population.
- **Stratification with Unknown Dimensions:** SamRand will perform a single-level clustering along the dimension with the least variance (to guarantee diverse strata). Samples are pulled from these two strata based on their proportion to the dataset's distribution. For instance, a dataset with location as the dimension with the least variance (either X or Y with a 60:40 split) will generate a sample of 6 rows in location X and 4 in location Y if the sample size is 10.
- **Stratification with known Dimensions:** If you provide specific dimensions (column indices) when invoking SamRand, it will apply multi-level clustering to generate strata. This means it will split the data by the first dimension, then split the strata resulting from the first split by the second dimension, and so on.

**Important Note:**
Depending on how your dataset is distributed, it is possible that there will be strata with only a single row.
SamRand will extract at least one row from each strata.
This will inflate sample size, resulting in a sample size larger than what you specified.
To reconcile the difference, SamRand will (once it has a representative sample) remove rows at random from that sample until it shrinks down to the desired size.
Consequently, rows from larger strata have a higher probability to be removed towards the end of the sampling process.

There is also whether you choose to sample with or without replacement:

- **with Replacement:** Rows previously sampled may be sampled again. Which means that the dataset may consist of duplicate rows.
- **without Replacement:** Rows previously sampled may not be sampled again. which means that the dataset will not contain duplicates unless the dataset itself contains duplicates.

If there is a sampling strategy you'd like to see implemented or fixed, feel free to open an issue.
I will try to get around to it.
Alternatively, you can submit a merge request.
Stay up-to-date by monitoring SamRand's `issues page <https://gitlab.com/omazhary/SamRand/-/issues>`_.

==========================
How Do I Use SamRand?
==========================

SamRand supports two modes of use:
- as a standalone application, and
- as a module within your python script.

---------------------------------
What Should My Dataset Look Like?
---------------------------------
Right now, SamRand supports two types of datasets, CSV files and JSON files.
For now, CSV files are expected to use commas as delimiters, with double quotes around text (default python CSV settings).
JSON files are expected to be valid.
Examples of both dataset types are included in the `test folder of this repository <https://gitlab.com/omazhary/SamRand/-/tree/master/test>`_.

---------------------------
As a standalone application
---------------------------
Once installed, you can use SamRand as a standalone application in your terminal of choice.
It supports the following arguments:

- **-h**, **--help:** Shows a help message and exits.
- **--dataset <path/to/dataset/file>:** The file containing your dataset.
- **--size <integer>:** The required sample size (n).
- **--header:** When using a CSV dataset file, use this flag to indicate whether the first row is a header.
- **--replacement:** Extract samples with replacement. Not including this flag means without replacement (the default behavior).
- **--stratify:** Balance the extracted sample so that it reflects the population's distribution.
- **--strata '[0, 1, 2, ...]':** When using stratification, use this parameter to indicate which fields should be used as a basis for stratification. Accepts valid JSON arrays of column indices starting with 0.
- **--output:** The output format of the samples. Default is JSON. Can be one of [CSV|JSON].

A typical command using SamRand looks like the following example that samples a CSV dataset with a header for 30 samples, then outputs the sample to _stdout_ in CSV format:

.. code:: shell

    $ SamRand --dataset datasets/dataset.csv \
    --size 30 \
    --header \
    --stratify \
    --strata '[4, 5]' \
    --output CSV

To output the results somewhere other than _stdout_, redirect the output to a file depending on your terminal emulator.
For instance, when redirecting the above command's output to a CSV file in a standard bash session:

.. code:: shell

    $ SamRand --dataset datasets/dataset.csv \
    --size 30 \
    --header \
    --stratify \
    --strata '[4, 5]' \
    --output CSV > output.csv

------------------
As a Python module
------------------
You can build a python script and use SamRand within it to sample datasets on the fly to do with as you please.
For instance, if you wanted to sample a dataset in your python script, you would import SamRand as a dependency, and give it the necessary information:

.. code:: python

    import samrand as sr

    dataset_path = '/path/to/my/dataset.json'
    dataset = sr.reader.read_json(dataset_path)
    sample = sr.sampler.sample(dataset, 30, stratify=True, replacement=True)

Further documentation can be found `here <https://samrand.readthedocs.io/>`_.

==============================
How Do I Install SamRand?
==============================

Regardless of whether you want to use it as a standalone application or a module in your project, you can install SamRand via pip as you would any normal python module:

.. code:: shell

    $ pip install samrand