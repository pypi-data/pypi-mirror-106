# Halloumi SES User

Library used to create IAM Users and generates the SES credentials to use with the AWS Simple Email Service (SES).

## Usage

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.core as cdk
import halloumi_ses_user as halloumi_ses_user

class SesUserStack(cdk.Stack):
    def __init__(self, scope, id, *, description=None, env=None, stackName=None, tags=None, synthesizer=None, terminationProtection=None, analyticsReporting=None):
        super().__init__(scope, id, description=description, env=env, stackName=stackName, tags=tags, synthesizer=synthesizer, terminationProtection=terminationProtection, analyticsReporting=analyticsReporting)
        halloumi_ses_user.SesUser(self, "SESUser")
```

For more information, please check the [API Doc](API.md)
