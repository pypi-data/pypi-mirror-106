import unittest
try:
    from . import email_alerts
    from . import auth
except:
    import email_alerts
    import auth

class POC_TestCase(unittest.TestCase):
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

class Full(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.auth = auth.load_file_auth("env.json")

    @classmethod
    def tearDownClass(cls):
        cls.auth = None

    def test_auth(self):
        print("Loaded auth file")
        print(Full.auth)

    def test_email_alert(self):
        print(">>> Sending alert <<<")
        result = email_alerts.send(auth=Full.auth,subject="test")
        print("Alert sent")
    
    def test_email_alert_no_auth(self):
        print("Trying with no auth")
        result = email_alerts.send()
    
def run_selected_tests():
    suite = unittest.TestSuite()
    suite.addTest(Full('test_email_alert_no_auth'))
    return suite

if __name__ == '__main__':
    # unittest.main(Full())
    #### run suite: ####
    runner = unittest.TextTestRunner()
    runner.run(run_selected_tests())
