import pyexcel

from nose.tools import eq_


class TestStringIO:
    def test_xls_output_stringio(self):
        data = [[1, 2, 3], [4, 5, 6]]
        io = pyexcel.save_as(
            dest_file_type="xlsx", array=data, library="pyexcel-libxlsxw"
        )
        r = pyexcel.get_sheet(file_type="xlsx", file_content=io.getvalue())
        result = [1, 2, 3, 4, 5, 6]
        actual = list(r.enumerate())
        eq_(result, actual)
