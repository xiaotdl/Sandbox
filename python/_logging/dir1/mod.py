import logging
from dir2 import submod


LOG = logging.getLogger(__name__)
LOG.info('logger of mod say something...')

def testLogger():
    LOG.debug('this is mod.testLogger...')
    submod.tst()
