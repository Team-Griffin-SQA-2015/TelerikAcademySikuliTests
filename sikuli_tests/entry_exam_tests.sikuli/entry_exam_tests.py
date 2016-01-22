import unittest
import time
bdLibPath=os.path.abspath(sys.argv[0]+"..")
if not bdLibPath in sys.path: sys.path.append(bdLibPath)
from _lib import *


class EntryExamTests(unittest.TestCase):
    def setUp(self):
        RunBrowserToUrl("chrome","http://stage.telerikacademy.com/")
        sleep(3)

    def tearDown(self):
        pass

    def test_001_NavigateToEntryExamWithLoggedUser(self):
        if exists(MainPage.enterButton):
            AdminLogin("griffin","Start123")
        sleep(3)
        hover(MainPage.telerikAcademyMenu)
        wait(MainPage.entryExamMenu)
        click(MainPage.entryExamMenu)

        wheel(EntryExam.applicationForAcademyHeading, WHEEL_DOWN, 2)
        assert exists(EntryExam.applicationForAcademyHeading)
        #self.assertTrue(exists(EntryExam.applicationForAcademyHeading))

    def test_002_NavigateToEntryExamWithoutLogin(self):
        if exists(MainPage.logoutButton):
            click(MainPage.logoutButton)
        sleep(3)
        wait(MainPage.enterButton)
        wait(MainPage.telerikAcademyMenu)
        hover(MainPage.telerikAcademyMenu)
        wait(MainPage.entryExamMenu)
        click(MainPage.entryExamMenu)
        wait(LoginPage.loginHeading, 30)
        assert exists(LoginPage.loginHeading)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(EntryExamTests)

    outfile = open("_entry_exam_tests_report.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='Entry Exam Tests Report')
    runner.run(suite)
    outfile.close()