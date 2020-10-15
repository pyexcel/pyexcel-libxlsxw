isort $(find pyexcel_libxlsxw -name "*.py"|xargs echo) $(find tests -name "*.py"|xargs echo)
black -l 79 pyexcel_libxlsxw
black -l 79 tests
