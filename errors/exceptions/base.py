class ExceptionBase(Exception):
	"""
	* Will be inherited by all Exception classes
	* Throws particularly three points every time exception is raised.
		** Issue
		** Help
		** Data
			*** Read ErrorBase class for more info on these.
	"""

	def __init__(self, issue, help, data):
		super(ExceptionBase, self).__init__(issue, help, data)
