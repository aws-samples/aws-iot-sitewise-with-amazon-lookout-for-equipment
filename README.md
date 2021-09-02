## Integrating AWS IoT SiteWise and Amazon Lookout for Equipment

AWS IoT SiteWise service is an Amazon Web Service to collect data from the plant floor with a local gateway, structures and labels that data, and generates real time KPIs to make better data-driven decisions. Amazon Lookout for Equipment is an applied AI/ML service specifically developed for industrial/manufacturing workload. The performance of these two services can be significantly strengthened by integrating Lookout for Equipment with IoT SiteWise. With this integration, it will shift this industry from reactive, descriptive analytics to proactive forecasting of poor performance, and achieve automated ML workflow for asset diagnosis. Since Lookout for Equipment service is suitable for both single and multi-variate root causes, IoT SiteWise becomes a natural option for industrial data pipeline of this ML service with its robust multi measurements collection capability. 

To accelerate ML service enablement in manufacturing industry, this demonstrator deploys an end-to-end workflow to integrate these two services together, so that Lookout for Equipment can be used for anomaly detection of operating assets in near real time, with minimal latency. This solution seamlessly integrates outputs from Lookout for Equipment with the IoT SiteWise Alarm feature, so operational technology (OT) teams can be given automated early warning of their asset fleet health status change, and achieve proactive asset optimization with an AI-enabled solution. 

### Automatic setup with CloudFormation
You will deploy a CloudFormation template that will provision an environment for your work going forward. The first template will setup the IoT SiteWise simulator. In another browser window, login to your AWS account.

Once you have done that, open one of the link below (depending on the region closest to you) in a new tab to start the process of deploying the items you need via CloudFormation.

*Note: This material is designed to work in the regions where the service is available. Using other regions will cause issues.*

| Region |     | CloudFormation Stack |
| ---    | --- | --- |
| US East (N. Virginia) | **us-east-1** | [![Launch stack](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=LookoutForEquipmentSitewiseIntegration&templateURL=https://lookoutforequipmentbucket-us-east-1.s3.amazonaws.com/cloud-formation-templates/L4ESiteWiseAssetCFN.yml) |

After you setup the IoT SiteWise simulator with the above cloudformation, you can create a data pipeline with the following CloudFormation to integrate Lookout for Equipment and IoT SiteWise. 

*Note: This material is designed to work in the regions where the service is available. Using other regions will cause issues.*

| Region |     | CloudFormation Stack |
| ---    | --- | --- |
| US East (N. Virginia) | **us-east-1** | [![Launch stack](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=LookoutForEquipmentSitewisePipeline&templateURL=https://lookoutforequipmentbucket-us-east-1.s3.amazonaws.com/cloud-formation-templates/sitewise_export_s3.yml) |

This data pipeline comprises of four parts: 
* Stream AWS IoT SiteWise data to Amazon Simple Storage Service (S3) in near real time;
* Use AWS Lambda function to trigger Amazon Athena at scheduled time to reformat exported IoT SiteWise data in S3, and output data as CSV file for Lookout for Equipment inference scheduler to ingest;
* After Lookout for Equipment inference finished, use Lambda function to ingest Lookout for Equipment output data to specific measurement tags in IoT SiteWise;
* Setup AWS resources for running Lookout for Equipment service (e.g. Amazon SageMaker Notebook and S3 bucket).

## Considerations for Practical Implementations

For demonstration purpose, an AWS IoT SiteWise simulator is used to simulate the measurement value updates for industrial asset in this blog. For real industrial applications, OT team can configure data sources, such as OPC-UA server, to ingest asset data to AWS IoT SiteWise. 
In this demo, an asset group with two level of hierarchy deployed. In reality, the number of hierarchies and the number of assets within each hierarchy can be significantly more (https://docs.aws.amazon.com/general/latest/gr/iot-sitewise.html). However, since Lambda functions used in data engineering pipeline can be scaled up to meet the demand with concurrent invocations of Lambda functions, so this solution can be easily extended to large scale industrial assets.

## Clean Up procedures
CloudFormation stacks:
To avoid incurring future charges, navigate to the CloudFormation console and delete two CloudFormation stacks created from this blog walkthrough. 

Cloud Watch Log groups: 

* Delete cloud watch log groups created associated with asset alarm models, asset models and assets creation. 
* Delete log groups associated with Lambda functions created in this solution.   

S3 Buckets: 

* Navigate  to the S3 console, 
* Empty and delete these two S3 buckets created in the second CloudFormation for Amazon Lookout for Equipment training and inference.  
* Empty S3 bucket for AWS IoT SiteWise data storage. 

SiteWise Monitor:

* Delete SiteWise monitor dashboards first, then delete SiteWise project you created for this SiteWise demo.

Lookout for Equipment:

* Stop the inference scheduler, and delete Inference Schedulers for models developed in Lookout for Equipment
* Delete Inference Scheduler developed in Lookout for Equipment
* Delete datasets developed in Lookout for Equipment  

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

