def formatName(name):
    '''只要英文和数字'''
    # highpoints = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    # name = highpoints.sub(u'', name)

    name = filter(str.isalnum, name)
    return name

print formatName('123465789fdsagdfrtytr')
print formatName('123465789f%#@(*d+_)/*-./sagdfrtytr')
print formatName('1234 65789fdsag dfrtytr')