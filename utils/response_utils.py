import logging as logger

from deepdiff import DeepDiff


class ResponseUtils:

    @staticmethod
    def assert_response_jsons(expected_response, actual_response, fields_ignored=None):
        if fields_ignored is None:
            diff = DeepDiff(expected_response, actual_response, ignore_order=True)
        else:
            diff = DeepDiff(expected_response, actual_response, ignore_order=True,
                            exclude_paths=fields_ignored)

        if diff == {}:
            logger.info(diff)
            return True
        else:
            logger.info(diff)
            return False
