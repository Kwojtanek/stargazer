__author__ = 'Jakub Wojtanek, Kwojtanek@gmail.com'
"""
READS otypes.json
Gets description about object from wikipedia
Gets list of images from wiki
Iterates throu list,
Gets one image from list, The biggest??
Scraps from wiki image info
gets uniformname from SearchTypes.json
maps data:
 Maintype > uniformname
 Nametype > otypes[value]
 Shortcutnametype > otype[key]
 Description > wikiscraper.data
Saves procceeded types
Loop otypeLen <= len proceeded types
"""
from DataScraper.Scrapers import WikiMediaScraper

SearchTypes = [
    {
        'value': 'Galaxy',
        'label': 'Galaxy'},
    {
        'value': 'Star',
        'label': 'Star'},
    {
        'value': 'Interstellar matter',
        'label': 'Interstellar matter'},
    {
        'value': 'Candidate objects',
        'label': 'Candidate objects'},
    {
        'value': 'Gravitational Source',
        'label': 'Gravitational Source'},

    {
        'value': 'gamma-ray source',
        'label': 'gamma-ray source'},
    {
        'value': 'X-ray source',
        'label': 'X-ray source'},
    {
        'value': 'UV-emission source',
        'label': 'UV-emission source'},

    {
        'value': 'Infra-Red source',
        'label': 'Infra-Red source'}
    ,
    {
        'value': 'Radio-source',
        'label': 'Radio-source'},
    {
        'value': 'Very red source',
        'label': 'Extremely Red Object'},

]
'''
def mainfunc():
    #Reads type
    data = {}
    data['Maintype'] = get_description(otype_reader(pktype_reader())[0])
    data['Nametype'] = otype_reader(pktype_reader())[1]
    data['Shortcutnametype'] = otype_reader(pktype_reader())[0]
    #Gets info from wikipedia
    Description = WikiMediaScraper(data['Nametype']).get_finall_data()
    if WikiMediaScraper(data['Nametype']).get_finall_data():
            data['Description'] = WikiMediaScraper(data['Nametype']).get_finall_data()
    TypeSender('',data).send_data()
    print 'proceeded object %s' % data
    print '....................................................................................................'
mainfunc()
'''
for x in SearchTypes:
    print x['value']
    print WikiMediaScraper(x['value']).get_finall_data()