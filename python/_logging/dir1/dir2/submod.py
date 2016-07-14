import logging


LOG = logging.getLogger(__name__)
LOG.info('logger of submod say something...')

def tst():
    LOG.info('this is submod.tst()...')
