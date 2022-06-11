import statistics

"""
statistics.mean(data)
    Return the sample arithmetic mean of data which can be a sequence or iterable.

statistics.fmean(data)
    Convert data to floats and compute the arithmetic mean.
    [New in version 3.8.]
"""
means = statistics.fmean([100, 90])
print(means)