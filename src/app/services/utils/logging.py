import logging

logger = logging.getLogger('django')

class DynamicLogger:
    def __init__(self, logging_name='django'):
        """
        Args:
            logging_setting (str): 呼び出すログ設定
        """
        self.logger = logging.getLogger(logging_name)