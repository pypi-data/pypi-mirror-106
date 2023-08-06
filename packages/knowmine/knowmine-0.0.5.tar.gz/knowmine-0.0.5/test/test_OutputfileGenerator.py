
"""
Unit tests for the knowmine.OutputfileGenerator module.

"""

import knowmine.OutputfileGenerator as of
import os


folder = os.getcwd() + "/"
filename = "Test_file"
result = [filename, "Test sentence is produced", 1, 1]
result_output = of.Output(folder, result)


def test_add_result_to_file():

    result_output.add_result_to_database()
    result_output.add_result_to_excel()

    for file in os.listdir(folder):
        filename = os.fsdecode(file)
        if filename.endswith(('.db')):
            result_file_db = 1
        if filename.endswith(('.xlsx')):
            result_file_xlsx = 1

    assert result_file_db == 1
    assert result_file_xlsx == 1
