def get_grade(s1, s2, s3):
    grade = ''

    if 90 <= ((s1 + s2 + s3) / 3) <= 100:
        grade = 'A'
    elif 80 <= ((s1 + s2 + s3) / 3) < 90:
        grade = 'B'
    elif 70 <= ((s1 + s2 + s3) / 3) < 80:
        grade = 'C'
    elif 60 <= ((s1 + s2 + s3) / 3) < 70:
        grade = 'D'
    elif 0 <= ((s1 + s2 + s3) / 3) < 60:
        grade = 'F'

    return grade