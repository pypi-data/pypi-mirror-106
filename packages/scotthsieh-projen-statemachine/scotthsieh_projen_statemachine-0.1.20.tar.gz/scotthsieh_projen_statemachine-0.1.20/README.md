# projen-simple

Build a custom construct based on an AWS Blog post and use projen to publish to 4 language repositories.
(Hope Go is coming soon)

# Architecture

This library constrcution is referred to [this AWS blog](https://aws.amazon.com/tw/blogs/compute/introducing-amazon-api-gateway-service-integration-for-aws-step-functions/).

# How to utilize polyglot packages

## TypeScript

```bash
$ cdk --init language typescript
$ yarn add projen-statemachine-example
```

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
from scotthsieh_projen_statemachine import StateMachineApiGatewayExample

class TypescriptStack(cdk.Stack):
    def __init__(self, scope, id, props=None):
        super().__init__(scope, id, props)

        stage_name = "default"
        part_path = "pets"
        example_construct = StateMachineApiGatewayExample(self, "KerKer",
            stage_name=stage_name, part_path=part_path
        )

        cdk.CfnOutput(self, "OStateMachine",
            value=example_construct.state_machine.state_machine_arn
        )
        cdk.CfnOutput(self, "OExecutionOutput",
            value=example_construct.execution_input, description="Sample input to StartExecution."
        )
```

## Python

```bash
$ cdk init --language python
$ cat <<EOL > requirements.txt
aws-cdk.core
scotthsieh_projen_statemachine
EOL
$ python -m pip install -r requirements.txt
```

```python
from aws_cdk import core as cdk
from scotthsieh_projen_statemachine import StateMachineApiGatewayExample

class PythonStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
         super().__init__(scope, construct_id, **kwargs)

         stage_name = 'default'
         part_path = 'pets'
         example_construct = StateMachineApiGatewayExample(
             self, 'PythonStatemachne', stage_name=stage_name, part_path=part_path,
         )

         cdk.CfnOutput(self, "OStateMachine",
             value=example_construct.state_machine.state_machine_arn
         )
         cdk.CfnOutput(self, "OExecutionOutput", value=example_construct.execution_input, description="Sample input to StartExecution.")
```

# References

* [jsii reference](https://github.com/cdklabs/jsii-release)
* [aws-cdk-go](https://github.com/aws/aws-cdk-go)
* [jsii](https://github.com/aws/jsii)
