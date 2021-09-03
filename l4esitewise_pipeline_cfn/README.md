## AWS Resources that will be created with l4esitewise_pipeline_cfn

* an S3 bucket for SiteWise data export
* S3 buckets for Lookout for Equipment inference scheduler 
* an Amazon IoT Core rule
* IAM roles and policies that are necessary
* an Amazon Kinesis Data Firehouse stream
* Amazon Lambda functions to send SiteWise data from IoT Core to Firehose
* an Amazon Glue database and two Glue tables: one fore asset property and one for metadata
* Athena query to transform SiteWise data for Lookout for Equipment inference
* a Lambda function “LocalResourcePrefix_l4einferenceschedule” to preprocess input data for Lookout for Equipment
* CloudWatch Events to schedule “LocalResourcePrefix_l4einferenceschedule” trigger
* a Lambda function “LocalResourcePrefix_l4einferenceoutput” that will be triggered by Lookout for Equipment output file upload in S3, and will send output messages to SIteWise  
* S3 PutObject trigger for Lambda function “LocalResourcePrefix_l4einferenceoutput”
* SageMaker Notebook instances used for  Lookout for Equipment model training
* CloudWatch log group for Lambda function and Kinesis Firehose monitoring

## Instruction for Creating l4esitewise_pipeline_cfn

*  Sign in to the Amazon Web Services Management Console. 
*  Click on this launch stack button:

| Region |     | CloudFormation Stack |
| ---    | --- | --- |
| US East (N. Virginia) | **us-east-1** | [![Launch stack](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=LookoutForEquipmentSitewisePipeline&templateURL=https://lookoutforequipmentbucket-us-east-1.s3.amazonaws.com/cloud-formation-templates/sitewise_export_s3.yml) |

* On the *Create stack* page, choose *Next* at the bottom of the page. 
* On the *Specify stack details* page, enter a *Stack Name* of your choice, enter a *l4eBucketPrefix* for the S3 bucket that this template creates for Lookout for Equipment. This bucket name must be globally unique. (https://docs.aws.amazon.com/AmazonS3/latest/userguide/BucketRestrictions.html#bucketnamingrules)
* *SiteWiseAsset1Id*: Fill in the UUID for Demo Pump Asset 1 that you obtained from the previous CloudFormation output
* *SiteWiseAsset2Id*:Fill in the UUID for Demo Pump Asset 2 that you obtained from the previous CloudFormation output
* (Optional) Change any of the template's other parameters:

* (Optional)*BucketPrefix* for the S3 bucket that this template creates in order to receive asset data. 

* (Optional)*GlobalResourcePrefix* – A prefix for names of global resources, such as IAM roles, created from this template. 
* (Optional)*LocalResourcePrefix* – A prefix for names of resources created from this template in the current Region. 
* Note: If you create this template multiple times, you should change the bucket name and resource prefix parameters in order to avoid resource name conflicts. For L4EBucketPrefix, there is a possibility that this bucketprefix was used by other readers, so please change the prefix to be globally unique.
* Choose *Next*. 
* On the *Configure stack options* page, choose *Next*. 
* At the bottom of the page, select the check box that says *I acknowledge that Amazon CloudFormation might create IAM resources*. 
* Choose *Create stack*. 

## Clean up procedure

* If you decide to relaunch the same cloudforamtion in your AWS account in the same region, pleaes follow the following Cleanup procedure to ensure resources created from the previous stack are deleted completely, since CloudFormation cannot create resources that already exist.

CloudFormation stacks: To avoid incurring future charges, navigate to the CloudFormation console and delete the previous CloudFormation stack.

Cloud Watch Log groups:

    Delete cloud watch log groups created associated with asset alarm models, asset models and assets creation.
    Delete log groups associated with Lambda functions created from the previous CloudFormation.

S3 Buckets:

    Navigate to the S3 console,
    Empty and delete these two S3 buckets created in the previous CloudFormation for Amazon Lookout for Equipment training and inference.
    Empty and delete the two S3 bucket used for SiteWise data storage.
