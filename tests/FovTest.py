__author__ = 'Jakub Wojtanek, Kwojtanek@gmail.com'
import unittest
import re

def Fov(dimAxb):
    """
    Function returns Field of view that will be passed to alladin    """
    x = 0
    if dimAxb:
        pattern = re.compile('\d+')
        numb = re.findall(pattern,dimAxb)
        for n in numb:
            if n >= x:
                x = n
        return float(x)*1.8
    else:
        return None


class Test(unittest.TestCase):
    def testFov(self):
        a = '20 x 20'
        b = '20 x'
        c= '10'
        d = 'x'
        self.assertEqual(Fov(a),36.)
        self.assertEqual(Fov(b),36.)
        self.assertEqual(Fov(c),18. )
        self.assertEqual(Fov(d),None)


if __name__ == '__main__':
    unittest.main()
