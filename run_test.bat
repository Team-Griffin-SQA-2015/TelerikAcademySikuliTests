set TestRunner="sikulix\runsikulix.cmd"
set TestList="sikuli_tests\%1.sikuli"

call %TestRunner% -r %TestList%