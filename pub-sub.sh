#!/bin/bash

topic_arn=$(awslocal sns create-topic --name test-producer | jq -r '.TopicArn')
queue_url=$(awslocal sqs create-queue --queue-name test-consumer | jq -r '.QueueUrl')
subscription_arn=$(awslocal sns subscribe --topic-arn $topic_arn --protocol sqs --notification-endpoint $queue_url | jq -r '.SubscriptionArn')

echo Created topic and queue url
echo QueueUrl: $queue_url
echo TopicArn: $topic_arn
echo SubscriptionArn: $subscription_arn

echo Sending test message
response=$(awslocal sns publish --topic-arn $topic_arn --message test)
echo Message sent with response: $response

echo Receive test message
receive_message=$(awslocal sqs receive-message --queue-url $queue_url)
echo Message sent with response: $receive_message

