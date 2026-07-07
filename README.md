# AWS Lambda Image Processing

## Project Overview

This project demonstrates a serverless image processing workflow using AWS Lambda and Amazon S3.

When an image is uploaded to a source S3 bucket, an S3 event automatically triggers a Lambda function that resizes the image and stores the processed version in a destination S3 bucket. Amazon CloudWatch Logs is used to monitor and validate the function execution.

## Architecture Components

- AWS Lambda
- Amazon S3 (Source Bucket)
- Amazon S3 (Destination Bucket)
- Amazon CloudWatch Logs

## Architecture

tbd...

## Skills Demonstrated

- AWS Lambda
- Amazon S3
- Serverless Computing
- Event-Driven Architecture
- S3 Event Notifications
- Amazon CloudWatch Logs
- Serverless Image Processing

## Implementation Steps

1. Created two Amazon S3 buckets for source and processed images.
2. Created an AWS Lambda function using Python.
3. Configured the source S3 bucket as the Lambda event trigger.
4. Uploaded an image to the source bucket.
5. Automatically resized the image using the Lambda function.
6. Stored the processed image in the destination S3 bucket.
7. Verified the execution using Amazon CloudWatch Logs.

## What I Learned

- AWS Lambda fundamentals
- Serverless computing
- Event-driven architecture
- Amazon S3 event notifications
- Image processing with AWS Lambda
- Monitoring Lambda executions with Amazon CloudWatch Logs

## Possible Improvements

- Configure environment variables for greater flexibility.
- Add exception handling and structured logging.
- Support additional image formats and configurable thumbnail sizes.
- Configure Amazon CloudWatch alarms for execution monitoring.

## Project Files

- Architecture Diagram (Lucidchart)
- Lambda Function Overview
- Source S3 Bucket
- Destination S3 Bucket
- Amazon CloudWatch Logs
- Lambda Source Code
