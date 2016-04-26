__author__ = 'Jakub Wojtanek, Kwojtanek@gmail.com'
from astroquery.ned import Ned
import unittest
result_table = Ned.query_object("NGC 6720")
result_table2 = Ned.get_table("NGC 6720", table='diameters')

for k in result_table:
    print k
print result_table.keys()

print result_table2.keys()
print result_table['RA(deg)']
print result_table['DEC(deg)']
print result_table['Magnitude and Filter']
print result_table['Distance (arcmin)']
print result_table['Diameter Points']
print result_table2['Major Axis']
print result_table2['Minor Axis']

