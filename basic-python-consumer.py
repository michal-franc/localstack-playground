import boto3
import uuid
import logging
import time

local_stack_sns_endpoint = 'http://localhost:4575'
local_stack_sqs_endpoint = 'http://localhost:4576'
local_stack_arn = 'arn:aws:sns:eu-west-1:123456789012:'
queue_name = 'test-consumer'

sns_client = boto3.client(
    'sns',
    endpoint_url=local_stack_sns_endpoint,
    aws_access_key_id='test',
    aws_secret_access_key='test',
    aws_session_token='test'
)

sqs_client = boto3.client(
    'sqs',
    endpoint_url=local_stack_sqs_endpoint,
    aws_access_key_id='test',
    aws_secret_access_key='test',
    aws_session_token='test'
)

topic_arn = '%stest-producer' % local_stack_arn
queue_arn = '%s%s' % (local_stack_arn, queue_name)
queue_endpoint = '%s/queue/%s' % (local_stack_sqs_endpoint, queue_name)

print "... Creating Queue ..."

response = sqs_client.create_queue(
        QueueName=queue_name
    )

print "... Queue Created ..."
print response

print "... Creating subscription ..."
response = sns_client.subscribe(
    TopicArn=topic_arn,
    Protocol='sqs',
    Endpoint=queue_arn
)

print "... subscription created %s" % response

print "... Consuming messages from %s ..." % queue_endpoint

i = 1

while 1:
    # wait_time_seconds count only 1 request in x seconds (0 - 20)
    # num_messages get x messages in same request (1 - 10)
    messages = sqs_client.receive_message(
            QueueUrl=queue_endpoint,
            WaitTimeSeconds=10,
            MaxNumberOfMessages=10
        )
    for message in messages:
        print 'message: %s' % message

    print "iteration %s" % i
    i += 1

