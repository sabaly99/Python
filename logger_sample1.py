import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)

def divide(a, b):
    logger.info("divide() called")

    try:
        result = a / b
        logger.info("Division successful")
        return result

    except Exception as e:
        err = logger.exception(f" error: {e} Cannot divide by zero")
        return err
print(divide(10, 667))