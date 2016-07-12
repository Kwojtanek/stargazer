var min_mag = 0;
var max_mag = 23.8;
var maxid = 32471;
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
    {
        'value': 'NGC',
        'label': 'New General Catalogue'},
    {
        'value': 'PGC',
        'label': 'Principal Galaxies Catalogue'
    },
    {
        'value': 'Messier',
        'label': 'Messier Objects Catalouge'
    },
    {
        'value': 'IC',
        'label': 'Index Catalouge'
    },
    {
        'value': 'UGC',
        'label': 'Uppsala General Catalogue'
    },
    {
        'value': 'HCG',
        'label': 'Hickson Compact Group'
    },
    {
        'value': 'GCL',
        'label': 'Globular Clusters'
    },
    {
        'value': 'OCL',
        'label': 'Open Clusters'
    }
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
[{"uniname": "Infra-Red source", "data": [{"value": "IR>30um", "label": "FIR"}, {"value": "IR<10um", "label": "NIR"}]},
 {"uniname": "Composite object", "data": [{"value": "Region", "label": "reg"}, {"value": "Void", "label": "vid"}, {"value": "SuperClG", "label": "SCG"}, {"value": "ClG", "label": "ClG"}, {"value": "GroupG", "label": "GrG"}, {"value": "Compact_Gr_G", "label": "CGG"}, {"value": "PairG", "label": "PaG"}, {"value": "IG", "label": "IG"}, {"value": "Cl*?", "label": "C?*"}, {"value": "GlCl?", "label": "Gl?"}, {"value": "Cl*", "label": "Cl*"}, {"value": "GlCl", "label": "GlC"}, {"value": "OpCl", "label": "OpC"}, {"value": "Assoc*", "label": "As*"}, {"value": "Stream*", "label": "St*"}, {"value": "MouvGroup", "label": "MGr"}, {"value": "**", "label": "**"}, {"value": "EB*", "label": "EB*"}, {"value": "EB*Algol", "label": "Al*"}, {"value": "EB*betLyr", "label": "bL*"}, {"value": "EB*WUMa", "label": "WU*"}, {"value": "EB*Planet", "label": "EP*"}, {"value": "SB*", "label": "SB*"}, {"value": "EllipVar", "label": "El*"}, {"value": "Symbiotic*", "label": "Sy*"}, {"value": "CataclyV*", "label": "CV*"}, {"value": "DQHer", "label": "DQ*"}, {"value": "AMHer", "label": "AM*"}, {"value": "Nova-like", "label": "NL*"}, {"value": "Nova", "label": "No*"}, {"value": "DwarfNova", "label": "DN*"}, {"value": "XB", "label": "XB*"}, {"value": "LMXB", "label": "LXB"}, {"value": "HMXB", "label": "HXB"}]}, {"uniname": "Interstellar matter", "data": [{"value": "PartofCloud", "label": "PoC"}, {"value": "PN?", "label": "PN?"}, {"value": "ComGlob", "label": "CGb"}, {"value": "Bubble", "label": "bub"}, {"value": "EmObj", "label": "EmO"}, {"value": "Cloud", "label": "Cld"}, {"value": "GalNeb", "label": "GNe"}, {"value": "BrNeb", "label": "BNe"}, {"value": "DkNeb", "label": "DNe"}, {"value": "RfNeb", "label": "RNe"}, {"value": "MolCld", "label": "MoC"}, {"value": "Globule", "label": "glb"}, {"value": "denseCore", "label": "cor"}, {"value": "SFregion", "label": "SFR"}, {"value": "HVCld", "label": "HVC"}, {"value": "HII", "label": "HII"}, {"value": "PN", "label": "PN"}, {"value": "HIshell", "label": "sh"}, {"value": "SNR?", "label": "SR?"}, {"value": "SNR", "label": "SNR"}, {"value": "Circumstellar", "label": "cir"}, {"value": "outflow?", "label": "of?"}, {"value": "Outflow", "label": "out"}, {"value": "HH", "label": "HH"}]}, {"uniname": "Star", "data": [{"value": "*inCl", "label": "*iC"}, {"value": "*inNeb", "label": "*iN"}, {"value": "*inAssoc", "label": "*iA"}, {"value": "*in**", "label": "*i*"}, {"value": "V*?", "label": "V*?"}, {"value": "Pec*", "label": "Pe*"}, {"value": "HB*", "label": "HB*"}, {"value": "YSO", "label": "Y*O"}, {"value": "Ae*", "label": "Ae*"}, {"value": "Em*", "label": "Em*"}, {"value": "Be*", "label": "Be*"}, {"value": "BlueStraggler", "label": "BS*"}, {"value": "RGB*", "label": "RG*"}, {"value": "AGB*", "label": "AB*"}, {"value": "C*", "label": "C*"}, {"value": "S*", "label": "S*"}, {"value": "SG*", "label": "sg*"}, {"value": "RedSG*", "label": "s*r"}, {"value": "YellowSG*", "label": "s*y"}, {"value": "BlueSG*", "label": "s*b"}, {"value": "post-AGB*", "label": "pA*"}, {"value": "WD*", "label": "WD*"}, {"value": "pulsWD*", "label": "ZZ*"}, {"value": "low-mass*", "label": "LM*"}, {"value": "brownD*", "label": "BD*"}, {"value": "Neutron*", "label": "N*"}, {"value": "OH/IR", "label": "OH*"}, {"value": "CH", "label": "CH*"}, {"value": "pMS*", "label": "pr*"}, {"value": "TTau*", "label": "TT*"}, {"value": "WR*", "label": "WR*"}, {"value": "PM*", "label": "PM*"}, {"value": "HV*", "label": "HV*"}, {"value": "V*", "label": "V*"}, {"value": "Irregular_V*", "label": "Ir*"}, {"value": "Orion_V*", "label": "Or*"}, {"value": "Rapid_Irreg_V*", "label": "RI*"}, {"value": "Eruptive*", "label": "Er*"}, {"value": "Flare*", "label": "Fl*"}, {"value": "FUOr", "label": "FU*"}, {"value": "Erupt*RCrB", "label": "RC*"}, {"value": "RCrB_Candidate", "label": "RC?"}, {"value": "RotV*", "label": "Ro*"}, {"value": "RotV*alf2CVn", "label": "a2*"}, {"value": "Pulsar", "label": "Psr"}, {"value": "BYDra", "label": "BY*"}, {"value": "RSCVn", "label": "RS*"}, {"value": "PulsV*", "label": "Pu*"}, {"value": "RRLyr", "label": "RR*"}, {"value": "Cepheid", "label": "Ce*"}, {"value": "PulsV*delSct", "label": "dS*"}, {"value": "PulsV*RVTau", "label": "RV*"}, {"value": "PulsV*WVir", "label": "WV*"}, {"value": "PulsV*bCep", "label": "bC*"}, {"value": "deltaCep", "label": "cC*"}, {"value": "gammaDor", "label": "gD*"}, {"value": "pulsV*SX", "label": "SX*"}, {"value": "LPV*", "label": "LP*"}, {"value": "Mira", "label": "Mi*"}, {"value": "semi-regV*", "label": "sr*"}, {"value": "SN", "label": "SN*"}, {"value": "Sub-stellar", "label": "su*"}, {"value": "Planet?", "label": "Pl?"}, {"value": "Planet", "label": "Pl"}]}, {"uniname": "Galaxy", "data": [{"value": "PartofG", "label": "PoG"}, {"value": "GinCl", "label": "GiC"}, {"value": "BClG", "label": "BiC"}, {"value": "GinGroup", "label": "GiG"}, {"value": "GinPair", "label": "GiP"}, {"value": "High_z_G", "label": "HzG"}, {"value": "AbsLineSystem", "label": "ALS"}, {"value": "Ly-alpha_ALS", "label": "LyA"}, {"value": "DLy-alpha_ALS", "label": "DLA"}, {"value": "metal_ALS", "label": "mAL"}, {"value": "Ly-limit_ALS", "label": "LLS"}, {"value": "Broad_ALS", "label": "BAL"}, {"value": "RadioG", "label": "rG"}, {"value": "HII_G", "label": "H2G"}, {"value": "LSB_G", "label": "LSB"}, {"value": "AGN_Candidate", "label": "AG?"}, {"value": "QSO_Candidate", "label": "Q?"}, {"value": "Blazar_Candidate", "label": "Bz?"}, {"value": "BLLac_Candidate", "label": "BL?"}, {"value": "EmG", "label": "EmG"}, {"value": "StarburstG", "label": "SBG"}, {"value": "BlueCompG", "label": "bCG"}, {"value": "LensedImage", "label": "LeI"}, {"value": "LensedG", "label": "LeG"}, {"value": "LensedQ", "label": "LeQ"}, {"value": "AGN", "label": "AGN"}, {"value": "LINER", "label": "LIN"}, {"value": "Seyfert", "label": "SyG"}, {"value": "Seyfert_1", "label": "Sy1"}, {"value": "Seyfert_2", "label": "Sy2"}, {"value": "Blazar", "label": "Bla"}, {"value": "BLLac", "label": "BLL"}, {"value": "OVV", "label": "OVV"}, {"value": "QSO", "label": "QSO"}]}]

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
