from sikuli import *
import HTMLTestRunner
import math
import os
bdLibPath = os.path.abspath(sys.argv[0] + "..")
if not bdLibPath in sys.path: sys.path.append(bdLibPath)
from _uimap import *

################################################################################
################################ Nikola Nenov ##################################
################################################################################
def RunBrowserToUrl(browser,toUrl):
    #TestAction("Start " +browser +" "+toUrl)
    sleep(0.5)
    type("d",KEY_WIN); sleep(1)
    type("r", KEY_WIN); sleep(1)
    type(browser+" "); sleep(1)
    type(toUrl); sleep(1)
    type(Key.ENTER)

def StartApp(appName):
    sleep(1)
    type("d",KEY_WIN); sleep(1)
    type("r", KEY_WIN); sleep(1)
    type(appName); sleep(1)
    type(Key.ENTER)

def AdminLogin(username, password):
    click(MainPage.enterButton)
    wait(LoginPage.username)
    click(LoginPage.username)
    type(username)
    type(Key.TAB)
    type(password)
    click(LoginPage.submitButton)

def NavigateToMovedLectures():
    wait(MainPage.adminMenu)
    click(MainPage.adminMenu)
    wait(MainPage.adminMovedLectures)
    click(MainPage.adminMovedLectures)

def ClearGrid():
    wait(MovedLectures.removeItem)

    while exists(MovedLectures.removeItem):
        click(MovedLectures.removeItem)
        wait(MovedLectures.deletePopUp)
        click(MovedLectures.deletePopUp)

def FillInLectureFullDetails():
    wait(MovedLectures.popUpTitle)
    click(MovedLectures.courseDropDown)
    click(MovedLectures.courseDropDownOption)
    click(MovedLectures.startDate)
    type("a",KeyModifier.CTRL)
    type("01/01/2016 01:00:00")
    type(Key.TAB)
    type("01/01/2016 02:00:00")
    type(Key.TAB)
    type("Light")
    click(MovedLectures.updateButton)

def FillInLectureFullInvalidDetails():
    wait(MovedLectures.popUpTitle)
    click(MovedLectures.courseDropDown)
    click(MovedLectures.courseDropDownOption)
    click(MovedLectures.startDate)
    type("a",KeyModifier.CTRL)
    type("01/01/216 01:00:00")
    type(Key.TAB)
    type("01/01/2016 02:00:00")
    type(Key.TAB)
    type("Light")
    click(MovedLectures.updateButton)

################################################################################
############################# Lyudmil Nikodimov ################################
################################################################################

baseUrl = "stage.telerikacademy.com"
defaultBrowser = "iexplore.exe"
defaulBrowserPath = "C:\\Program Files (x86)\\Internet Explorer\\" + defaultBrowser;
defaultUsername = "griffin"
defaultPassword = "Start123"

def maximizeActiveWindow():
    type(Key.UP, KeyModifier.KEY_WIN)

def minimizeActiveWindow():
    type(Key.DOWN, KeyModifier.KEY_WIN)

def waitUntilReady():
    wait(TALS.icon_Refresh, 20)

# CTRL + SHIFT + DEL does not work in sikuli (known bug)
def clearBrowserCache():
    type(KeyModifier.SHIFT + KeyModifier.CTRL)
    type(Key.DELETE)
    sleep(1)
    type("d")
    type(Key.F4, KeyModifier.CTRL)

def switchToAddressBar():
    type(Key.F6)

def navigateTo(url):
    sleep(0.5)
    type(url)
    type(Key.ENTER)
    sleep(0.5)
    waitUntilReady()

def runBrowserToUrl(browser, url):
    openApp(browser)
    navigateTo(url)
    maximizeActiveWindow()

def openApp(appName):
    app = App(appName)
    if not app.window():
        App.open(defaulBrowserPath)
        wait(2)
    app.focus()
    wait(1)

def closeApp():
    type(Key.F4, KeyModifier.ALT)

def enterUserCredentials(username, password):
    wait(TALS.input_UsernameOrEmail, 10)
    click(TALS.input_UsernameOrEmail)
    type(username)
    wait(TALS.input_Password, 10)
    click(TALS.input_Password)
    type(password)
    wait(TALS.input_Submit, 10)
    click(TALS.input_Submit)
    waitUntilReady()

def pageDownToVisible(image):
    while True:
        if exists(image, 2):
            break
        type(Key.PAGE_DOWN)

def pageUpToVisible(image):
    while True:
        if exists(image, 2):
            break
        type(Key.PAGE_UP)

def changeInputData(image, text):
    wait(image, 10)
    doubleClick(image)
    type(Key.DELETE)
    type(text)

def submitChanges():
    type(Key.ENTER)