import logging
import logging.config
import json

LCF = open('config/logger.json', 'r')
LOGGER = json.load(LCF)
LCF.close()

logging.config.dictConfig(LOGGER)
logger = logging.getLogger(__name__)

logger.debug('[Logger Test for new Logger]: If you see this message then please update the module called it')
