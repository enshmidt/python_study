# Using functional approach, generators, currying,
# implement functions that writes IP list of redirected requests (code 304) into another file
# separate pure_func from functions that change state (io_func)
# write negative test "test_myfunc_negative"
# Set pytest as default runner https://stackoverflow.com/questions/6397063/how-do-i-configure-pycharm-to-run-py-test-tests
# hit Ctrl+Shift+F10 or RMB on the file to run tests


def io_func(logfile_path, result_file_path):
    lines = (line for line in open(logfile_path))
    [open(result_file_path, "a+").write(pure_func(line) + "\n") for line in lines if int(line.split(" ")[8]) == 304]
    return result_file_path


def pure_func(file_line):
    return file_line.split(" ")[0]


res_file_path = io_func("apache_log", "out_file")


def test_myfunc_positive():
    line = '218.30.103.62 - - [17/May/2015:11:05:17 +0000] "GET /projects/xdotool/xdotool.xhtml \
    HTTP/1.1" 304 - "-" "Sogou web spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)"'
    assert pure_func(line) == "218.30.103.62"


def test_myfunc_negative():
    line = '218.30.103.62 - - [17/May/2015:11:05:37 +0000] "GET /blog/geekery/c-vs-python-bdb.html HTTP/1.1" \
           200 11388 "-" "Sogou web spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)"'
    assert line.split(" ")[0] not in open("out_file")
