pip install -q finance-datareader

finstate = fdr.SnapDataReader('NAVER/FINSTATE/005930')

import FinanceDataReader as fdr

finstate = fdr.SnapDataReader('NAVER/FINSTATE/005930')
finstate

finstate.columns

profit = finstate[['매출액', '영업이익', '당기순이익']]
profit

fdr.chart.plot(profit, kind='bar')

ratio = finstate[['ROE(%)', 'ROA(%)', 'EPS(원)', 'PER(배)']]
ratio

fdr.chart.plot(ratio, secondary_y='EPS(원)')

fdr.SnapDataReader('NAVER/FINSTATE/005930') # 년도별, 주재무제표
fdr.SnapDataReader('NAVER/FINSTATE-Q/005930') # 분기별, 주재무제표
fdr.SnapDataReader('NAVER/FINSTATE-Q3/005930') # 분기별, K-IFRS별도
fdr.SnapDataReader('NAVER/FINSTATE-A/005930') # 년도+분기, 주재무제표


# SK하이닉스(000660)
fdr.SnapDataReader('NAVER/FINSTATE/000660').to_csv()

# 카카오(035720)
fdr.SnapDataReader('NAVER/FINSTATE/035720').to_csv()
