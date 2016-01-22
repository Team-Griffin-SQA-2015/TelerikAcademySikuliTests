from _uimap import *
from _lib import *
from sikuli import *
import HTMLTestRunner
import unittest
bdLibPath = os.path.abspath(sys.argv[0] + "..")
if not bdLibPath in sys.path: sys.path.append(bdLibPath)


class SmokeTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

################################################################################
########################## Navigate To User Settings ###########################
################################################################################

    def test_001_NavigateToTelerikAcademy(self):
        runBrowserToUrl(defaultBrowser, baseUrl)

    def test_002_LoginUser(self):
        switchToAddressBar()
        navigateTo(baseUrl + "/Users/Auth/Login")
        enterUserCredentials(defaultUsername, defaultPassword)

    def test_003_NavigateToUserSettings(arg):
        switchToAddressBar()
        navigateTo(baseUrl + "/Users/Profile/Settings")

################################################################################
################################ First Name En #################################
################################################################################

    # Boundary value anaylis testing lower limit of first name in english
    # (minValue=2)
    def test_004_ValidateFirstNameEn_OneSymbol(self):
        pageDownToVisible(UserSettings.label_FirstNameEn)
        changeInputData(UserSettings.label_FirstNameEn, "T")
        submitChanges()
        wait(UserSettings.message_InvalidMinLengthFirstName, 5)
        self.assertTrue(exists(UserSettings.message_InvalidMinLengthFirstName))

    def test_005_ValidateFirstNameEn_TwoSymbols(self):
        pageDownToVisible(UserSettings.label_FirstNameEn)
        changeInputData(UserSettings.label_FirstNameEn, "Te")
        submitChanges()
        wait(UserSettings.message_Success, 5)
        self.assertTrue(exists(UserSettings.message_Success))

    def test_006_ValidateFirstNameEn_ThreeSymbols(self):
        pageDownToVisible(UserSettings.label_FirstNameEn)
        changeInputData(UserSettings.label_FirstNameEn, "Tes")
        submitChanges()
        wait(UserSettings.message_Success, 5)
        self.assertTrue(exists(UserSettings.message_Success))

    # Boundary value anaylis testing upper limit of first name in english
    # (maxValue=30)
    def test_007_ValidateFirstNameEn_TwentyNineSymbol(self):
        pageDownToVisible(UserSettings.label_FirstNameEn)
        changeInputData(UserSettings.label_FirstNameEn, "TesttesttesttestTesttesttestT")
        submitChanges()
        wait(UserSettings.message_Success, 5)
        self.assertTrue(exists(UserSettings.message_Success))

    def test_008_ValidateFirstNameEn_ThirtySymbols(self):
        pageDownToVisible(UserSettings.label_FirstNameEn)
        changeInputData(UserSettings.label_FirstNameEn, "TesttesttesttestTesttesttestTe")
        submitChanges()
        wait(UserSettings.message_Success, 5)
        self.assertTrue(exists(UserSettings.message_Success))

    def test_009_ValidateFirstNameEn_ThirtyOneSymbols(self):
        pageDownToVisible(UserSettings.label_FirstNameEn)
        changeInputData(UserSettings.label_FirstNameEn, "TesttesttesttestTesttesttestTes")
        submitChanges()
        wait(UserSettings.message_InvalidMaxLengthFirstName, 5)
        self.assertTrue(exists(UserSettings.message_InvalidMaxLengthFirstName))

    def test_010_ResetFirstNameEn(self):
        changeInputData(UserSettings.label_FirstNameEn, "")
        submitChanges()
        wait(UserSettings.message_Success, 5)
        self.assertTrue(exists(UserSettings.message_Success))

################################################################################
################################ Last Name En ##################################
################################################################################

    # Boundary value anaylis testing lower limit of last name in english
    # (minValue=2)
    def test_011_ValidateLastNameEn_OneSymbol(self):
        pageDownToVisible(UserSettings.label_LastNameEn)
        changeInputData(UserSettings.label_LastNameEn, "T")
        submitChanges()
        wait(UserSettings.message_InvalidMinLengthLastName, 5)
        self.assertTrue(exists(UserSettings.message_InvalidMinLengthLastName))

    def test_012_ValidateLastNameEn_TwoSymbols(self):
        pageDownToVisible(UserSettings.label_LastNameEn)
        changeInputData(UserSettings.label_LastNameEn, "Te")
        submitChanges()
        wait(UserSettings.message_Success, 5)
        self.assertTrue(exists(UserSettings.message_Success))

    def test_013_ValidateLastNameEn_ThreeSymbols(self):
        pageDownToVisible(UserSettings.label_LastNameEn)
        changeInputData(UserSettings.label_LastNameEn, "Tes")
        submitChanges()
        wait(UserSettings.message_Success, 5)
        self.assertTrue(exists(UserSettings.message_Success))

    # Boundary value anaylis testing upper limit of last name in english
    # (maxValue=30)
    def test_014_ValidateLastNameEn_TwentyNineSymbol(self):
        pageDownToVisible(UserSettings.label_LastNameEn)
        changeInputData(UserSettings.label_LastNameEn, "TesttesttesttestTesttesttestT")
        submitChanges()
        wait(UserSettings.message_Success, 5)
        self.assertTrue(exists(UserSettings.message_Success))

    def test_015_ValidateLastNameEn_ThirtySymbols(self):
        pageDownToVisible(UserSettings.label_LastNameEn)
        changeInputData(UserSettings.label_LastNameEn, "TesttesttesttestTesttesttestTe")
        submitChanges()
        wait(UserSettings.message_Success, 5)
        self.assertTrue(exists(UserSettings.message_Success))

    def test_016_ValidateLastNameEn_ThirtyOneSymbols(self):
        pageDownToVisible(UserSettings.label_LastNameEn)
        changeInputData(UserSettings.label_LastNameEn, "TesttesttesttestTesttesttestTes")
        submitChanges()
        wait(UserSettings.message_InvalidMaxLengthLastName, 5)
        self.assertTrue(exists(UserSettings.message_InvalidMaxLengthLastName))

    def test_017_ResetFirstNameEn(self):
        changeInputData(UserSettings.label_LastNameEn, "")
        submitChanges()
        wait(UserSettings.message_Success, 5)
        self.assertTrue(exists(UserSettings.message_Success))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SmokeTests)
    outfile = open("report.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='SmokeTests Report')
    runner.run(suite)
    outfile.close()
