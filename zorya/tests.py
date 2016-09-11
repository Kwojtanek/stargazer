from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory
from django.core.urlresolvers import reverse
from zorya.models import StellarObject
from django.test import TestCase
import json
class UpdateCreateApiTest(TestCase):
    data = {u'unique_name': u'Messier 45', u'overview': u'In astronomy, the Pleiades (/?pla?.?di?z/ or /?pli?.?di?z/), or Seven Sisters (Messier 45 or M45), is an open star cluster containing middle-aged hot B-type stars located in the constellation of Taurus. It is among the nearest star clusters to Earth and is the cluster most obvious to the naked eye in the night sky. The celestial entity has several meanings in different cultures and traditions.\\nThe cluster is dominated by hot blue and extremely luminous stars that have formed within the last 100 million years. Dust that forms a faint reflection nebulosity around the brightest stars was thought at first to be left over from the formation of the cluster (hence the alternative name Maia Nebula after the star Maia), but is now known to be an unrelated dust cloud in the interstellar medium, through which the stars are currently passing. Computer simulations have shown that the Pleiades was probably formed from a compact configuration that resembled the Orion Nebula. Astronomers estimate that the cluster will survive for about another 250 million years, after which it will disperse due to gravitational interactions with its galactic neighborhood.', u'type_shortcut': u'OpCl', u'otype': u'Composite object', u'declination': u'+24 0', u'rightAsc': u'03:47:00', u'type': u'Open (galactic) Cluster ', u'constelation': 17}
    def setUp(self):
        StellarObject.objects.create(**self.data)
    def testCreate(self):
        M45 = StellarObject.objects.get(unique_name=u'Messier 45')
        self.assertEqual(M45.type_shortcut,'OpCl')

