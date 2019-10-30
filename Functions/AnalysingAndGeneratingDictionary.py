def grades(*notes, st = False):
    '''
    Analyses the grade of a student
    :param notes: one or more students grade (accept multiple)
    :param st: Show or not the students status (optional)
    :return: a dict with data of the students situation
    '''
    count = len(notes)
    avg = sum(notes)/count
    result = {
        'total': count,
        'highest': max(notes),
        'lowest': min(notes),
        'avg': avg
    }

    if (st):
        status = 'terrible'
        if (5 <= avg < 7):
            status = 'ok'
        elif(7 <= avg <= 8):
            status = 'good'
        elif(avg > 8):
            status = 'fantastic'
        result['status'] = status

    return result


print(grades(1,2,3,4,5,6,7,8,9,10,5.5,6.1, st=True))
