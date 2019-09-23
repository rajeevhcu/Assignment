def median(sample):
    sample.sort()
    sample_size = len(sample)
    if sample_size % 2 == 0:
        return (sample[sample_size // 2 - 1] + sample[sample_size // 2]) / 2
    else:
        return sample[sample_size // 2]
