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