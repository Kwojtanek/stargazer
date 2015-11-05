__author__ = 'Jakub Wojtanek, Kwojtanek@gmail.com'
import json

def get_description(otype):

    """
    return matching description of type, if none is matching waits for new
    """
    with open('/pro/stargazer/DataScraper/tests/SearchTypes.json','r') as f:
        st = (json.load(f))
        f.close()

    for x in range(0,len(st)):
        for y in range(0,len(st[x]['value'])):
            if st[x]['value'][y] == otype:
                return st[x]['label']

    inputvalue = raw_input('No label in file... for %s ' % otype )

    for z in range(0,len(st)):
        for v in range(0,len(st[z]['value'])):
            if st[z]['value'][v] == inputvalue:
                st[z]['value'].append(otype)
                with open('/pro/stargazer/DataScraper/tests/SearchTypes.json','w') as f:
                    json.dump(st,f)
                return st[z]['label']
            else:
                inputlabel = raw_input('Pliz provide label for ... %s ' % otype)
                newrow = {'value': [otype], 'label': inputlabel}
                st.append(newrow)
                with open('/pro/stargazer/DataScraper/tests/SearchTypes.json','w') as f:
                    json.dump(st,f)
                return st[z]['label']

