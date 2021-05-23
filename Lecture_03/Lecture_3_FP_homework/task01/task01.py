# Using functional approach, generators, currying,
# implement functions that writes IP list of redirected requests (code 304) into another file
# separate pure_func from functions that change state (io_func)
# write negative test "test_myfunc_negative"
# Set pytest as default runner https://stackoverflow.com/questions/6397063/how-do-i-configure-pycharm-to-run-py-test-tests
# hit Ctrl+Shift+F10 or RMB on the file to run tests


def io_func(logfile_path, result_file_path):
    with open(logfile_path, 'r') as logfile, open(result_file_path, 'a+') as result:
        lines = (line for line in logfile)
        for line in lines:
            if pure_func(line) != " ":
                result.write(pure_func(line) + "\n")
    return result_file_path


def pure_func(file_line):
    list_file_line = file_line.split(" ")
    return list_file_line[0] if list_file_line[8] == "304" else " "


res_file_path = io_func("apache_log", "out_file")


def test_myfunc_positive():
    line = '218.30.103.62 - - [17/May/2015:11:05:17 +0000] "GET /projects/xdotool/xdotool.xhtml HTTP/1.1" 304 - "-" ' \
           '"Sogou web spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)" '
    assert pure_func(line) == "218.30.103.62"


def test_myfunc_negative():
    line = '218.30.103.62 - - [17/May/2015:11:05:37 +0000] "GET /blog/geekery/c-vs-python-bdb.html HTTP/1.1" 200 ' \
           '11388 "-" "Sogou web spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)" '
    assert pure_func(line) == " "
