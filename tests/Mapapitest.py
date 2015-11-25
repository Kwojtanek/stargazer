__author__ = 'Jakub Wojtanek, Kwojtanek@gmail.com'
MAGNITUDO = [9, 11, 12.6]
mag = 11
for x in MAGNITUDO:
    if x < mag:
        print x
        MAGNITUDO.pop(MAGNITUDO.index(x))
print MAGNITUDO