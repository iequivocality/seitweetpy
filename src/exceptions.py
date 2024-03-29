class CredentialsFileFormatError(Exception):
	"""exception raised when credentials file format is incorrect"""
	def __init__(self, message):
		super(CredentialsFileFormatError, self).__init__(message)

class InvalidCredentialsError(Exception):
	"""exception raised when credentials file format is incorrect"""
	def __init__(self, message):
		super(InvalidCredentialsError, self).__init__(message)

class InvalidArgumentsError(Exception):
	"""exception raised when option arguments passed are incorrect"""
	def __init__(self, message):
		super(InvalidArgumentsError, self).__init__(message)