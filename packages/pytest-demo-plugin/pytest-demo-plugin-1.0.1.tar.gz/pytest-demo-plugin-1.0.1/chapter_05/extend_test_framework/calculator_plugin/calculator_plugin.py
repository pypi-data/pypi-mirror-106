def pytest_generate_tests(metafunc):
    metafunc.parametrize(('num_01', 'num_02', 'expected'), [
        (1, 2, 3),
        (1, 3, 4)
    ])
