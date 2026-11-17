"""Regression tests for the Windows launchers' Python fallback order."""
import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent


class WindowsLauncherTest(unittest.TestCase):
    def check_launcher(self, name, module):
        text = (ROOT / name).read_text(encoding="utf-8")
        steps = [
            ".venv\\Scripts\\python.exe",
            "where python3.12",
            "py -3.12 --version",
            "py -3 -c",
            "python -c",
            "python -m " + module,
        ]
        positions = []
        for step in steps:
            self.assertIn(step, text, f"{name}: launcher lacks '{step}' fallback")
            positions.append(text.index(step))
        self.assertEqual(positions, sorted(positions), f"{name}: fallback order is wrong")
        self.assertEqual(
            text.count("sys.exit(sys.version_info < (3, 10))"), 2,
            f"{name}: py -3 and python fallbacks must check for Python 3.10+",
        )

    def test_easyedit_cmd_falls_back_to_any_python(self):
        self.check_launcher("easyedit.cmd", "easyedit")

    def test_easyedit_web_cmd_falls_back_to_any_python(self):
        self.check_launcher("easyedit-web.cmd", "easyedit.web")


if __name__ == "__main__":
    unittest.main()
