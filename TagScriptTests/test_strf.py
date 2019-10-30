import time
import TagScriptEngine

from unittest import TestCase

class test_strf_functionality(TestCase):

    def setUp(self):
        """ Sets up engine and other variables that might be needed between tests """
        self.engine = TagScriptEngine.Engine()
    def tearDown(self):
        """ Cleans the plate to make tests consistent """
        self.engine.Clear_Variables()
        self.engine = None

    # Actual tests below
    # ======
    def test_basic_strf(self):
        year = time.strftime("%Y")
        
        # backwards compativility
        self.assertEqual(self.engine.Process("Hehe, it's strf{%Y}"), f"Hehe, it's {year}")

    def test_percentages(self):
        self.assertEqual(self.engine.Process("strf{%%}"), "%")

    def test_bad_formatting(self):
        self.assert_("<<strf error>> ValueError" in self.engine.Process("strf{%Y-%-m-%d}"))

    def test_complex_datetime(self):
        t = time.gmtime()
        curr_time = time.strftime("%Y-%m-%d", t)
        self.assertEqual(self.engine.Process("strf{%Y-%m-%d}"), curr_time)

    def test_locale(self):
        t = time.gmtime()
        curr_time = time.strftime("%c", t)
        self.assertEqual(self.engine.Process("strf{%c}"), curr_time)

    def test_cuddled_up_variables(self):
        t = time.gmtime()
        huggle_wuggle = time.strftime("%y%y%y%y")
        self.assertEqual(self.engine.process("strf{%y%y%y%y}"), huggle_wuggle)