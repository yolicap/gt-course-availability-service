import check_availability as ca
import push_notification as pn

COURSE_CSNS = []

# E.164 format numbers
# e.g. +12065550101
PHONE_NUMBERS = []

INTERVAL_MINS = 300
MESSAGE_TEMPLATE = 'ALERT ‼️‼️‼️ class {csn} is availability!!!! seats: {seats} waitlist: {waitlist}'


def run():
	schedule.every(1).minutes.do(check_csns) 
	while True: 
		try:
			schedule.run_pending() 
		except Exception as e:
			print("sumin broke 😵")
		finally:
    		time.sleep(1)

def check_csns():
	for csn in COURSE_CSNS :
		availability = ca.check_availability(csn)

		# seats available
		if (availability[0] or availability[1]):
			msg = MESSAGE_TEMPLATE.format(csn = csn, seats = availability[0], waitlist = availability[1])

			for number in PHONE_NUMBERS :
				pn.send_sms(msg, number)


if __name__ == '__main__':
	COURSE_CSN.append(52498)
	PHONE_NUMBERS.append(None)
	run()