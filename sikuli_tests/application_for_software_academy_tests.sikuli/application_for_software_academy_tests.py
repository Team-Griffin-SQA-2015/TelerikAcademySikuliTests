from _lib import *
import unittest
import time

bdLibPath=os.path.abspath(sys.argv[0]+"..")
if not bdLibPath in sys.path:
    sys.path.append(bdLibPath)

class ApplicationForSoftwareAcademyTests(unittest.TestCase):
    def setUp(self):
        RunBrowserToUrl("chrome","http://stage.telerikacademy.com/")
        sleep(3)

    def tearDown(self):
        pass

    def test_001_NavigateToApplicationWithoutLogin(self):
        if exists(MainPage.logoutButton):
            click(MainPage.logoutButton)
        sleep(3)
        wait(MainPage.enterButton)
        wait(MainPage.telerikAcademyMenu)
        hover(MainPage.telerikAcademyMenu)
        wait(MainPage.applicationForAcademyMenu)
        click(MainPage.applicationForAcademyMenu)
        wait(LoginPage.loginHeading, 30)
        assert exists(LoginPage.loginHeading)

    def test_002_NavigateToApplicationWithLoggedUser(self):
        if exists(MainPage.enterButton):
            AdminLogin("griffin","Start123")
        sleep(3)
        hover(MainPage.telerikAcademyMenu)
        wait(MainPage.applicationForAcademyMenu)
        click(MainPage.applicationForAcademyMenu)
        wait(EntryExam.applicationForAcademyHeading)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ApplicationForSoftwareAcademyTests)
    outfile = open("_application_for_software_academy_tests_report.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='Application for software academy tests Report')
    runner.run(suite)
    outfile.close()