import unittest
from fox import Fox, Location, Map, Map_init

class TestMapDictionary(unittest.TestCase):

    def test_map_has_valid_keys(self):
        expected_keys = {'morill_quad', 'chapel_gardens', 'mckeldin_mall', 'amphitheater', 'regents_drive_garage', 'engineering_fields', 'paint_branch_trail'}
        self.assertEqual(set(Map.keys()), expected_keys)

    def test_map_values_are_tuples(self):
        for value in Map.values():
            self.assertIsInstance(value, tuple)

    def test_map_values_contain_valid_keys(self):
        for value in Map.values():
            for location in value:
                if location == 'beyond': #fox got away
                    continue
                else:
                    self.assertIn(location, Map.keys())

class TestMapInit(unittest.TestCase):

    def test_map_init(self):
        locations = Map_init()
        for location in Map.keys():
            self.assertIsInstance(locations[location], Location)

class TestFox(unittest.TestCase):

    def test_spawn(self):
        fox = Fox()
        fox.spawn()
        self.assertIn(fox.location, Map.keys())

    def test_foxtrot(self):
        fox = Fox()
        fox.spawn()
        start_location = fox.location
        fox.foxtrot()
        self.assertIn(fox.location, Map[start_location])

class TestLocation(unittest.TestCase):

    def test_location_object(self):
        location = Location("Fox is present", "Fox is absent")
        self.assertEqual(location.present_prompt, "Fox is present")
        self.assertEqual(location.absent_prompt, "Fox is absent")
        self.assertFalse(location.present)

if __name__ == '__main__':
    unittest.main()
