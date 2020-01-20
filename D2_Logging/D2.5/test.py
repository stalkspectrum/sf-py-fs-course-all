import logging

handler = logging.FileHandler(filename='test.log')
handler.setLevel(logging.DEBUG)
logger = logging.getLogger()
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

logger.debug('Debug test message')
logger.info('Info test message')
logger.warning('Warning test message')
logger.error('Error test message')
logger.critical('Critical test message')
