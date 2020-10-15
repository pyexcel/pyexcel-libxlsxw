"""
    pyexcel_libxlsxw
    ~~~~~~~~~~~~~~~~~~~

    The lower level xlsx file format writer using libxlsxwpy

    :copyright: (c) 2016-2020 by Onni Software Ltd & its contributors
    :license: New BSD License
"""
from libxlsxwpy import Book
from pyexcel_io.plugin_api import IWriter, ISheetWriter


class XLSXSheetWriter(ISheetWriter):
    """
    xlsx sheet writer
    """

    def __init__(self, xlsx_sheet):
        self.xlsx_sheet = xlsx_sheet
        self.current_row = 0

    def write_row(self, array):
        """
        write a row into the file
        """
        for index, cell in enumerate(array):
            if isinstance(cell, (int, float)):
                self.xlsx_sheet.write_number(self.current_row, index, cell)
            elif isinstance(cell, bool):
                self.xlsx_sheet.write_boolean(self.current_row, index, cell)
            else:
                self.xlsx_sheet.write_string(
                    self.current_row, index, str(cell)
                )

        self.current_row += 1

    def close(self):
        pass


class XLSXWriter(IWriter):
    """
    xlsx writer
    """

    def __init__(
        self,
        file_name,
        file_type,
        constant_memory=True,
        default_date_format="dd/mm/yy",
        **keywords
    ):
        """
        Open a file for writing

        Please note that this writer configure xlsxwriter's BookWriter to use
        constant_memory by default.

        :param keywords: **default_date_format** control the date time format.
                         **constant_memory** if true, reduces the memory
                         footprint when writing large files. Other parameters
                         can be found in `xlsxwriter's documentation
                         <http://xlsxwriter.readthedocs.io/workbook.html>`_
        """
        if "single_sheet_in_book" in keywords:
            keywords.pop("single_sheet_in_book")
        self.xlsx_book = Book()
        self.xlsx_book.open(file_name)

    def create_sheet(self, name):
        sheet = self.xlsx_book.add_worksheet(name)
        return XLSXSheetWriter(sheet)

    def close(self):
        """
        This call actually save the file
        """
        self.xlsx_book.close()
        self.xlsx_book = None
