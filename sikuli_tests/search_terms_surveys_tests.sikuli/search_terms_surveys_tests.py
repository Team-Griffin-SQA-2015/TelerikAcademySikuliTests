import unittest
bdLibPath=os.path.abspath(sys.argv[0]+"..")
if not bdLibPath in sys.path: sys.path.append(bdLibPath)
from _lib import *
from _uimap import *

    
class SmokeTests(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass    


    def test_001_AddInvalidSearchTermWithEmptyWordShouldDisplayError(self):
        RunBrowserToUrl("chrome","http://stage.telerikacademy.com/Administration/SearchTerms")
        wait(SearchTerms.button_Add, 30)
        AddSearchTerm("","10")
        sleep(2)
        for i in range(1,2):
            type(Key.DOWN)

        assert exists(SearchTerms.word_ErrorMessageForRequired)

    def test_002_AddInvalidSearchTermWithHigherLengthWordShouldDisplayError(self):
        RunBrowserToUrl("chrome","http://stage.telerikacademy.com/Administration/SearchTerms")
        wait(SearchTerms.button_Add, 30)
        AddSearchTerm("dasdadsadasdasdsadsadsadsadsadsadsadsadsadasdsadasdasdadddddddddddddddddddssssssssssssssssssssssssssssss","10")
        sleep(2)
        for i in range(1,2):
            type(Key.DOWN)

        assert exists(SearchTerms.word_ErrorMessageForLength)

    def test_003_AddInvalidSearchTermWithEmptyCountShouldDisplayError(self):
        RunBrowserToUrl("chrome","http://stage.telerikacademy.com/Administration/SearchTerms")
        wait(SearchTerms.button_Add, 30)
        AddSearchTerm("NewTESTWORD",Key.BACKSPACE)
        sleep(2)
        for i in range(1,2):
            type(Key.DOWN)

        assert exists(SearchTerms.count_ErrorMessage)

    def test_004_AddValidSearchTermShouldSucceed(self):
        RunBrowserToUrl("chrome","http://stage.telerikacademy.com/Administration/SearchTerms")
        wait(SearchTerms.button_Add, 30)
        AddSearchTerm("NewSearchTerm","10")
        sleep(2)
        for i in range(1,2):
            type(Key.DOWN)

        assert exists(SearchTerms.gridRowWithCorrectResult)

    def test_005_DeleteSearchTermShouldSuceed(self):
        DeleteSearchTerm()
        assert not exists(SearchTerms.gridRowWithCorrectResult)

    def test_006_ExportToPDFShouldSucceed(self):
        ExportSearchTermToPDF()
        OpenPDFFile()
        wait(SearchTerms.checker_PDF,30)

    def test_007_AddValidSurveyShouldSucceed(self):
        RunBrowserToUrl("chrome","http://stage.telerikacademy.com/Administration/Surveys/Index")
        wait(SearchTerms.button_Add, 30)
        AddSurvey("NewSurvey")
        assert exists(Surveys.survey_Result)

    def test_008_AddValidQuestionShouldSucceed(self):
        ExpandSurvey()
        AddQuestion("New Question")
        assert exists(Surveys.question_Result)

    def test_009AddInvalidQuestionWithEmptyTextShouldDisplayError(self):
        RunBrowserToUrl("chrome","http://stage.telerikacademy.com/Administration/Surveys/Index")
        wait(SearchTerms.button_Add, 30)
        AddSurvey("NewSurvey")
        ExpandSurvey()
        AddQuestion(Surveys.option_TextType,"")
        sleep(1)
        assert exists(Surveys.question_TextErrorMessage)

    def test_010AddInvalidQuestionWithEmptyTypeShouldDisplayError(self):
        RunBrowserToUrl("chrome","http://stage.telerikacademy.com/Administration/Surveys/Index")
        wait(SearchTerms.button_Add, 30)
        AddSurvey("NewSurvey")
        ExpandSurvey()
        AddQuestion(Surveys.label_QuestionType,"new question")
        sleep(1)
        assert exists(Surveys.question_TypeErrorMessage)





if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SmokeTests)

    outfile = open("report.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='SmokeTests Report' )
    runner.run(suite)
    outfile.close()

