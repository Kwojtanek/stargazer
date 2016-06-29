var min_mag = 0;
var max_mag = 20.6;
var maxid = 13401;
var hashtag = '';
var familycount = 9

ConstList = [
    {
        "label": "Pegasus\n/ˈpɛɡəsəs/",
        "value": "peg"
    },
    {
        "label": "Pisces\n/ˈpaɪsiːz/, /ˈpɪsiːz/",
        "value": "psc"
    },
    {
        "label": "Andromeda\n/ænˈdrɒmɨdə/",
        "value": "and"
    },
    {
        "label": "Sculptor\n/ˈskʌlptər/",
        "value": "scl"
    },
    {
        "label": "Cetus\n/ˈsiːtəs/",
        "value": "cet"
    },
    {
        "label": "Phoenix\n/ˈfiːnɨks/",
        "value": "phe"
    },
    {
        "label": "Cepheus\n/ˈsiːfiəs/, /ˈsiːfjuːs/",
        "value": "cep"
    },
    {
        "label": "Tucana\n/tjʊˈkeɪnə/",
        "value": "tuc"
    },
    {
        "label": "Cassiopeia\n/ˌkæsi.ɵˈpiːə/",
        "value": "cas"
    },
    {
        "label": "Triangulum\n/traɪˈæŋɡjʊləm/",
        "value": "tri"
    },
    {
        "label": "Hydrus\n/ˈhaɪdrəs/",
        "value": "hyi"
    },
    {
        "label": "Perseus\n/ˈpɜrsiəs,",
        "value": "per"
    },
    {
        "label": "Aries\n/ˈɛəriːz/, /ˈɛərɪ.iːz/",
        "value": "ari"
    },
    {
        "label": "Eridanus\n/ɨˈrɪdənəs/",
        "value": "eri"
    },
    {
        "label": "Fornax\n/ˈfɔrnæks/",
        "value": "for"
    },
    {
        "label": "Horologium\n/ˌhɒrəˈlɒdʒiəm/",
        "value": "hor"
    },
    {
        "label": "Taurus\n/ˈtɔrəs/",
        "value": "tau"
    },
    {
        "label": "Reticulum\n/rɨˈtɪkjʊləm/",
        "value": "ret"
    },
    {
        "label": "Camelopardalis\n/kəˌmɛlɵˈpɑrdəlɨs/",
        "value": "cam"
    },
    {
        "label": "Dorado\n/dəˈrɑːdəʊ/",
        "value": "dor"
    },
    {
        "label": "Mensa\n/ˈmɛnsə/",
        "value": "men"
    },
    {
        "label": "Caelum\n/ˈsiːləm/",
        "value": "cae"
    },
    {
        "label": "Orion\n/ɵˈraɪ.ən/",
        "value": "ori"
    },
    {
        "label": "Auriga\n/ɔːˈraɪɡə/",
        "value": "aur"
    },
    {
        "label": "Pictor\n/ˈpɪktər/",
        "value": "pic"
    },
    {
        "label": "Lepus\n/ˈliːpəs/",
        "value": "lep"
    },
    {
        "label": "Columba\n/kɵˈlʌmbə/",
        "value": "col"
    },
    {
        "label": "Gemini\n/ˈdʒɛmɨnaɪ/",
        "value": "gem"
    },
    {
        "label": "Monoceros\n/məˈnɒsɨrəs/",
        "value": "mon"
    },
    {
        "label": "Carina\n/kəˈraɪnə/",
        "value": "car"
    },
    {
        "label": "Puppis\n/ˈpʌpɨs/",
        "value": "pup"
    },
    {
        "label": "Canis Major\n/ˈkeɪnɨs ˈmeɪdʒər/",
        "value": "cma"
    },
    {
        "label": "Lynx\n/ˈlɪŋks/",
        "value": "lyn"
    },
    {
        "label": "Volans\n/ˈvoʊlænz/",
        "value": "vol"
    },
    {
        "label": "Canis Minor\n/ˈkeɪnɨs ˈmaɪnər/",
        "value": "cmi"
    },
    {
        "label": "Cancer\n/ˈkænsər/",
        "value": "cnc"
    },
    {
        "label": "Vela\n/ˈviːlə/",
        "value": "vel"
    },
    {
        "label": "Hydra\n/ˈhaɪdrə/",
        "value": "hya"
    },
    {
        "label": "Octans\n/ˈɒktænz/",
        "value": "oct"
    },
    {
        "label": "Ursa Major\n/ˌɜrsə ˈmeɪdʒər/",
        "value": "uma"
    },
    {
        "label": "Pyxis\n/ˈpɪksɨs/",
        "value": "pyx"
    },
    {
        "label": "Leo Minor\n/ˈliː.oʊ ˈmaɪnər/",
        "value": "lmi"
    },
    {
        "label": "Leo\n/ˈliː.oʊ/",
        "value": "leo"
    },
    {
        "label": "Antlia\n/ˈæntliə/",
        "value": "ant"
    },
    {
        "label": "Draco\n/ˈdreɪkoʊ/",
        "value": "dra"
    },
    {
        "label": "Chamaeleon\n/kəˈmiːliən/",
        "value": "cha"
    },
    {
        "label": "Sextans\n/ˈsɛkstənz/",
        "value": "sex"
    },
    {
        "label": "Ursa Minor\n/ˌɜrsə ˈmaɪnər/",
        "value": "umi"
    },
    {
        "label": "Crater\n/ˈkreɪtər/",
        "value": "crt"
    },
    {
        "label": "Centaurus\n/sɛnˈtɔrəs/",
        "value": "cen"
    },
    {
        "label": "Virgo\n/ˈvɜrɡoʊ/",
        "value": "vir"
    },
    {
        "label": "Coma Berenices\n/ˈkoʊmə bɛrəˈnaɪsiːz/",
        "value": "com"
    },
    {
        "label": "Corvus\n/ˈkɔrvəs/",
        "value": "crv"
    },
    {
        "label": "Crux\n/ˈkrʌks/",
        "value": "cru"
    },
    {
        "label": "Musca\n/ˈmʌskə/",
        "value": "mus"
    },
    {
        "label": "Canes Venatici\n/ˈkeɪniːz vɨˈnætɨsaɪ/",
        "value": "cvn"
    },
    {
        "label": "Boötes\n/boʊˈoʊtiːz/",
        "value": "boo"
    },
    {
        "label": "Circinus\n/ˈsɜrsɨnəs/",
        "value": "cir"
    },
    {
        "label": "Lupus\n/ˈljuːpəs/",
        "value": "lup"
    },
    {
        "label": "Libra\n/ˈlaɪbrə/, /ˈliːbrə/",
        "value": "lib"
    },
    {
        "label": "Apus\n/ˈeɪpəs/",
        "value": "aps"
    },
    {
        "label": "Triangulum Australe\n/traɪˈæŋɡjʊləm ɔːˈstræliː/",
        "value": "tra"
    },
    {
        "label": "Serpens\n/ˈsɜrpɛnz/",
        "value": "ser"
    },
    {
        "label": "Corona Borealis\n/kɵˈroʊnə ˌbɔəriˈælɨs/",
        "value": "crb"
    },
    {
        "label": "Norma\n/ˈnɔrmə/",
        "value": "nor"
    },
    {
        "label": "Scorpius\n/ˈskɔrpiəs/",
        "value": "sco"
    },
    {
        "label": "Hercules\n/ˈhɜrkjʊliːz/",
        "value": "her"
    },
    {
        "label": "Ophiuchus\n/ˌɒfiˈjuːkəs/",
        "value": "oph"
    },
    {
        "label": "Ara\n/ˈɛərə/",
        "value": "ara"
    },
    {
        "label": "Pavo\n/ˈpeɪvoʊ/",
        "value": "pav"
    },
    {
        "label": "Sagittarius\n/sædʒɨˈtɛəriəs/",
        "value": "sgr"
    },
    {
        "label": "Corona Australis\n/kɵˈroʊnə ʔɔːˈstrælɨs/",
        "value": "cra"
    },
    {
        "label": "Telescopium\n/ˌtɛlɨˈskɒpiəm/",
        "value": "tel"
    },
    {
        "label": "Lyra\n/ˈlaɪrə/",
        "value": "lyr"
    },
    {
        "label": "Scutum\n/ˈskjuːtəm/",
        "value": "sct"
    },
    {
        "label": "Aquila\n/ˈækwɨlə/",
        "value": "aql"
    },
    {
        "label": "Vulpecula\n/vʌlˈpɛkjʊlə/",
        "value": "vul"
    },
    {
        "label": "Cygnus\n/ˈsɪɡnəs/",
        "value": "cyg"
    },
    {
        "label": "Sagitta\n/səˈdʒɪtə/",
        "value": "sge"
    },
    {
        "label": "Delphinus\n/dɛlˈfaɪnəs/",
        "value": "del"
    },
    {
        "label": "Capricornus\n/ˌkæprɨˈkɔrnəs/",
        "value": "cap"
    },
    {
        "label": "Indus\n/ˈɪndəs/",
        "value": "ind"
    },
    {
        "label": "Microscopium\n/ˌmaɪkrɵˈskoʊpiəm/",
        "value": "mic"
    },
    {
        "label": "Aquarius\n/əˈkwɛəriəs/",
        "value": "aqr"
    },
    {
        "label": "Equuleus\n/ɨˈkwuːliəs/",
        "value": "equ"
    },
    {
        "label": "Grus\n/ˈɡrʌs/",
        "value": "gru"
    },
    {
        "label": "Piscis Austrinus\n/ˈpaɪsɨs ɔːˈstraɪnəs/",
        "value": "psa"
    },
    {
        "label": "Lacerta\n/ləˈsɜrtə/",
        "value": "lac"
    }
]

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

]

