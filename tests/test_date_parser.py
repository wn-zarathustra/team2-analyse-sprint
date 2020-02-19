import team_two_analyse.analysesprint as ansp

def test_multiple_for_date_parser():
    assert ansp.date_parser(ansp.dates[:3]) == ['2019-11-29', '2019-11-29', '2019-11-29']

    assert ansp.date_parser(ansp.dates[-3:]) == ['2019-11-20','2019-11-20', '2019-11-20']

    assert ansp.date_parser(['2019-11-29 12:50:54',
                        '2019-11-29 12:46:53',
                        '2019-11-29 12:46:10']) == ['2019-11-29', '2019-11-29', '2019-11-29']