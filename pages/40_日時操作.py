import streamlit as st

from datetime import datetime

WAREKI_START = {
   '令和': datetime(2019, 5, 1),
   '平成': datetime(1989, 1, 8),
   '昭和': datetime(1926, 12, 25)
}

def convert_to_wareki(y, m, d):
    """西暦の年月日を和暦の年に変換する."""
    try:
        y_m_d = datetime(y, m, d)
        if WAREKI_START['令和'] <= y_m_d:
            reiwa_year = WAREKI_START['令和'].year
            era_year = y_m_d.year
            year = (era_year - reiwa_year) + 1
            era_str = '令和'
        elif WAREKI_START['平成'] <= y_m_d:
            reiwa_year = WAREKI_START['平成'].year
            era_year = y_m_d.year
            year = (era_year - reiwa_year) + 1
            era_str = '平成'
        elif WAREKI_START['昭和'] <= y_m_d:
            reiwa_year = WAREKI_START['昭和'].year
            era_year = y_m_d.year
            year = (era_year - reiwa_year) + 1
            era_str = '昭和'
        else:
            return '昭和以前'

        if year == 1:
            year = '元'
       
        return era_str + str(year) + '年'
    except ValueError as e:
        raise e

print('西暦2020年4月1日は、', convert_to_wareki(2020, 4, 1), sep='')
print('西暦2019年5月1日は、', convert_to_wareki(2019, 5, 1), sep='')
print('西暦2019年4月30日は、', convert_to_wareki(2019, 4, 30), sep='')
print('西暦1989年1月8日は、', convert_to_wareki(1989, 1, 8), sep='')
print('西暦1989年1月7日は、', convert_to_wareki(1989, 1, 7), sep='')
print('西暦1974年5月5日は、', convert_to_wareki(1974, 5, 5), sep='')
print('西暦1926年12月25日は、', convert_to_wareki(1926, 12, 25), sep='')
print('西暦1926年12月24日は、', convert_to_wareki(1926, 12, 24), sep='')