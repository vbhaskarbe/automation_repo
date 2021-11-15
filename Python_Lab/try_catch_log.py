import sys
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except Exception:
    logger.error('Failed to read the file', exc_info=True)


