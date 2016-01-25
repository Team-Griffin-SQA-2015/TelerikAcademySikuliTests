from sikuli import *
from _uimap import *
import HTMLTestRunner
import math
import os

bdLibPath = os.path.abspath(sys.argv[0] + "..")
if not bdLibPath in sys.path:
    sys.path.append(bdLibPath)

################################################################################
################################ Nikola Nenov ##################################
################################################################################

def runBrowserToUrl(browser, toUrl):
    # TestAction("Start " +browser +" "+toUrl)
    sleep(0.5)
    type("d", KEY_WIN)
    sleep(1)
    type("r", KEY_WIN)
    sleep(1)
    type(browser+" ")
    sleep(1)
    type(toUrl)
    sleep(1)
    type(Key.ENTER)

def startApp(appName):
    sleep(1)
    type("d", KEY_WIN)
    sleep(1)
    type("r", KEY_WIN)
    sleep(1)
    type(appName)
    sleep(1)
    type(Key.ENTER)

def adminLogin(username, password):
    click(MainPage.enterButton)
    wait(LoginPage.username)
    click(LoginPage.username)
    type(username)
    type(Key.TAB)
    type(password)
    click(LoginPage.submitButton)

def navigateToMovedLectures():
    wait(MainPage.adminMenu)
    click(MainPage.adminMenu)
    wait(MainPage.adminMovedLectures)
    click(MainPage.adminMovedLectures)

def clearGrid():
    wait(MovedLectures.removeItem)
    while exists(MovedLectures.removeItem, 10):
        click(MovedLectures.removeItem)
        wait(MovedLectures.deletePopUp)
        click(MovedLectures.deletePopUp)

def fillInLectureFullDetails():
    wait(MovedLectures.popUpTitle)
    click(MovedLectures.courseDropDown)
    click(MovedLectures.courseDropDownOption)
    click(MovedLectures.startDate)
    type("a", KeyModifier.CTRL)
    type("01/01/2016 01:00:00")
    type(Key.TAB)
    type("01/01/2016 02:00:00")
    type(Key.TAB)
    type("Light")
    click(MovedLectures.updateButton)

def fillInLectureFullInvalidDetails():
    wait(MovedLectures.popUpTitle)
    click(MovedLectures.courseDropDown)
    click(MovedLectures.courseDropDownOption)
    click(MovedLectures.startDate)
    type("a", KeyModifier.CTRL)
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

################################################################################
############################## Nikola Bogomirov ################################
################################################################################

def AddSearchTerm(word,count):
    click(SearchTerms.button_Add)
    sleep(2)
    click(SearchTerms.label_Word)
    type(word)
    sleep(2)
    click(SearchTerms.input_Count)
    type(count)
    sleep(2)
    click(SearchTerms.button_Update)

def DeleteSearchTerm():
    reg = find(SearchTerms.gridRowWithCorrectResult).right(200)
    click(reg.find(SearchTerms.button_Delete))
    sleep(2)
    type(Key.ENTER)

def ExportSearchTermToPDF():
    click(SearchTerms.button_ExportToPDF)
    wait(SearchTerms.bar_SaveFileType,30)
    type("export")
    type(Key.ENTER)
    sleep(2)

def OpenPDFFile():
    RunBrowserToUrl("chrome","C:\Users\Niki\Desktop\export.pdf")
    sleep(2)

def AddSurvey(name):
    click(SearchTerms.button_Add)
    sleep(2)
    click(Surveys.label_SurveyName)
    type(name)
    sleep(2)
    click(Surveys.label_ActiveFrom)
    type("23/01/2016 00:00:00")
    sleep(2)
    click(Surveys.label_ActiveTo)
    type("25/01/2016 00:00:00")
    click(Surveys.label_SurveyName)
    sleep(2)
    click(SearchTerms.button_Update)

def ExpandSurvey():
    sleep(1)
    reg=find(Surveys.survey_Result).left(100)
    click(reg.find(Surveys.button_Expand))
    sleep(1)

def AddQuestion(questionType,question):
    ScrollDown(13)
    click(SearchTerms.button_Add)
    wait(Surveys.label_QuestionType)
    click(Surveys.label_QuestionType)
    click(questionType)
    click(Surveys.label_QuestionText)
    type(question)
    for checkbox in findAll(Surveys.image_CheckBox):
        click(checkbox)
    sleep(1)
    ScrollDown(3)
    sleep(2)
    click(SearchTerms.button_Update)

def ScrollDown(times):
    for i in range(1, times):
            type(Key.DOWN)