def func(x1, x2, y1=0, y2=0, *args, kw1, kw2=None, **kwargs):
    print('x1 =', x1, '(type=%s)' % type(x1).__name__)
    print('x1 =', x2, '(type=%s)' % type(x2).__name__)
    print('y1 =', y1, '(type=%s)' % type(y1).__name__)
    print('y1 =', y2, '(type=%s)' % type(y2).__name__)
    print('args =', str(args), '(type=%s)' % type(args).__name__)
    print('kw1 =', kw1, '(type=%s)' % type(kw1).__name__)
    print('kw2 =', kw2, '(type=%s)' % type(kw2).__name__)
    print('kwargs =', str(kwargs), '(type=%s)' % type(kwargs).__name__)
    print()


my_args = [1, 2, 3, 4, 5, 6]
my_kwargs = {'kw1': 'key1', 'kw2': 'key2', 'kw3': 'key3'}
func(1, *my_args, 2, **my_kwargs)
