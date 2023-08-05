# AWS CDK Datadog Resources

[![npm version](https://badge.fury.io/js/%40nomadblacky%2Fcdk-datadog-resources.svg)](https://badge.fury.io/js/%40nomadblacky%2Fcdk-datadog-resources)

An AWS CDK construct library that wrapped [DataDog/datadog-cloudformation-resources](https://github.com/DataDog/datadog-cloudformation-resources).

## Requirements

Before use this library, [register datadog-cloudformation-resources to your AWS account.](https://github.com/DataDog/datadog-cloudformation-resources#datadog-aws-cloudformation)

You need to register the correct version listed in `Supported Resources`.

## Supported CDK Languages

* TypeScript
* Python
* ~~Java~~ Sorry, there is a problem with the release. ([#22](https://github.com/NomadBlacky/cdk-datadog-resources/issues/22))

## Supported Resources

| Supported? | Resource                | Name                             | Description                                              | Datadog CF Version |
| :--------: | ----------------------- | -------------------------------- | -------------------------------------------------------- | ------------------ |
|            | Dashboards              | `Datadog::Dashboards::Dashboard` | [Create, update, and delete Datadog dashboards.](https://github.com/DataDog/datadog-cloudformation-resources/tree/master/datadog-dashboards-dashboard-handler)      | N/A                |
|            | Datadog-AWS integration | `Datadog::Integrations::AWS`     | [Manage your Datadog-Amazon Web Service integration.](https://github.com/DataDog/datadog-cloudformation-resources/tree/master/datadog-integrations-aws-handler) | N/A                |
|     ✅     | Monitors                | `Datadog::Monitors::Monitor`     | [Create, update, and delete Datadog monitors.](https://github.com/DataDog/datadog-cloudformation-resources/tree/master/datadog-monitors-monitor-handler)        | [3.0.0](https://github.com/DataDog/datadog-cloudformation-resources/blob/master/datadog-monitors-monitor-handler/CHANGELOG.md#300--2021-02-16)         |
|            | Downtimes               | `Datadog::Monitors::Downtime`    | [Enable or disable downtimes for your monitors.](https://github.com/DataDog/datadog-cloudformation-resources/tree/master/datadog-monitors-downtime-handler)      | N/A                |
|            | User                    | `Datadog::IAM::User`             | [ Create and manage Datadog users.](https://github.com/DataDog/datadog-cloudformation-resources/tree/master/datadog-iam-user-handler)                   | N/A                |

## Installation

TypeScript

```shell
npm install @nomadblacky/cdk-datadog-resources
```

Python

```shell
pip install cdk-datadog-resources
```

Java

```xml
<dependency>
    <groupId>dev.nomadblacky</groupId>
    <artifactId>cdk-datadog-resources</artifactId>
    <version>x.y.z</version>
</dependency>
```

## Usage

Belows are examples of TypeScript.

### Monitors

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
from aws_cdk.core import App, Stack
from nomadblacky.cdk_datadog_resources import DatadogMonitor

app = App()
stack = Stack(app, "CdkDatadogResourcesTestStack")

DatadogMonitor(stack, "TestMonitor",
    datadog_credentials={
        "api_key": process.env.DATADOG_API_KEY || "DATADOG_API_KEY",
        "application_key": process.env.DATADOG_APP_KEY || "DATADOG_APP_KEY"
    },
    query="avg(last_1h):sum:system.cpu.system{host:host0} > 100",
    type=MonitorType.QueryAlert,
    name="Test Monitor",
    options={
        "thresholds": {
            "critical": 100,
            "warning": 80,
            "o_k": 90
        },
        "notify_no_data": True,
        "evaluation_delay": 60
    }
)
```
