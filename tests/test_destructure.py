from lib.utils.destructure import destructure

def test_destructure():
    mockDict = {
        'a': 1,
        'b': 2,
        'c': 3
    }
    a, b, c = destructure(mockDict)('a', 'b', 'c')
    assert a == 1
    assert b == 2
    assert c == 3