SearchCatalogues = [
    'NGC',
    'PGC',
    'Messier',
    'IC'

]
Nodata = [
    {
        'value': 'Radio-source',
        'label': 'Radio-source'},
    {
        'value': 'Unknown',
        'label': 'Object of unknown nature'},
            {
        'value': '',
        'label': 'No data'},
        {
        'value': 'Inexistent',
        'label': 'Not an object (error, artefact, ...)'},
        {
        'value': 'Very red source',
        'label': 'Extremely Red Object'},

]
ddtypes = [
    {"uniname": "Galaxy", "data": [
        {"value": "GinPair", "label": "Galaxy in Pair of Galaxies"},
        {"value": "Galaxy", "label": "Galaxy"},
        {"value": "EmG", "label": "Emission-line galaxy  "},
        {"value": "GinGroup", "label": "Galaxy in Group of Galaxies"},
        {"value": "IG", "label": "Interacting Galaxies"},
        {"value": "Seyfert_2", "label": "Seyfert 2 Galaxy "},
        {"value": "LSB_G", "label": "Low Surface Brightness Galaxy"},
        {"value": "LINER", "label": "LINER-type Active Galaxy Nucleus"},
        {"value": "GinCl", "label": "Galaxy in Cluster of Galaxies"},
        {"value": "RadioG", "label": "Radio Galaxy"},
        {"value": "Seyfert", "label": "Seyfert Galaxy "},
        {"value": "BClG", "label": "Brightest galaxy in a Cluster (BCG)"},
        {"value": "BlueCompG", "label": "Blue compact Galaxy"},
        {"value": "HII_G", "label": "HII Galaxy"},
        {"value": "QSO_Candidate", "label": "Possible Quasar"},
        {"value": "Seyfert_1", "label": "Seyfert 1 Galaxy"},
        {"value": "StarburstG", "label": "Starburst Galaxy"},
        {"value": "QSO", "label": "Quasar"},
        {"value": "Blazar", "label": "Blazar"},
        {"value": "BLLac", "label": "BL Lac - type object"},
        {"value": "PartofG", "label": "Part of a Galaxy"}]},
    {"uniname": "Interstellar matter", "data": [
        {"value": "PN", "label": "Planetary Nebula"},
        {"value": "HII", "label": "HII (ionized) region"},
        {"value": "ISM", "label": "Interstellar matter"},
        {"value": "RfNeb", "label": "Reflection Nebula"},
        {"value": "HH", "label": "Herbig-Haro Object"},
        {"value": "EmObj", "label": "Emission Object"},
        {"value": "SNR", "label": "SuperNova Remnant"},
        {"value": "BrNeb", "label": "Bright Nebula"},
        {"value": "GalNeb", "label": "Galactic Nebula"},
        {"value": "HIshell", "label": "HI shell"},
        {"value": "MolCld", "label": "Molecular Cloud"}]},
    {"uniname": "Unknown", "data": [
        {"value": "Unknown", "label": "Object of unknown nature "}]},
    {"uniname": "Star", "data": [
        {"value": "Star", "label": "Star"},
        {"value": "Em*", "label": "Emission-line Star"},
        {"value": "Ae*", "label": "Herbig Ae/Be star"},
        {"value": "Orion_V*", "label": "Variable Star of Orion Type"},
        {"value": "WR*", "label": "Wolf-Rayet Star"},
        {"value": "*inCl", "label": "Star in Cluster"}]},
    {"uniname": "Composite object", "data": [
        {"value": "OpCl", "label": "Open (galactic) Cluster "},
        {"value": "GlCl", "label": "Globular Cluster"},
        {"value": "Cl*", "label": "Cluster of Stars"},
        {"value": "Assoc*", "label": "Association of Stars"},
        {"value": "PairG", "label": "Pair of Galaxies"},
        {"value": "multiple_object", "label": "Composite object"},
        {"value": "**", "label": "Double or multiple star"},
        {"value": "Cl*?", "label": "Possible (open) star cluster"},
        {"value": "MouvGroup", "label": "Moving Group"},
        {"value": "GroupG", "label": "Group of Galaxies"},
        {"value": "SB*", "label": "Spectroscopic binary"},
        {"value": "Nova", "label": "Nova"},
        {"value": "EB*Algol", "label": "Eclipsing binary of Algol type"},
        {"value": "ClG", "label": "Cluster of Galaxies"}]},
    {"uniname": "Infra-Red source", "data": [
        {"value": "IR", "label": "Infra-Red source"}]},
    ]
    // IE compability
    var doctop = function(){
        if(document.documentElement && document.documentElement.scrollTop)
        {return document.documentElement.scrollTop}
        if(document.body.scrollTop)
        {return document.body.scrollTop}}
    var dochaight =function(){
        if(document.documentElement && document.documentElement.scrollHeight)
        {return document.documentElement.scrollHeight}
        if(document.body.scrollHeight)
        {return document.body.scrollHeight}
        else return 0;}
