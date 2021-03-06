import os
import unittest
import tempfile

from yaz.loader import load


class TestLoader(unittest.TestCase):
    def test_loader(self):
        """Should load a module from a given directory"""
        with tempfile.TemporaryDirectory() as dir:
            os.mkdir(os.path.join(dir, "loader"))
            with open(os.path.join(dir, "loader", "__init__.py"), "w") as file:
                file.write("loader_completed = \"Done\"")

            module = load(dir, "loader")
            self.assertEqual("Done", module.loader_completed)

    def test_unavailable_directory(self):
        """Should not load a module which is not available"""
        module = load("./unavailable_test_directory", "unavailable_test_module_name")
        self.assertIsNone(module)