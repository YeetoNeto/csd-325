import unittest
# Program that stores a function that accepts two paramters City, Country
import CityFunctions

class test_cityCountry(unittest.TestCase):

    def test_city_country(self):
        self.assertEqual(CityFunctions.cityCountry('Santiago', 'Chile'), 'Santiago,Chile')



#if check to potentially use this function in a future program without triggering main. Took inspiration from the textbook for this
if __name__ == '__main__': 
    unittest.main()