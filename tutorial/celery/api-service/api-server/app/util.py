import sys

from app import app


def try_commit(session):
    try:
        session.commit()
    except BaseException:
        e = sys.exc_info()[0]
        app.logger.error('Error: %s', e)
        session.rollback()
        raise
