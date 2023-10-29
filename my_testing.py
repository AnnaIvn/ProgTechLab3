import unittest
import lab3_flask_app as prog

class FlaskAppTests(unittest.TestCase):

    # basic setup
    def setUp(self):
        # self.prog = prog
        self.prog = prog.app.test_client()

    # test for checking format 
    def test_check_format(self):
        self.assertTrue(prog.check_format('6Ben Schaefer'))     # correct
        self.assertTrue(prog.check_format('7Findlay Shaffer'))  # correct
        self.assertTrue(prog.check_format('8Kara Moss'))        # correct
        self.assertFalse(prog.check_format('Pen'))              # no age + incorrect length
        self.assertFalse(prog.check_format('Emre Walls'))       # no age
        self.assertFalse(prog.check_format('5Asa Rojas'))       # incorrect age
        self.assertFalse(prog.check_format('9Casey Long'))      # incorrect age
        self.assertFalse(prog.check_format('9E'))               # incorrect length


    # test for adding ':' character if needed
    def test_two_dot_formating(self):
        self.assertEqual(prog.two_dot_formating('6Anna Rou'), '6:Anna Rou')          # changed
        self.assertEqual(prog.two_dot_formating('6:Reg Realmer'), '6:Reg Realmer')   # unchanged


    # test for adding ' ' character if needed
    def test_space_formatting(self):
        self.assertEqual(prog.space_formating('8:Jake Snow'), '8: Jake Snow')      # changed
        self.assertEqual(prog.space_formating('7: Lyla Dylla'), '7: Lyla Dylla')   # unchanged

    # test group distribution
    def test_distrib_by_age(self):
        self.assertEqual(prog.distrib_by_age('6: Andreas Pittman'), '6: Andreas Pittman -> 1st grade')
        self.assertEqual(prog.distrib_by_age('7: Blake Bowman'), '7: Blake Bowman -> 2nd grade')
        self.assertEqual(prog.distrib_by_age('8: Ruth Roy'), '8: Ruth Roy -> 3rd grade')
        self.assertEqual(prog.distrib_by_age('5: Katie Rivera'), '5: Katie Rivera -> Incorrect age')

    def test_exception(self):
        with self.assertRaises(Exception):
            prog.exception('5: Dyllan Bradly')   # returns true exception occurs
            #prog.exception('8: Baley Afton')     # exception doesn't occur
            

    def tearDown(self):
        pass

if __name__ == '__main__':
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()
