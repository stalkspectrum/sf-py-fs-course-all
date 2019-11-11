def make_russian(numb):
    snum = str(numb)
    if snum[-1] == '1':
        if numb > 10 and snum[-2] == '1':
            students = ' студентов'
        else:
            students = ' студент'
    elif snum[-1] in ['2', '3', '4']:
        if numb > 10 and snum[-2] == '1':
            students = ' студентов'
        else:
            students = ' студента'
    else:
        students = ' студентов'
    return snum + students
