"""
    Ory Kratos API

    Documentation for all public and administrative Ory Kratos APIs. Public and administrative APIs are exposed on different ports. Public APIs can face the public internet without any protection while administrative APIs should never be exposed without prior authorization. To protect the administative API port you should use something like Nginx, Ory Oathkeeper, or any other technology capable of authorizing incoming requests.   # noqa: E501

    The version of the OpenAPI document: v0.0.0-alpha.38
    Contact: hi@ory.sh
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ory_kratos_client
from ory_kratos_client.model.submit_self_service_verification_flow_with_link_method import SubmitSelfServiceVerificationFlowWithLinkMethod


class TestSubmitSelfServiceVerificationFlowWithLinkMethod(unittest.TestCase):
    """SubmitSelfServiceVerificationFlowWithLinkMethod unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSubmitSelfServiceVerificationFlowWithLinkMethod(self):
        """Test SubmitSelfServiceVerificationFlowWithLinkMethod"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SubmitSelfServiceVerificationFlowWithLinkMethod()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
