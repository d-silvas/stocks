from db.crud import session_scope, recreate_database
from db.models import IncomeStatement, Ticker
from yahooquery import Ticker as YqTicker
import numpy as np

if __name__ == '__main__':
    recreate_database()

    ul = YqTicker('ul')
    # print(ul.income_statement().columns)
    print(ul.summary_detail)
    print(ul.summary_profile)

    with session_scope() as s:
        s.add(Ticker(ticker='ul'))
        for index, row in ul.income_statement().replace([np.nan], [None]).iterrows():
            new_is = IncomeStatement(
                ticker_id=s.query(Ticker).filter(Ticker.ticker == 'ul').first().id,
                as_of_date=row['asOfDate'],
                period_type=row['periodType'],
                basic_average_shares=row['BasicAverageShares'],
                basic_eps=row['BasicEPS'],
                cost_of_revenue=row['CostOfRevenue'],
                ebit=row['EBIT'],
                ebitda=row['EBITDA'],
            )
            s.add(new_is)

        s.commit()
