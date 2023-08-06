import unittest
from os.path import join
from FadeMaxSize.findMax import find_max_file 


class MaxTest(unittest.TestCase):
    
    def test_v1(self):
        self.assertEqual(find_max_file(join('tests', 'test_folder')), {
            'file': join('tests', 'test_folder', 'Firefox_Installer.test'),
            'size': 325.2890625
        })

    def test_v2(self):
        self.assertEqual(find_max_file(join('tests', 'test_folder', 'test')), {
            'file': join('tests', 'test_folder', 'test', 'test_2', 'oeAa5ViXYD0.jpg'),
            'size': 113.3349609375
        })  

    def test_v3(self):
        self.assertEqual(find_max_file(join('tests', 'test_folder', 'test', 'test_1')), {
            'file': join('tests', 'test_folder', 'test', 'test_1', 'test_3', 'fwe2.txt'),
            'size': 37.533203125
        })


if __name__ == '__main__':
    unittest.main()