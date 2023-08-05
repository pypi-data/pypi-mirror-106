from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cvalue:
	"""Cvalue commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cvalue", core, parent)

	# noinspection PyTypeChecker
	class RangeStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Lower: int: Range: -110 dBm to -48 dBm, Unit: dBm
			- Upper: int: Range: -110 dBm to -48 dBm, Unit: dBm"""
		__meta_args_list = [
			ArgStruct.scalar_int('Lower'),
			ArgStruct.scalar_int('Upper')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Lower: int = None
			self.Upper: int = None

	def get_range(self) -> RangeStruct:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:RREPort:CVALue:RANGe \n
		Snippet: value: RangeStruct = driver.sense.rreport.cvalue.get_range() \n
		Returns the signal level range, corresponding to the 'C value' index reported by the MS. \n
			:return: structure: for return value, see the help for RangeStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:GSM:SIGNaling<Instance>:RREPort:CVALue:RANGe?', self.__class__.RangeStruct())

	def get_value(self) -> int:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:RREPort:CVALue \n
		Snippet: value: int = driver.sense.rreport.cvalue.get_value() \n
		Returns the 'C value' reported by the MS as dimensionless index. \n
			:return: cvalue: Range: 0 to 63
		"""
		response = self._core.io.query_str('SENSe:GSM:SIGNaling<Instance>:RREPort:CVALue?')
		return Conversions.str_to_int(response)
