"""This module contains common Pytest fixtures and hooks for unit tests."""

from pytest import fixture
from six.moves import mock

from robotframework_reportportal.listener import listener
from robotframework_reportportal.result_visitor import RobotResultsVisitor


@fixture()
def visitor():
    return RobotResultsVisitor()


@fixture()
def mock_variables():
    mock_variables = mock.Mock()
    mock_variables.endpoint = "http://localhost:8080"
    mock_variables.launch_name = "Robot"
    mock_variables.project = "default_personal"
    mock_variables.uuid = "test_uuid"
    mock_variables.launch_attributes = ''
    mock_variables.launch_id = None
    mock_variables.launch_doc = None
    mock_variables.log_batch_size = 1
    mock_variables.mode = None
    mock_variables.pool_size = 1
    mock_variables.skip_analytics = None
    mock_variables.test_attributes = []
    mock_variables.skip_analytics = True
    mock_variables.pabot_used = None
    mock_variables.skipped_issue = True
    return mock_variables


@fixture()
def mock_listener(mock_variables):
    mock_listener = listener()
    mock_listener._variables = mock_variables
    return mock_listener


@fixture()
def suite_attributes():
    return {
        'id': 's1',
        'doc': '',
        'longname': 'Suite',
        'metadata': {},
        'source': '/Users/User/work/tests/robot/test.robot',
        'suites': [],
        'tests': ['Test'],
        'starttime': '20210407 12:24:27.116',
        'totaltests': 1
    }


@fixture()
def test_attributes():
    return {
        'id': 's1-t1',
        'doc': '',
        'longname': 'Suite.Test',
        'tags': [],
        'source': '/Users/User/work/tests/robot/test.robot',
        'template': '',
        'starttime': '20210407 12:24:27.116'
    }
