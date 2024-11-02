import django.contrib.sessions.backends.db as db
# These imports necessary for the fix A2:2017-Broken Authentication
#import random
#from random import randrange

class SessionStore(db.SessionStore):
	session_counter = 0

	def _get_new_session_key(self):
		while True:
			# This fixes OWASP-2017 A2:2017-Broken Authentication issue
			# session_key = 'session-' + str(random.randint(1000000000, 10000000000))
			session_key = 'session-' + str(SessionStore.session_counter)
			SessionStore.session_counter += 1
			if not self.exists(session_key):
				return session_key