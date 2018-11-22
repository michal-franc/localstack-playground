import boto3
import uuid
import logging
import time

local_stack_sns_endpoint = 'http://localhost:4575'

local_stack_arn = 'arn:aws:sns:us-east-1:123456789012:'

client = boto3.client(
    'sns',
    endpoint_url=local_stack_sns_endpoint,
    aws_access_key_id='test',
    aws_secret_access_key='test',
    aws_session_token='test'
)

topic_arn = '%stest-producer' % local_stack_arn
print "sending messages to %s" % topic_arn

while 1:
    print "... producing message ..."
    response = client.publish(TopicArn=topic_arn, Message='test message - %s' % uuid.uuid4())
    print "... message send - response %s" % response
    time.sleep(1)
