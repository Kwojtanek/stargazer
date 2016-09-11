__doc__ = 'This file sends to the endpoint formated types of objects, source="types.txt",' \
          ' urlhttp://simbad.u-strasbg.fr/simbad/sim-display?data=otypes'
__author__ = 'Jakub Wojtanek, Kwojtanek@gmail.com'
import re, json
from DataScraper.Senders import TypeSender
with open('types.txt', 'r') as f:
    types = f.read()
    f.close()
lineslist = []
oldlineslist = types.splitlines()
for i, line in enumerate(oldlineslist):
    if line:
        lineslist.append(line)
list_types = []
# for i,line in enumerate(lineslist):
#     data={}
#     l = re.split('[\s]{2,}', line)
#     if l[0] != '':
#         it = i + 18
#         data['nametype'] = l[0]
#         data['shortcutnametype'] = l[1]
#         data['descriptiontype'] = l[2]
#         main = data
#
#     elif not len(l) == 1:
#         try:
#             l.remove('\xc2\xb7')
#             l.remove('\xc2\xb7')
#             l.remove('\xc2\xb7')
#
#         except:
#             pass
#         data['maintype'] = it
#         data['nametype'] = l[1]
#         data['shortcutnametype'] = l[2]
#         data['descriptiontype'] = l[3]
#     print i,json.dumps(data)
data=[]
for line in (lineslist):
    l = re.split('[\s]{2,}', line)
    if l[0] != '':
        data.append({"uniname":l[2],'data':[]})
        data[-1]['data'].append({"value":l[0],'label':l[2]})
    elif not len(l) == 1:
        try:
            l.remove('\xc2\xb7')
            l.remove('\xc2\xb7')
            l.remove('\xc2\xb7')

        except:
            pass
        data[-1]['data'].append({'value':l[1],'label':l[3]})
for o in data:
    print json.dumps(o)