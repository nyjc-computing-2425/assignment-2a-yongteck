import subprocess
import unittest

from autograding import TestInputOutput, TestFunction
from autograding.case import InOut, FuncCall


class TestSF(TestInputOutput):
    def setUp(self):
        self.testcases = [
            InOut(input="2.345", output="The number 2.345 has 4 significant figures."),
            InOut(input="02.345", output="The number 02.345 has 4 significant figures."),
            InOut(input="0.0023", output="The number 0.0023 has 2 significant figures."),
            InOut(input="2.3400", output="The number 2.3400 has 5 significant figures."),
            InOut(input="0.002300", output="The number 2.345 has 4 significant figures."),
        ]


if __name__ == '__main__':
    import os
    if not os.listdir("autograding"):
        import subprocess
        subprocess.run(["git", "submodule", "update", "--init"])
    unittest.main()
