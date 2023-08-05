import typing
import os
from aws_cdk import (
    aws_lambda,
    aws_stepfunctions,
    aws_stepfunctions_tasks,
    aws_events,
    aws_events_targets,
    core
)

LAMBDAS_RUNTIME = os.environ.get('LAMBDAS_RUNTIME', aws_lambda.Runtime.PYTHON_3_7)
LAMBDAS_PATH = os.environ.get('LAMBDAS_PATH', './lambdas')


class StateMachine(core.Construct):
    _sm: aws_stepfunctions.IStateMachine = None
    _smprops: dict = {}
    lambdas_assets: aws_lambda.Code
    lambdas_runtime: aws_lambda.Runtime

    def __init__(self, scope: core.Construct, id: str, *, lambdas_path=LAMBDAS_PATH, lambdas_runtime=LAMBDAS_RUNTIME, **attr) -> None:
        super().__init__(scope, id, **attr)
        self.lambdas_runtime = lambdas_runtime
        self.assets = aws_lambda.Code.asset(lambdas_path)

    @property
    def sm(self) -> aws_stepfunctions.StateMachine:
        if not self._sm:
            self.sm = aws_stepfunctions.StateMachine(self, 'sm', **self.smprops)
        return self._sm

    @sm.setter
    def sm(self, value: aws_stepfunctions.StateMachine):
        self._sm = value

    @property
    def smprops(self) -> dict:
        if not self._smprops:
            self._smprops['definition'] = aws_stepfunctions.Pass(self, 'pass')
        return self._smprops

    @smprops.setter
    def smprops(self, value: typing.Union[aws_stepfunctions.StateMachineProps, dict]):
        if isinstance(value, aws_stepfunctions.StateMachineProps):
            self._smprops = value.__dict__['_values']
        self._smprops = value

    def launch(self, statemachine_props: aws_stepfunctions.StateMachineProps=None) -> aws_stepfunctions.StateMachine:
        self.smprops = statemachine_props
        core.CfnOutput(self, 'sm-arn', value=self.sm.state_machine_arn)
        return self.sm

    def lambda_task(
            self,
            name: str,
            fx: aws_lambda.IFunction=None,
            fx_attr: aws_lambda.FunctionProps=None,
            invoke: dict={}):
        if not fx:
            fx_attr = aws_lambda.FunctionProps(
                code=self.assets,
                handler=f"{name}.handler",
                runtime=self.lambdas_runtime
            )
            fx = aws_lambda.Function(
                self, "fxi_{}".format(name), **fx_attr.__dict__['_values']
            )

        return aws_stepfunctions_tasks.LambdaInvoke(
            self, "{}".format(name),
            lambda_function=fx,
            **invoke
        )

    def cron(self, name: str, cron: dict, *, input: aws_events.RuleTargetInput=None):
        rule = aws_events.Rule(self, name, schedule=aws_events.Schedule.cron(**cron))
        target = aws_events_targets.SfnStateMachine(
            self.sm,
            input=input
        )
        rule.add_target(target)
