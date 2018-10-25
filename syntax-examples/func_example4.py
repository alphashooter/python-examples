def func(x1, x2, y1=0, y2=0, *args):
    print('x1 =', x1, '(type=%s)' % type(x1).__name__)
    print('x1 =', x2, '(type=%s)' % type(x2).__name__)
    print('y1 =', y1, '(type=%s)' % type(y1).__name__)
    print('y1 =', y2, '(type=%s)' % type(y2).__name__)
    print('args =', str(args), '(type=%s)' % type(args).__name__)
    print()


func(1, 2)
func(1, 2, 3, 4)
func(1, 2, 3, 4, 5, 6)
