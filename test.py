import FinanceDataReader as fdr

finstate = fdr.SnapDataReader('NAVER/FINSTATE/005930')
finstate

profit = finstate[['매출액', '영업이익', '당기순이익']]
profit

fdr.chart.plot(profit, kind='bar')

ratio = finstate[['ROE(%)', 'ROA(%)', 'EPS(원)', 'PER(배)']]
ratio

fdr.chart.plot(ratio, secondary_y='EPS(원)')

fdr.SnapDataReader('NAVER/FINSTATE/005930') # 기본값: '0'=주재무제표,'Y'=년
fdr.SnapDataReader('NAVER/FINSTATE-Q/005930') # '0'=주재무제표(기본), 'Q'=분기
fdr.SnapDataReader('NAVER/FINSTATE-3Q/005930') # '3'=K-IFRS별도, 'Q'=분기
fdr.SnapDataReader('NAVER/FINSTATE-T/005930') # '0'=주재무제표(기본), 'A'=연간+분기


fdr.SnapDataReader('NAVER/FINSTATE/005930') # 연간 주재무제표

fdr.SnapDataReader('NAVER/FINSTATE-Y/005930') # 연간 주재무(='NAVER/FINSTATE-2Y/005930')
fdr.SnapDataReader('NAVER/FINSTATE-1Y/005930') # 연간 K-IFRS 별도
fdr.SnapDataReader('NAVER/FINSTATE-2Y/005930') # 연간 K-IFRS 연결
fdr.SnapDataReader('NAVER/FINSTATE-3Y/005930') # 연간 K-GAAP 개별
fdr.SnapDataReader('NAVER/FINSTATE-4Y/005930') # 연간 K-GAAP 연결

fdr.SnapDataReader('NAVER/FINSTATE-Q/005930') # 분기 주재무(='NAVER/FINSTATE-2Q/005930')
fdr.SnapDataReader('NAVER/FINSTATE-1Q/005930') # K-IFRS 별도
fdr.SnapDataReader('NAVER/FINSTATE-2Q/005930') # K-IFRS 연결
fdr.SnapDataReader('NAVER/FINSTATE-3Q/005930') # K-GAAP 개별
fdr.SnapDataReader('NAVER/FINSTATE-4Q/005930') # K-GAAP 연결


# SK하이닉스(000660)
fdr.SnapDataReader('NAVER/FINSTATE/000660').to_csv()

# 카카오(035720)
fdr.SnapDataReader('NAVER/FINSTATE/035720').to_csv()
