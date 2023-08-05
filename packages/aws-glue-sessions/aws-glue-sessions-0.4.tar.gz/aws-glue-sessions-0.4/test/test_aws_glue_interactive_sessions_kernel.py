import json
import time
import unittest

import pytest
from aws_glue_interactive_sessions_kernel.glue_python_kernel.GlueKernel import GlueKernel
import aws_glue_interactive_sessions_kernel.glue_python_kernel.constants
from unittest.mock import patch, MagicMock
from unittest import TestCase

GLUE_ROLE_ARN = 'arn:aws:iam::517487340733:role/GlueTesting'
SEND_OUTPUT_PATH = <insert ROLE ARN>

class KernelTest(unittest.TestCase):

    def fake_output(self):
        return None

    def test_aws_glue_interactive_sessions_kernel_importable(self):
        import aws_glue_interactive_sessions_kernel  # noqa: F401

    def test_set_region(self):
        kernel = GlueKernel()
        kernel.set_region('us-east-2')
        assert kernel.get_region() == 'us-east-2'
        kernel.set_region('us-west-2')
        assert kernel.get_region() == 'us-west-2'

    def test_set_glue_arn(self):
        kernel = GlueKernel()
        kernel.set_glue_role_arn('arn')
        assert kernel.get_glue_role_arn() == 'arn'
        kernel.set_region('arn2')
        assert kernel.get_region() == 'arn2'

    def test_authenticate(self):
        kernel = GlueKernel()
        with patch(SEND_OUTPUT_PATH, MagicMock(return_value=self.fake_output())):
            kernel.set_region('us-east-1')
            kernel.set_glue_role_arn(GLUE_ROLE_ARN)
            kernel.glue_client = kernel.authenticate(glue_role_arn=kernel.get_glue_role_arn())
            assert kernel.glue_client

    def test_create_session(self):
        kernel = GlueKernel()
        with patch(SEND_OUTPUT_PATH, MagicMock(return_value=self.fake_output())):
            kernel.set_region('us-east-1')
            kernel.set_glue_role_arn(GLUE_ROLE_ARN)
            kernel.glue_client = kernel.authenticate(glue_role_arn=kernel.get_glue_role_arn())
            kernel.create_session()
            assert kernel.get_session_id()

    def test_delete_session(self):
        kernel = GlueKernel()
        with patch(SEND_OUTPUT_PATH, MagicMock(return_value=self.fake_output())):
            kernel.set_region('us-east-1')
            kernel.set_glue_role_arn(GLUE_ROLE_ARN)
            kernel.glue_client = kernel.authenticate(glue_role_arn=kernel.get_glue_role_arn())
            kernel.create_session()
            assert kernel.get_session_id()
            kernel.delete_session()
            assert not kernel.glue_client
            assert not kernel.get_session_id()

    def test_disconnect_session(self):
        kernel = GlueKernel()
        with patch(SEND_OUTPUT_PATH, MagicMock(return_value=self.fake_output())):
            kernel.set_region('us-east-1')
            kernel.set_glue_role_arn(GLUE_ROLE_ARN)
            kernel.glue_client = kernel.authenticate(glue_role_arn=kernel.get_glue_role_arn())
            kernel.create_session()
            assert kernel.get_session_id()
            kernel.disconnect()
            assert not kernel.get_session_id()

    def test_run_statement(self):
        kernel = GlueKernel()
        with patch(SEND_OUTPUT_PATH, MagicMock(return_value=self.fake_output())):
            kernel.set_region('us-east-1')
            kernel.set_glue_role_arn(GLUE_ROLE_ARN)
            kernel.glue_client = kernel.authenticate(glue_role_arn=kernel.get_glue_role_arn())
            kernel.create_session()
            assert kernel.get_session_id()
            statement_id = kernel.glue_client.run_statement(SessionId=kernel.get_session_id(), Code="print('hello world')")["Id"]
            assert statement_id != None
            statement = kernel.glue_client.get_statement(SessionId=kernel.get_session_id(), Id=statement_id)["Statement"]
            statement_output = statement["Output"]["Data"]["TextPlain"]
            status = statement["State"]
            assert status == 'AVAILABLE'
            assert statement_output == 'hello world'


    def test_authenticate_no_arn(self):
        kernel = GlueKernel()
        with patch(SEND_OUTPUT_PATH, MagicMock(return_value=self.fake_output())):
            with pytest.raises(Exception) as e_info:
                kernel.set_region('us-east-1')
                kernel.authenticate()
                assert str(e_info.value) == 'Neither glue_role_arn nor profile were provided'

    def test_configure(self):
        kernel = GlueKernel()
        with patch(SEND_OUTPUT_PATH, MagicMock(return_value=self.fake_output())):
            configs = '{\"region\":\"us-east-2\", \"iam_role\":\"iam_role\", \"extra_py_files\":\"a,b,c,d\"}'
            kernel.configure(configs)
            assert kernel.get_region() == 'us-east-2'
            assert kernel.get_glue_role_arn() == 'iam_role'
            assert kernel.get_extra_py_files() == 'a,b,c,d'


