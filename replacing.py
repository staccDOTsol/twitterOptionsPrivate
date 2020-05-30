from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove

def replace(file_path):
    #Create temp file
    toappend = []
    with open('./test_replaced.csv','w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                csv = line.split(',')
                if 'D' not in csv[-1]:
                    datetime = csv[0].split(':')
                    datetime[-1] = '00'
                    newdatetime = ':'.join(datetime)
                    csv[0] = newdatetime
                    toappend.append(','.join(csv))
        toappend.reverse()
        for line in toappend:
            new_file.write(line)


replace('./test.csv')