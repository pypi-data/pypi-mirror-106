from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ecbep:
	"""Ecbep commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ecbep", core, parent)

	# noinspection PyTypeChecker
	class RangeStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Lower: float: Range: 0 to 1.75
			- Upper: float: Range: 0.25 to 2"""
		__meta_args_list = [
			ArgStruct.scalar_float('Lower'),
			ArgStruct.scalar_float('Upper')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Lower: float = None
			self.Upper: float = None

	def get_range(self) -> RangeStruct:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:RREPort:ECBep:RANGe \n
		Snippet: value: RangeStruct = driver.sense.rreport.ecbep.get_range() \n
		Returns the CV BEP range, corresponding to the 'CV BEP' index reported by the MS for an 8PSK modulated DL signal. \n
			:return: structure: for return value, see the help for RangeStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:GSM:SIGNaling<Instance>:RREPort:ECBep:RANGe?', self.__class__.RangeStruct())

	def get_value(self) -> int:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:RREPort:ECBep \n
		Snippet: value: int = driver.sense.rreport.ecbep.get_value() \n
		Returns the 'CV BEP', reported by the MS as dimensionless index for an 8PSK modulated DL signal. \n
			:return: cv_bep_8_psk: Range: 0 to 7
		"""
		response = self._core.io.query_str('SENSe:GSM:SIGNaling<Instance>:RREPort:ECBep?')
		return Conversions.str_to_int(response)
