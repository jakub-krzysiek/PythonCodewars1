def past(h, m, s):
    if (0 > h or h > 23) or (0 > m or m > 59) or (0 > s or s > 59):
        return (h * 3600 + m * 60 + s) * 1000
