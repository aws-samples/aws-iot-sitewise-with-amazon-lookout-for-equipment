After launch the SiteWiseSimulator cloudformation, the following AWS resources will be created: 

1. Three Amazon IoT SiteWise assets: two for centrifugal pumps (child asset) and one for pump station (parent asset);
2. Two SiteWise Alarm models: one for pump station and one for centrifugal pump;
3. Relevant IAM Role and Policies for SiteWise Alarm to access IoT Events and vice versa; 
4. Three Lambda functions to create Alarm models, Asset Models and Assets programmatically;
5. One Lambda function to publish 30 sensor data to relevant SiteWise measurement tags at frequency of 1 Hz; 
6. CloudWatch Event scheduler to trigger Lambda function to publish data to SiteWise;
7. Relevant IAM policies and roles that permit the Lambda functions to do the following: (1) Access SiteWise to create assets/assets models, and alarm models; (2) Update SiteWise asset property values with BatchPutMessage operation; 
8. Permission to allow CloudWatch Event to trigger Lambda function to batch put asset property values;
9. CloudWatch Log Group for monitoring individual Lambda function.
