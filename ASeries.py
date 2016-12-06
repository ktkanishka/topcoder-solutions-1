class ASeries(object):
    def longest(self, vals):
        values = sorted(vals)
        s = set([()])
        for val in values:
            tmp = set()
            for series in s:
                tmp.add(series)
                if len(series) in (0, 1):
                    new_series = series + (val,)
                    tmp.add(new_series)
                else:
                    if val - series[len(series) - 1] == series[len(series) - 1] - series[len(series) -2]:
                       new_series = series + (val,)
                       tmp.add(new_series)
            s = tmp
        return len(max(s, key=lambda x: len(x)))
