'''
# cdk-lambda-subminute

This construct creates a state machine that can invoke a Lambda function per time unit which can be less than one minute. You only need to craft a Lambda function and then assign it as an argument into the construct. An example is included.

https://docs.aws.amazon.com/cdk/api/latest/docs/aws-s3-assets-readme.html#asset-bundling
https://github.com/aws/aws-cdk/issues/8589
https://github.com/aws/aws-cdk/issues/14516
https://github.com/aws/aws-cdk/issues/11914

https://github.com/aws/aws-cdk/blob/master/packages/%40aws-cdk/core/lib/asset-staging.ts
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

import aws_cdk.aws_lambda
import aws_cdk.core


class LambdaSubminute(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="projen-statemachine-example.LambdaSubminute",
):
    def __init__(
        self,
        parent: aws_cdk.core.Construct,
        name: builtins.str,
        *,
        target_function: aws_cdk.aws_lambda.IFunction,
    ) -> None:
        '''
        :param parent: -
        :param name: -
        :param target_function: The Lambda function that is going to be executed per time unit less than one minute.
        '''
        props = LambdaSubminuteProps(target_function=target_function)

        jsii.create(LambdaSubminute, self, [parent, name, props])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="iteratorFunction")
    def iterator_function(self) -> aws_cdk.aws_lambda.IFunction:
        '''The Lambda function that plays the role of the iterator.'''
        return typing.cast(aws_cdk.aws_lambda.IFunction, jsii.get(self, "iteratorFunction"))


@jsii.data_type(
    jsii_type="projen-statemachine-example.LambdaSubminuteProps",
    jsii_struct_bases=[],
    name_mapping={"target_function": "targetFunction"},
)
class LambdaSubminuteProps:
    def __init__(self, *, target_function: aws_cdk.aws_lambda.IFunction) -> None:
        '''
        :param target_function: The Lambda function that is going to be executed per time unit less than one minute.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "target_function": target_function,
        }

    @builtins.property
    def target_function(self) -> aws_cdk.aws_lambda.IFunction:
        '''The Lambda function that is going to be executed per time unit less than one minute.'''
        result = self._values.get("target_function")
        assert result is not None, "Required property 'target_function' is missing"
        return typing.cast(aws_cdk.aws_lambda.IFunction, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaSubminuteProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "LambdaSubminute",
    "LambdaSubminuteProps",
]

publication.publish()
