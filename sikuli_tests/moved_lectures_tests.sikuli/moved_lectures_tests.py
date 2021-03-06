from _lib import *
import unittest
import time

bdLibPath = os.path.abspath(sys.argv[0]+"..")
if not bdLibPath in sys.path:
    sys.path.append(bdLibPath)

class MovedLecturesTests(unittest.TestCase):

    def setUp(self):
        runBrowserToUrl("chrome", "http://stage.telerikacademy.com/")
        if exists(MainPage.enterButton):
            adminLogin("griffin", "Start123")
            navigateToMovedLectures()
        else:
            navigateToMovedLectures()
        if exists(MovedLectures.removeItem):
            clearGrid()

    def tearDown(self):
        pass

    def test_001_AddLectureWithoutCourseAddsLectureForAllCourses(self):
        click(MovedLectures.addNewItem)
        wait(MovedLectures.popUpTitle)
        click(MovedLectures.updateButton)
        assert exists(MovedLectures.validForAllCOursesText)

    def test_002_AddLectureWithOutTrainingRoomLeavesTheFieldBlank(self):
        click(MovedLectures.addNewItem)
        wait(MovedLectures.popUpTitle)
        click(MovedLectures.updateButton)
        assert exists(MovedLectures.validForAllTrainingRooms)

    def test_003_AddLectureWithValidDetailsCreatesNewEntry(self):
        click(MovedLectures.addNewItem)
        fillInLectureFullDetails()
        click(MovedLectures.refreshGrid)
        assert exists(MovedLectures.validEntry)

    def test_004_AddLectureWithEndDateBeforeCurrentDate(self):
        click(MovedLectures.addNewItem)
        wait(MovedLectures.popUpTitle)
        click(MovedLectures.startDate)
        type("a", KeyModifier.CTRL)
        type("01/01/2016 01:00:00")
        type(Key.TAB)
        type("12/24/2015 02:00:00")
        click(MovedLectures.updateButton)
        assert exists(MovedLectures.startDateValidationError)

    def test_005_AddLectureWithSameDetailsMoreThanOnceDisplaysError(self):
        click(MovedLectures.addNewItem)
        fillInLectureFullDetails()
        click(MovedLectures.refreshGrid)
        click(MovedLectures.addNewItem)
        fillInLectureFullDetails()
        assert exists(MovedLectures.startDateValidationError)

    def test_006_DeleteButtonRemovesTheRespectiveEntryFromTheList(self):
        click(MovedLectures.addNewItem)
        wait(MovedLectures.popUpTitle)
        click(MovedLectures.updateButton)
        wait(MovedLectures.validForAllCOursesText)
        click(MovedLectures.removeItem)
        wait(MovedLectures.deletePopUp)
        click(MovedLectures.deletePopUp)
        assert exists(MovedLectures.emptyGrid)

    def test_007_UpdateEntryWithValidDetailsChangesTheCurrentDetails(self):
        click(MovedLectures.addNewItem)
        click(MovedLectures.addNewItem)
        wait(MovedLectures.popUpTitle)
        click(MovedLectures.updateButton)
        click(MovedLectures.editItem)
        fillInLectureFullDetails()
        click(MovedLectures.refreshGrid)
        assert exists(MovedLectures.validEntry)

    def test_008_UpdateWithInvalidDetailsDoesntChangesTheCurrentDetails(self):
        click(MovedLectures.addNewItem)
        wait(MovedLectures.popUpTitle)
        click(MovedLectures.updateButton)
        click(MovedLectures.editItem)
        fillInLectureFullInvalidDetails()
        wait(MovedLectures.startDateValidationError)
        click(MovedLectures.cancelButton)
        click(MovedLectures.refreshGrid)
        assert exists(MovedLectures.validForAllCOursesText)

    def test_009_UpdateWithInvalidDetailsDoesntChangeTheCurrentDetails(self):
        click(MovedLectures.addNewItem)
        wait(MovedLectures.popUpTitle)
        click(MovedLectures.updateButton)
        click(MovedLectures.addNewItem)
        fillInLectureFullDetails()
        click(MovedLectures.refreshGrid)
        click(MovedLectures.coursesFilterDropdown)
        click(MovedLectures.courseFilterDropDownAllCourses)
        assert exists(MovedLectures.allCoursesList)
        click(MovedLectures.coursesFilterDropdownAllSelectedManualEntry)
        type("a", KeyModifier.CTRL)
        type("Archer QA"+Key.TAB)
        assert exists(MovedLectures.validEntry)

    def test_010_ExportPDFCreatedPDFFileWithTheContentsOfTheGrid(self):
        currentTime = time.strftime("%H%M%S")
        path = "D:\\testexport{0}.pdf".format(currentTime)
        click(MovedLectures.addNewItem)
        wait(MovedLectures.popUpTitle)
        fillInLectureFullDetails()
        click(MovedLectures.refreshGrid)
        click(MovedLectures.exportToPDF)
        wait(MovedLectures.exportPopUp)
        type(path+Key.ENTER)
        type("d", KEY_WIN)
        sleep(1)
        type("r", KEY_WIN)
        sleep(1)
        type(path)
        sleep(0.5)
        type(Key.ENTER)
        sleep(1)
        type(Key.NUM1, KeyModifier.CTRL)
        assert exists(MovedLectures.exportedValidEntry)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MovedLecturesTests)
    outfile = open("moved_lectures_tests_report.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='Moved Lectures Report')
    runner.run(suite)
    outfile.close()
