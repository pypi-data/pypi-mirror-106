import unittest
from os.path import join 
from os import getcwd, remove
from foxTemplateEngine import FoxEngine


class EngineTest(unittest.TestCase):

    def test_loops(self):
        current_dir = getcwd()
        for_test_path = join(current_dir, 'tests', 'input', 'test_loops')
        output_path = join(current_dir, 'tests', 'output', 'test_loops')
        obj = FoxEngine(for_test_path)
        with open(output_path) as res_file:
            res_text = res_file.read()
        self.assertEqual(obj.getRenderedTemplateAsText(), res_text)


    def test_variable(self):
        current_dir = getcwd()
        for_test_path = join(current_dir, 'tests', 'input', 'test_variable')
        output_path = join(current_dir, 'tests', 'output', 'test_variable')
        obj = FoxEngine(for_test_path, {
            'test_var': 'Hello, World!'
        })
        with open(output_path) as res_file:
            res_text = res_file.read()
        self.assertEqual(obj.getRenderedTemplateAsText(), res_text)


    def test_all(self):
        current_dir = getcwd()
        for_test_path = join(current_dir, 'tests', 'input', 'test_all')
        output_path = join(current_dir, 'tests', 'output', 'test_all')
        obj = FoxEngine(for_test_path, {
            'var': 'Hello, World!'
        })
        with open(output_path) as res_file:
            res_text = res_file.read()
        self.assertEqual(obj.getRenderedTemplateAsText(), res_text)


if __name__ == '__main__':
    unittest.main()