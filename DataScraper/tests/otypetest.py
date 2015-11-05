import pickle
import json

__author__ = 'Jakub Wojtanek, Kwojtanek@gmail.com'
def get_otype(otype):
    """
    reads type of object and if does not ocures in list waits for input

    """
    with open('/pro/stargazer/DataScraper/otypes.json','rb') as f:
        ot = (json.load(f))
        f.close()
    if ot.has_key(otype):
        return ot.get(otype)
    else:
        inputvalue = raw_input('No otype %s '  + otype)
        ot[otype] = inputvalue
        if inputvalue == 'break':
            return False
        else:
            with open('/pro/stargazer/DataScraper/otypes.json','w') as f:
                json.dump(ot,f)
get_otype('Radio')