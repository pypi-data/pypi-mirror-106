import datetime
from Cryptodome.Hash import SHA256, HMAC
from base64 import b64decode, b64encode

class GadgethiAuthenticationStandardEncryption():
	# First the header should increase two fields (1) key (2) secret (3) time
	# key and the secret will be given 
	# You need to put key, time, hmac_result in the header file 
	# Please call authentication to get the need information dictionary in the header file
	def __init__(self,key,secret):
		self.key = str(key) 
		self.secret = str(secret)

	def HMAC256_digest(self,secret,string,mode='base64'):
		# we give secret type is string
		if type(secret) != bytes:
			secret = secret.encode()
		h = HMAC.new(secret, digestmod=SHA256)
		if string != bytes:
			string = string.encode()
		h.update(string)
		if mode != 'base64':
			return h.hexdigest()
		else:
			b64 = b64encode(bytes.fromhex(h.hexdigest())).decode()
			return b64

	def HMAC256_encryption(self, time_shift):
		# We standardize Taipei as the standard time
		localtime = int(datetime.datetime.utcnow().timestamp()) + (time_shift*60*60)
		encryption_result = self.HMAC256_digest(self.secret,self.key+str(localtime))
		return encryption_result

	def time_standard(self, time_shift):
		return int(datetime.datetime.utcnow().timestamp()) + (time_shift*60*60)

	def authentication_encryption(self, time_shift=8):
		authentication_dictionary = {}
		authentication_dictionary['Gadgethi-Key'] = self.key
		authentication_dictionary['Hmac256-Result'] = self.HMAC256_encryption(time_shift)
		authentication_dictionary['time'] = str(self.time_standard(time_shift))
		return authentication_dictionary

class GadgethiAuthenticationStandardDecryption():
	# For server part
	def __init__(self,key,hmac256_result,time):
		self.key = key
		self.hmac256_result = hmac256_result
		self.time = time
		self.decline_reason = 'All Clear'

	def HMAC256_digest(self,secret,string,mode='base64'):
		# we give secret type is string
		if type(secret) != bytes:
			secret = secret.encode()
		h = HMAC.new(secret, digestmod=SHA256)
		if string != bytes:
			string = string.encode()
		h.update(string)
		if mode != 'base64':
			return h.hexdigest()
		else:
			b64 = b64encode(bytes.fromhex(h.hexdigest())).decode()
			return b64

	def accepting_time_range(self, time_shift,interval):
		localtime = int(datetime.datetime.utcnow().timestamp()) + (time_shift*60*60)
		if localtime - interval < int(self.time) < localtime + interval:
			return True
		else:
			self.decline_reason = 'time_range error'
			return False

	def encryption_comparsion(self, secret):
		encryption_result = self.HMAC256_digest(secret,self.key+str(self.time))
		if encryption_result == self.hmac256_result:
			return True
		else:
			self.decline_reason = 'encryption_comparsion error'
			return False

	def authentication_decryption(self, time_shift=8,interval=30,secret='gadgethi'):
		if self.encryption_comparsion(secret) and self.accepting_time_range(time_shift,interval):
			return {"indicator":True,"message":self.decline_reason}
		else:
			return {"indicator":False,"message":self.decline_reason}

if __name__ == "__main__":
	g = GadgethiAuthenticationStandardEncryption("nanshanddctablet", "gadgethi")
	print(g.HMAC256_digest(g.secret,g.key+"1619644177"))