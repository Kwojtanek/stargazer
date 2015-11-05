__author__ = 'Jakub Wojtanek, Kwojtanek@gmail.com'
import json
with open('/pro/stargazer/DataScraper/otypes.json','r') as f:
    otypes = json.load(f)
    f.close()

with open('/pro/stargazer/DataScraper/SearchTypes.json','r') as f:
    stypes = json.load(f)
    f.close()

    #print stypes[1]['value'][0]
    #print stypes[1]['label']

    #print otypes[stypes[1]['value'][0]]

uniformdata = []
'''
for x in range(0,len(stypes)):
    udata = {}
    if not stypes[x]['label'] in udata:
        udata[stypes[x]['label']] = [stypes[1]['value'][0]]
    else:
        udata[stypes[x]['label']]
'''


for x in range(0,len(stypes)):
    if x == 0:
        single_row = { 'uniname': stypes[x]['label'],'data': [{'value' : [stypes[x]['value'][0]],'label': otypes[stypes[x]['value'][0]]}]}
        uniformdata.append(single_row)

    else:
        for y in range(0,len(uniformdata)):
            print 'Commparing %s & %s' % (uniformdata[y]['uniname'], stypes[x]['label'])
            if uniformdata[y]['uniname'] == stypes[x]['label']:
                for z in range(0,len(uniformdata[y]['data'])):
                    #print 'Commparing %s & %s' % (uniformdata[y]['data'][z]['value'], stypes[x]['value'][0])
                    if uniformdata[y]['data'][z]['value'] == stypes[x]['value'][0]:
                        print 'True'
                        break
                    else:
                        print 'False'
                        uniformdata[y]['data'].append({'value' : stypes[x]['value'][0],'label': otypes[stypes[x]['value'][0]]})
                        break
                break
            else:
                print 'y len %s and uniform len %s' % (y, len(uniformdata))
                if y + 1 == len(uniformdata):
                    single_row = { 'uniname': stypes[x]['label'], 'data': [{'value' : stypes[x]['value'][0],'label': otypes[stypes[x]['value'][0]]}]}
                    uniformdata.append(single_row)
                    break
                else:
                    pass



with open('/pro/stargazer/DataScraper/tests/śmieci/dropdowntypes.json','w+') as f:
    json.dump(uniformdata,f)
    f.close()

przyklad = [{'uniname': 'Galaxy',
      'data': [{'value': 'GinGroup', 'label': 'Group in Galaxis'},
                {'value':'bka','label':'bka'}
                ]}
    ,]
