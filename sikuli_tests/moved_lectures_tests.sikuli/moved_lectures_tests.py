import unittest
import time
bdLibPath=os.path.abspath(sys.argv[0]+"..")
if not bdLibPath in sys.path: sys.path.append(bdLibPath)
from _lib import *

    
class MovedLecturesTests(unittest.TestCase):
    
    def setUp(self):
        RunBrowserToUrl("chrome","http://stage.telerikacademy.com/")
        if exists(MainPage.enterButton):
            AdminLogin("griffin","Start123")
            NavigateToMovedLectures()
        else:
           NavigateToMovedLectures()
        if exists(MovedLectures.removeItem):
            ClearGrid()
    
    def tearDown(self):
        pass    
    
    # def test_001_AddLectureWithoutCourseAddsLectureForAllCourses(self):
    #     click(MovedLectures.addNewItem)
    #     wait(MovedLectures.popUpTitle)
    #     click(MovedLectures.updateButton)
    #     assert exists(MovedLectures.validForAllCOursesText)
    #
    # def test_002_AddLectureWithOutTrainingRoomLeavesTrainingRoomFieldBlank(self):
    #     click(MovedLectures.addNewItem)
    #     wait(MovedLectures.popUpTitle)
    #     click(MovedLectures.updateButton)
    #     assert exists(MovedLectures.validForAllTrainingRooms)
    #
    # def test_003_AddLectureWithValidDetailsCreatesNewEntry(self):
    #     click(MovedLectures.addNewItem)
    #     FillInLectureFullDetails()
    #     click(MovedLectures.refreshGrid)
    #     assert exists(MovedLectures.validEntry)
    #
    # def test_004_AddLectureWithEndDateBeforeCurrentDate(self):
    #     click(MovedLectures.addNewItem)
    #     wait(MovedLectures.popUpTitle)
    #     click(MovedLectures.startDate)
    #     type("a",KeyModifier.CTRL)
    #     type("01/01/2016 01:00:00")
    #     type(Key.TAB)
    #     type("12/24/2015 02:00:00")
    #     click(MovedLectures.updateButton)
    #     assert exists(MovedLectures.startDateValidationError)
    #
    # def test_005_AddLectureWithSameDetailsMoreThanOnceDisplaysError(self):
    #     click(MovedLectures.addNewItem)
    #     FillInLectureFullDetails()
    #     click(MovedLectures.refreshGrid)
    #     FillInLectureFullDetails()
    #     assert exists(MovedLectures.startDateValidationError)

    # def test_006_DeleteButtonRemovesTheRespectiveEntryFromTheList(self):
    #     click(MovedLectures.addNewItem)
    #     wait(MovedLectures.popUpTitle)
    #     click(MovedLectures.updateButton)
    #     wait(MovedLectures.validForAllCOursesText)
    #     click(MovedLectures.removeItem)
    #     wait(MovedLectures.deletePopUp)
    #     click(MovedLectures.deletePopUp)
    #     assert exists(MovedLectures.emptyGrid)

    # def test_007_VerifyThatUpdatingAnEntryWithValidDetailsChangesTheCurrentDetails(self):
    #     click(MovedLectures.addNewItem)
    #     click(MovedLectures.addNewItem)
    #     wait(MovedLectures.popUpTitle)
    #     click(MovedLectures.updateButton)
    #     click(MovedLectures.editItem)
    #     FillInLectureFullDetails()
    #     click(MovedLectures.refreshGrid)
    #     assert exists(MovedLectures.validEntry)

    # def test_008_VerifyThatUpdatingAnEntryWithInvalidDetailsDoesntChangesTheCurrentDetails(self):
    #     click(MovedLectures.addNewItem)
    #     wait(MovedLectures.popUpTitle)
    #     click(MovedLectures.updateButton)
    #     click(MovedLectures.editItem)
    #     FillInLectureFullInvalidDetails()
    #     wait(MovedLectures.startDateValidationError)
    #     click(MovedLectures.cancelButton)
    #     click(MovedLectures.refreshGrid)
    #     assert exists(MovedLectures.validForAllCOursesText)

    def test_009_VerifyThatUpdatingAnEntryWithInvalidDetailsDoesntChangesTheCurrentDetails(self):
        click(MovedLectures.addNewItem)
        wait(MovedLectures.popUpTitle)
        click(MovedLectures.updateButton)
        click(MovedLectures.addNewItem)
        FillInLectureFullDetails()
        click(MovedLectures.refreshGrid)
        click(MovedLectures.coursesFilterDropdown)
        click(MovedLectures.courseFilterDropDownAllCourses)
        assert exists(MovedLectures.allCoursesList)
        click(MovedLectures.coursesFilterDropdownAllSelectedManualEntry)
        type("a",KeyModifier.CTRL)
        type("Archer QA"+Key.TAB)
        assert exists(MovedLectures.validEntry)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MovedLecturesTests)

    outfile = open("report.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='Moved Lectures Report' )
    runner.run(suite)
    outfile.close()

