import logging

logger = logging.getLogger('my_logger')
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(message)s')
handler.setFormatter(formatter)
logger.setLevel(logging.DEBUG)
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)

logger.debug('Проверка того, что сообщения уровня DEBUG обрабатываются и логгером, и обработчиком.')
logger.info('Тестовое сообщение уровня INFO')
logger.error('Ещё одно сообщение, но уже уровня ERROR')
