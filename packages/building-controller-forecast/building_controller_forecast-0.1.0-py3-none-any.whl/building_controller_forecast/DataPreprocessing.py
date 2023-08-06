try:
    import unzip_requirements
except ImportError:
    pass
import numpy as np


def remove_outliers(data,columns,num):
    outliers = []
    from collections import Counter
    for feature in data[columns].keys():
        # TODO: Calculate Q1 (25th percentile of the data) for the given feature
        Q1 = np.percentile(data[feature], 25)

        # TODO: Calculate Q3 (75th percentile of the data) for the given feature
        Q3 = np.percentile(data[feature], 75)

        # TODO: Use the interquartile range to calculate an outlier step (1.5 times the interquartile range)
        step = 1.5 * (Q3 - Q1)

        # Display the outliers
        all_outliers = data[~((data[feature] >= Q1 - step) & (data[feature] <= Q3 + step))]
        # OPTIONAL: Select the indices for data points you wish to remove
        outliers = outliers + all_outliers.index.tolist()

    # Remove the outliers, if any were specified
    o = Counter(outliers)
    good_data = data.drop(data.index[[int(i[0]) for i in o.most_common(num)]]).reset_index(drop=True)
    return good_data