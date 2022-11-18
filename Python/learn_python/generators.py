def remote_control():
    yield 'HBO'
    yield 'CNN'
    yield 'Discovery'
    yield 'BBC'


r = remote_control()
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
