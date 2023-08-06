from falcon import Request, Response

from citibox.gcloudlogger.contrib import Middleware
from citibox.gcloudlogger.contrib.falcon.falcon_record_factory import FalconRecordFactory


class FalconMiddleware(Middleware):

    def __init__(self):
        super().__init__()
        self.params = {}

    def process_resource(self, request: Request, response: Response, resource, params: dict):
        self.params = params

    def process_response(self, request: Request, response: Response, resource, req_succeeded: bool):
        """
        :param req: falcon.Request
        :param resp: falcon.Response
        :param resource: Resource object
        :param req_succeeded: bool
        :return:
        """
        log_record_factory = FalconRecordFactory(request=request, response=response, params=self.params)

        try:
            log_record = log_record_factory.build()
            self.logger.info(
                log_record.message,
                extra=log_record.to_dict()
            )
        except Exception as e:  # pragma nocover
            pass
