## SiteWise L4E Integration

AWS IoT SiteWise service is an Amazon service to collect data from the plant floor with a local gateway, structures and labels that data, and generates real time KPIs to make better data-driven decisions. On the other hand, Lookout for Equipment is Amazon latest applied AI/ML service specifically developed for industrial/manufacturing workload. The performance of these two services can be significantly strengthened by integrating Lookout for Equipment with Amazon SiteWise. With this integration, it will shift this industry from reactive, descriptive analytics to proactive forecasting of poor performance, and achieve automated ML workflow for asset diagnosis. Since Lookout for Equipment service is suitable for both single and multi-variate root causes, Amazon SiteWise becomes a natural option for industrial data pipeline of this ML service with its robust multi measurements collection capability. To accelerate ML service enablement in manufacturing industry, this blog developed an end to end workflow to integrate these two services together, so that Lookout for Equipment can be used for anomaly detection of operating assets in near real time, with minimal latency. This solution seamlessly integrates outputs from Lookout for Equipment with latest SiteWise Alarm feature, so OT team can be given automated early warning of their asset fleet health status change, and achieve proactive asset optimization with AI enabled AWS IoT SiteWise service. 

### Automatic setup with CloudFormation
You will deploy a CloudFormation template that will provision an environment for your work going forward. In another browser window, login to your AWS account.

Once you have done that, open one of the link below (depending on the region closest to you) in a new tab to start the process of deploying the items you need via CloudFormation.

*Note: This material is designed to work in the regions where the service is available. Using other regions will cause issues.*

| Region |     | CloudFormation Stack |
| ---    | --- | --- |
| US East (N. Virginia) | **us-east-1** | [![Launch stack](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=LookoutForEquipmentSitewiseIntegration&templateURL=https://github.com/aws-samples/aws-iot-sitewise-with-amazon-lookout-for-equipment/blob/main/l4esitewise_pipeline_cfn/sitewise_export_s3_080121.yml) |


## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

