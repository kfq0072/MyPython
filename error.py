# try:
#     print('try')
#     r = 100 / 5
#     print('result:', r)
# except ZeroDivisionError as e:
#     print('except:', e)
# finally:
#     print('finally')
# print('********END********')

# def foo(s):
#     return 10 / int(s)

# def bar(s):
#     return foo(s) * 2

# def main():
#     bar('0')

# main()

# import logging

# def foo(s):
#     return 10 / int(s)

# def bar(s):
#     return foo(s) * 2

# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)

# main()
# print('********END********')


def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()
