########################################################
# UI map for XYZ
########################################################
from sikuli import *
########################################################
class LoginPage:

    username = "username.png"

    password = "password.png"

    submitButton = "submitButton.png"

class MainPage:

    enterButton = Pattern("enterButton.png").targetOffset(-43,-2)

    adminMenu = Pattern("adminMenu.png").similar(0.87)

    telerikAcademyMenu = "telerikAcademyMenu.png"

    entryExamMenu = "entryExamMenu.png"

    adminMovedLectures = "adminMovedLectures.png"

class MovedLectures:

    addNewItem = "addNewItem.png"

    removeItem = "removeItem.png"

    editItem = "editItem.png"

    refreshGrid = Pattern("refreshGrid.png").targetOffset(29,2)

    popUpTitle = "1453407407372.png"

    courseDropDown = Pattern("courseDropDown.png").similar(0.80).targetOffset(-84,-3)

    startDate = Pattern("startDate.png").targetOffset(53,-6)

    endDate = Pattern("endDate.png").targetOffset(-91,-2)

    trainingRoomDropDown = Pattern("trainingRoomDropDown.png").targetOffset(-71,1)

    updateButton = Pattern("updateButton.png").similar(0.80)

    cancelButton = "cancelButton.png"

    validForAllCOursesText = "validForAllCOursesText.png"

    allCoursesList = "allCoursesList.png"

    courseDropDownOption = "courseDropDownOption.png"


    courseFilterDropDownAllCourses = "courseFilterDropDown.png"

    deletePopUp = Pattern("deletePopUp.png").targetOffset(-32,6)

    validForAllTrainingRooms = "validForAllTrainingRooms.png"

    startDateValidationError = "startDateValidationError.png"

    courseValidationError = "1453411922065.png"


    validEntry = Pattern("validEntry.png").similar(0.32)

    emptyGrid = "emptyGrid.png"

    coursesFilterDropdown = Pattern("coursesFilterDropdown.png").targetOffset(215,0)

    coursesFilterDropdownAllSelected = Pattern("coursesFilterDropdownAllSelected.png").targetOffset(217,2)

    coursesFilterDropdownAllSelectedManualEntry = "coursesFilterDropdownAllSelectedManualEntry.png"


    consoleWindow = "consoleWindow.png"


    exportToPDF = "exportToPDF.png"
    exportPopUp = "exportPopUp.png"
    exportedValidEntry = "exportedValidEntry.png"

class EntryExam:
    applicationForAcademyHeading = "applicationForAcademyHeading.png"

class TALS_LN:
    input_UsernameOrEmail = "input_UsernameOrEmail.png"
    input_Password = "input_Password.png"
    input_Submit = "input_Submit.png"
    icon_Refresh = Pattern("icon_Refresh.png").similar(0.80)
    label_FirstNameEn = Pattern("label_FirstNameEn.png").exact().targetOffset(200,0)
    label_LastNameEn = Pattern("label_LastNameEn.png").exact().targetOffset(200,0)
    message_InvalidMinLengthFirstName = Pattern("message_InvalidMinLengthFirstName.png").similar(0.80)
    message_InvalidMinLengthLastName = Pattern("message_InvalidMinLengthLastName.png").similar(0.80)
    message_InvalidMaxLengthFirstName = Pattern("message_InvalidMaxLengthFirstName.png").similar(0.80)
    message_InvalidMaxLengthLastName = Pattern("message_InvalidMaxLengthLastName.png").similar(0.80)
    message_Success = "message_Success.png"