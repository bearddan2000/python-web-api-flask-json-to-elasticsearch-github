import unittest

from schema import configurations

class TestSchemaConsts(unittest.TestCase):

    def test_configurations_exists(self):
        self.assertIsNotNone(configurations, 'configurations variable is None')
    
    def test_configurations_settings_exists(self):
        self.assertIsNotNone(configurations['settings'], 'configurations settings is None')
    
    def test_configurations_settings_analyzer_exists(self):
        self.assertIsNotNone(configurations['settings']['analysis']['analyzer'], 'configurations settings analysis analyzer is None')
    
    def test_configurations_mappings_exists(self):
        self.assertIsNotNone(configurations['mappings'], 'configurations mappings is None')
    
    def test_configurations_mappings_properties_exists(self):
        self.assertIsNotNone(configurations['mappings']['properties'], 'configurations mappings properties is None')

    def test_configurations_mappings_properties_name_exists(self):
        self.assertIsNotNone(configurations['mappings']['properties']['name'], 'configurations mappings properties name is None')

    def test_configurations_mappings_properties_name_type_exists(self):
        self.assertIsNotNone(configurations['mappings']['properties']['name']['type'], 'configurations mappings properties name type is None')

    def test_configurations_mappings_properties_name_type_equals(self):
        self.assertEqual(configurations['mappings']['properties']['name']['type'], 'keyword', 'configurations mappings properties name type is not keyword')

    def test_configurations_mappings_properties_desc_exists(self):
        self.assertIsNotNone(configurations['mappings']['properties']['desc'], 'configurations mappings properties desc is None')

    def test_configurations_mappings_properties_desc_type_exists(self):
        self.assertIsNotNone(configurations['mappings']['properties']['desc']['type'], 'configurations mappings properties desc type is None')

    def test_configurations_mappings_properties_desc_type_equals(self):
        self.assertEqual(configurations['mappings']['properties']['desc']['type'], 'text', 'configurations mappings properties desc type is not text')

    def test_configurations_mappings_properties_desc_analyzer_exists(self):
        self.assertIsNotNone(configurations['mappings']['properties']['desc']['analyzer'], 'configurations mappings properties desc analyzer is None')

    def test_configurations_mappings_properties_desc_analyzer_equals(self):
        self.assertEqual(configurations['mappings']['properties']['desc']['analyzer'], 'standard', 'configurations mappings properties desc analyzer is not standard')

    def test_configurations_mappings_properties_topics_exists(self):
        self.assertIsNotNone(configurations['mappings']['properties']['topics'], 'configurations mappings properties topics is None')

    def test_configurations_mappings_properties_topics_type_exists(self):
        self.assertIsNotNone(configurations['mappings']['properties']['topics']['type'], 'configurations mappings properties topics type is None')

    def test_configurations_mappings_properties_topics_type_equals(self):
        self.assertEqual(configurations['mappings']['properties']['topics']['type'], 'keyword', 'configurations mappings properties topics type is not keyword')

    def test_configurations_mappings_properties_filter_build_name_exists(self):
        self.assertIsNotNone(configurations['mappings']['properties']['filter.build.name'], 'configurations mappings properties filter.build.name is None')

    def test_configurations_mappings_properties_filter_build_name_type_exists(self):
        self.assertIsNotNone(configurations['mappings']['properties']['filter.build.name']['type'], 'configurations mappings properties filter.build.name type is None')

    def test_configurations_mappings_properties_filter_build_name_type_equals(self):
        self.assertEqual(configurations['mappings']['properties']['filter.build.name']['type'], 'keyword', 'configurations mappings properties filter.build.name type is not keyword')

    def test_configurations_mappings_properties_filter_build_color_exists(self):
        self.assertIsNotNone(configurations['mappings']['properties']['filter.build.color'], 'configurations mappings properties filter.build.color is None')

    def test_configurations_mappings_properties_filter_build_color_type_exists(self):
        self.assertIsNotNone(configurations['mappings']['properties']['filter.build.color']['type'], 'configurations mappings properties filter.build.color type is None')

    def test_configurations_mappings_properties_filter_build_color_type_equals(self):
        self.assertEqual(configurations['mappings']['properties']['filter.build.color']['type'], 'text', 'configurations mappings properties filter.build.color type is not text')

    def test_configurations_mappings_properties_filter_language_name_exists(self):
        self.assertIsNotNone(configurations['mappings']['properties']['filter.language.name'], 'configurations mappings properties filter.language.name is None')

    def test_configurations_mappings_properties_filter_language_name_type_exists(self):
        self.assertIsNotNone(configurations['mappings']['properties']['filter.language.name']['type'], 'configurations mappings properties filter.language.name type is None')

    def test_configurations_mappings_properties_filter_language_name_type_equals(self):
        self.assertEqual(configurations['mappings']['properties']['filter.language.name']['type'], 'keyword', 'configurations mappings properties filter.language.name type is not keyword')

    def test_configurations_mappings_properties_filter_language_color_exists(self):
        self.assertIsNotNone(configurations['mappings']['properties']['filter.language.color'], 'configurations mappings properties filter.language.color is None')

    def test_configurations_mappings_properties_filter_language_color_type_exists(self):
        self.assertIsNotNone(configurations['mappings']['properties']['filter.language.color']['type'], 'configurations mappings properties filter.language.color type is None')

    def test_configurations_mappings_properties_filter_language_color_type_equals(self):
        self.assertEqual(configurations['mappings']['properties']['filter.language.color']['type'], 'text', 'configurations mappings properties filter.language.color type is not text')

    def test_configurations_mappings_properties_filter_platform_name_exists(self):
        self.assertIsNotNone(configurations['mappings']['properties']['filter.platform.name'], 'configurations mappings properties filter.platform.name is None')

    def test_configurations_mappings_properties_filter_platform_name_type_exists(self):
        self.assertIsNotNone(configurations['mappings']['properties']['filter.platform.name']['type'], 'configurations mappings properties filter.platform.name type is None')

    def test_configurations_mappings_properties_filter_platform_name_type_equals(self):
        self.assertEqual(configurations['mappings']['properties']['filter.platform.name']['type'], 'keyword', 'configurations mappings properties filter.platform.name type is not keyword')

    def test_configurations_mappings_properties_filter_platform_color_exists(self):
        self.assertIsNotNone(configurations['mappings']['properties']['filter.platform.color'], 'configurations mappings properties filter.platform.color is None')

    def test_configurations_mappings_properties_filter_platform_color_type_exists(self):
        self.assertIsNotNone(configurations['mappings']['properties']['filter.platform.color']['type'], 'configurations mappings properties filter.platform.color type is None')

    def test_configurations_mappings_properties_filter_platform_color_type_equals(self):
        self.assertEqual(configurations['mappings']['properties']['filter.platform.color']['type'], 'text', 'configurations mappings properties filter.platform.color type is not text')

    def test_configurations_mappings_properties_filter_tech_name_exists(self):
        self.assertIsNotNone(configurations['mappings']['properties']['filter.tech.name'], 'configurations mappings properties filter.tech.name is None')

    def test_configurations_mappings_properties_filter_tech_name_type_exists(self):
        self.assertIsNotNone(configurations['mappings']['properties']['filter.tech.name']['type'], 'configurations mappings properties filter.tech.name type is None')

    def test_configurations_mappings_properties_filter_tech_name_type_equals(self):
        self.assertEqual(configurations['mappings']['properties']['filter.tech.name']['type'], 'keyword', 'configurations mappings properties filter.tech.name type is not keyword')

    def test_configurations_mappings_properties_filter_tech_color_exists(self):
        self.assertIsNotNone(configurations['mappings']['properties']['filter.tech.color'], 'configurations mappings properties filter.tech.color is None')

    def test_configurations_mappings_properties_filter_tech_color_type_exists(self):
        self.assertIsNotNone(configurations['mappings']['properties']['filter.tech.color']['type'], 'configurations mappings properties filter.tech.color type is None')

    def test_configurations_mappings_properties_filter_tech_color_type_equals(self):
        self.assertEqual(configurations['mappings']['properties']['filter.tech.color']['type'], 'text', 'configurations mappings properties filter.tech.color type is not text')

    def test_configurations_mappings_properties_catagory_catagory_exists(self):
        self.assertIsNotNone(configurations['mappings']['properties']['catagory.catagory'], 'configurations mappings properties catagory.catagory is None')

    def test_configurations_mappings_properties_catagory_catagory_type_exists(self):
        self.assertIsNotNone(configurations['mappings']['properties']['catagory.catagory']['type'], 'configurations mappings properties catagory.catagory type is None')

    def test_configurations_mappings_properties_catagory_catagory_type_equals(self):
        self.assertEqual(configurations['mappings']['properties']['catagory.catagory']['type'], 'keyword', 'configurations mappings properties catagory.catagory type is not keyword')

    def test_configurations_mappings_properties_catagory_subcatagory_exists(self):
        self.assertIsNotNone(configurations['mappings']['properties']['catagory.subcatagory'], 'configurations mappings properties catagory.subcatagory is None')

    def test_configurations_mappings_properties_catagory_subcatagory_type_exists(self):
        self.assertIsNotNone(configurations['mappings']['properties']['catagory.subcatagory']['type'], 'configurations mappings properties catagory.subcatagory type is None')

    def test_configurations_mappings_properties_catagory_subcatagory_type_equals(self):
        self.assertEqual(configurations['mappings']['properties']['catagory.subcatagory']['type'], 'keyword', 'configurations mappings properties catagory.subcatagory type is not keyword')

if __name__ == '__main__':
    unittest.main()

