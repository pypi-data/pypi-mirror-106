import sqlalchemy
import nure.sync.sql


class BigQuery(nure.sync.sql.Sql):
    def __init__(self, keyfile, suffix_func, arraysize=10_000, root_path='data/bigquery', ttl=None) -> None:
        super(BigQuery, self).__init__(suffix_func, root_path, ttl)

        self._engine = sqlalchemy.create_engine('bigquery://', credentials_path=keyfile, arraysize=arraysize)

    @property
    def engine(self) -> sqlalchemy.engine.Engine:
        return self._engine


if __name__ == '__main__':
    from datetime import datetime, timedelta

    from nure.sync.suffix import DailyActionLogSuffix
    country = 'my'
    date = (datetime.now() - timedelta(days=1)).strftime('%Y%m%d')
    bq = BigQuery('credentials/bigquery/zhk-ga-bigq.json', suffix_func=DailyActionLogSuffix('my'), ttl=10_800)
    fn = bq.require('sql/interaction.sql', re_replace={
        R'\$\(dataset_id\)': '94907906',
        R'\$\(date\)': date
    })
    print(fn)
