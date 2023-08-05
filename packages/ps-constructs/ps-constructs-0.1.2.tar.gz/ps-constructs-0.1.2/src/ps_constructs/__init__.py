'''
# replace this
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from ._jsii import *

import aws_cdk.core


class CdkSampleLib(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="psconstructs.CdkSampleLib",
):
    def __init__(self, scope: aws_cdk.core.Construct, id: builtins.str) -> None:
        '''
        :param scope: -
        :param id: -
        '''
        jsii.create(CdkSampleLib, self, [scope, id])


__all__ = [
    "CdkSampleLib",
]

publication.publish()
