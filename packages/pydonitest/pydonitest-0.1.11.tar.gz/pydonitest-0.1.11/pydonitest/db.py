import os
import logging
import pydonitest
import sqlalchemy


logger = pydonitest.logger_setup(__name__, pydonitest.module_loglevel)


class Postgres(object):
    """
    Interact with PostgreSQL database through Python.
    """
    def __init__(self, pg_user=None, pg_dbname=None):
        self.dbuser = pg_user
        self.dbname = pg_dbname
        self.dbcon = self.connect()

    def read_pgpass(self):
        """
        Read ~/.pgpass file if it exists and extract Postgres credentials. Return tuple
        in format: `hostname, port, pg_dbname, pg_user, pg_pass`
        """
        pgpass_file = os.path.expanduser('~/.pgpass')
        if os.path.isfile(pgpass_file):
            with open(pgpass_file, 'r') as f:
                pgpass_contents = f.read().split(':')

            # Ensure proper ~/.pgpass format, should be a tuple of length 5
            assert len(pgpass_contents) == 5, \
                'Invalid ~/.pgpass contents format. Should be `hostname:port:pg_dbname:pg_user:pg_pass`'

            return pgpass_contents

    def connect(self):
        """
        Connect to Postgres database and return the database connection.
        """
        if self.dbuser is None and self.dbname is None:
            # Attempt to parse ~/.pgpass file
            logger.warn('No credentials supplied, attempting to parse ~/.pgpass file')
            pgpass_contents = self.read_pgpass()
            if pgpass_contents is not None:
                hostname, port, pg_dbname, pg_user, pg_pass = pgpass_contents

                if pg_dbname > '' and pg_user > '':
                    self.dbuser = pg_user
                    self.dbname = pg_dbname
            else:
                raise Exception(pydonitest.advanced_strip("""
                Could not connect to Postgres database! Check the Postgres credentials you
                supplied and/or your ~/.pgpass file if it exists."""))

        con_str = f'postgresql://{self.dbuser}@localhost:5432/{self.dbname}'
        return sqlalchemy.create_engine(con_str)

    def execute(self, sql, logfile=None, log_ts=False, progress=False):
        """
        Execute list of SQL statements or a single statement, in a transaction.

        RESUME HERE
        """

        if progress:
            from tqdm import tqdm

        self.logger.logvars(locals())

        if logfile is None:
            write_log = False
        else:
            assert isinstance(logfile, str)
            write_log = True

        if write_log:
            self.logger.info("Writing output to file: " + logfile)

        sql = pydoni.ensurelist(sql)

        with self.dbcon.begin() as con:
            if progress:
                pbar = tqdm(total=len(sql), unit='query')

            for stmt in sql:
                con.execute(sqlalchemy.text(stmt))

                if write_log:
                    with open(logfile, 'a') as f:
                        entry = stmt + '\n'

                        if log_ts:
                            entry = pydoni.systime() + ' ' + entry

                        f.write(entry)

                if progress:
                    pbar.update(1)

        if progress:
            pbar.close()

        self.logger.info("All SQL statement(s) executed successfully")
        return True
