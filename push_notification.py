import boto3

SNS_RESOURCE = boto3.resource('sns')

def send_sms(msg : str, phone_number : str):
	try:
		response = SNS_RESOURCE.meta.client.publish(
			PhoneNumber=phone_number, Message=msg
		)
		message_id = response["MessageId"]
		logger.info(message_id)
		logger.info("Published message to %s.", phone_number)
	except ClientError:
		logger.exception("Couldn't publish message to %s.", phone_number)
		raise
	else:
		return message_id