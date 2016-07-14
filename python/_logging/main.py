import logging
import logging.config

def setup_logging():
    logging.config.fileConfig('logging.conf')
    return logging.getLogger()

def main():
    LOG = setup_logging()

    LOG.info('========== start the ball rolling ==========')

    LOG.debug('test root logger...')

    from dir1 import mod

    LOG.debug('let\'s test mod.testLogger()')
    mod.testLogger()

    LOG.info('finish test...')

if __name__ == '__main__':
    main()

# >>>
# 18:12:18 -     INFO: start the ball rolling...
# 18:12:18 -     INFO: logger of submod say something...
# 18:12:18 -     INFO: logger of mod say something...
# 18:12:18 -     INFO: this is submod.tst()...
# 18:12:18 -     INFO: finish test...
