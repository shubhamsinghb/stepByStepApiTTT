import json
import logging
import os

import pytest
import logging as logger
from utils.reporting_utils.slack_reporting.slack_client import SlackClient

pytest.failed_nodes = []


def pytest_sessionstart(session):
    session.results = dict()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    if result.when in ['call', 'setup']:
        item.session.results[item] = result
    if result.failed:
        node_id = result.nodeid
        test_case = node_id.split('::')[1]
        pytest.failed_nodes.append(test_case)


def pytest_sessionfinish(session):
    passed_amount = sum(1 for result in session.results.values() if result.passed)
    failed_amount = sum(1 for result in session.results.values() if result.failed)
    failed_amount = sum(1 for result in session.results.values() if result.failed)
    skipped_amount = sum(1 for result in session.results.values() if result.skipped)
    logger.info(f'there are {passed_amount} passed and {failed_amount} failed tests' and {skipped_amount})
    env = os.environ.get("ENV")
    failed = "\n".join(':point_right:  ' + x for x in pytest.failed_nodes)
    message = {
        'channel': (os.environ.get("SLACK_CHANNEL", '#general')),
        'text': f':thumbsup: Passed Tests :: {passed_amount}\n:thumbsdown: Failed Tests :: {failed_amount}\n'
                f':thinking_face: Skipped Tests :: {skipped_amount}\n'
                f':computer:Environment :: {env}\n\n'
                f':red_circle: List failed test \n{failed}'

    }
    if os.environ.get("SLACK_AUTH_TOKEN_QA") is not None:
        token= 'Bearer ' + os.environ.get("SLACK_AUTH_TOKEN_QA")
        response = SlackClient.slack_post_with_auth(payload=json.dumps(message),
                                                    auth=token)
