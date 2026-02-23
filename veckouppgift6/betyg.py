def validate_grade(points):
    if 0 <= points < 41: return 'IG'
    elif 41 <= points < 71: return 'G'
    else: return 'VG'



def test_godkant():
    assert validate_grade(41) == 'G'
    assert validate_grade(3) == 'IG'
    assert validate_grade(99) == 'VG'

