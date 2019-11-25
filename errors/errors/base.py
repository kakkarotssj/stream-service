from enum import Enum


class ErrorBase(Enum):
	"""
	* Will be inherited by all Group-specific error classes
	* Every error will have three sub-parts:
		** Issue: which caused the following error
		** Help: which will give an idea on to resolve the error
		** Data: relevant data upon which following error occurred.
	* All the derived classes will be enumeration based, having Issue as enum-name and Help as enum-value
	"""

	@classmethod
	def raise_exception(cls, error, data, exception):
		issue = error.name
		help = error.value
		data = data['data']

		raise exception(issue, help, data)
