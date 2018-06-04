# AWS Lambda Flowlogs To Graylog

## Description

AWS Lambda function to sendo AWS Flow Logs to a [Graylog](https://www.graylog.org/) UDP Input.

## Configure Graylog UDP Input

Registering a new **RAW UDP** input in our Graylog server:

    * Login to your graylog server.
    * Go to "System > Inputs" select "RAW/Plaintext UDP" and then "Launch new input". 
    * Fill the form with best parameters for your config. 
    * Click "Save".

## Configure AWS Flow logs

    * Login into your AWS cccount.
    * Go to "EC2 (Elastic Computer Cloud)" service. 
    * From the left menu, select "Network Interfaces"
    * Select the network interface that you want to enable flow logs. 
    * Go to "Flow Logs" tab.
    * Click "Create Flow Log"
    * Select a role that has permissions to write/create log groups at AWS CloudWatch. If you don't have any existing role, you must to create it. See the reference guide bellow.
    * Select your "Destination Log Group". Something like "/flow/to/graylog" it's a good start point.
    * Click "Create Flow Log". This can take up 15 minutes.

**References**: 
[AWS Flow Logs User guid](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/flow-logs.html)

## Configure Lambda function

    * Login into your AWS account.
    * Go to "Lambda" Service. 
    * Click "Create function".
    * Select "Author from scratch" option
    * Setup a name to your lambda function. Example: flowToGraylog
    * Select "Python 2.7" (was not tested on Python 3.6)
    * Select the role to your function. This role must have permissions to write/create log groups and permissions to run with a VPC. See reference bellow.
    * Put the code of "lambda_function.py" in your Lambda function.
    * Set environment variable "GRAYLOG_IP" and "GRAYLOG_UDP_PORT" with your Graylog configuration at "Environment Variables".
    * Select your VPC, subnet and security groups at "Network".
    * (Optional) You can configure a "test event" at your lambda fucntion to check if all is ok. Choose "CloudWatch Logs" from "Event Template".

**References**:
[AWS Lambda VPC Execution](https://docs.aws.amazon.com/lambda/latest/dg/vpc-rds-create-iam-role.html)


## Create subscription for log group 

    * Login into your AWS account.
    * Go to "Cloud Watch" service.
    * Select "Logs" from left menu. 
    * Select the log group created on the early step. 
    * Click on "Action" and then "Stream to AWS Lambda"
    * Select your lambda function. Then click "Next"
    * Select "Amazon VPC Flow logs" at "Log Format". Then click "Next"
    * Click "Start Streaming".

**References**:
[CloudWatch Subscriptions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateSubscriptionFilter.html)





