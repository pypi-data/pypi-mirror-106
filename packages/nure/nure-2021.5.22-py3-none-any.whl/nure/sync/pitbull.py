import json

import sqlalchemy
import nure.sync.sql


class Pitbull(nure.sync.sql.Sql):
    def __init__(self, secret_fn, suffix_func, root_path='data/pitbull', ttl=None) -> None:
        super(Pitbull, self).__init__(suffix_func, root_path, ttl)
        with open(secret_fn, 'rt') as fd:
            secret = json.load(fd)

        user = secret['user']
        password = secret['password']
        host = secret['host']
        port = secret['port']
        dbname = secret['dbname']

        self._engine = sqlalchemy.create_engine(
            f'postgresql://{user}:{password}@{host}:{port}/{dbname}')

    @property
    def engine(self) -> sqlalchemy.engine.Engine:
        return self._engine


if __name__ == '__main__':
    from nure.sync.suffix import VentureCodeSuffix
    venture_code = 'my'
    pitbull = Pitbull('credentials/pitbull.json', suffix_func=VentureCodeSuffix(venture_code), ttl=10_800)
    fn = pitbull.require('sql/catalogue.sql', sa_replace={'venture_code': venture_code})
    print(fn)
