import logging
logger=logging.getLogger("modernization")
logging.basicConfig(level=logging.INFO)
def record_request(correlation_id,operation):
    logger.info("operation=%s correlation_id=%s",operation,correlation_id)
