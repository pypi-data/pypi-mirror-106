from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Svariance:
	"""Svariance commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("svariance", core, parent)

	# noinspection PyTypeChecker
	class RangeStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Lower: float: Range: 0 dB² to 15.75 dB², Unit: dB²
			- Upper: float: Range: 0.25 dB² to 15.75 dB², Unit: dB²"""
		__meta_args_list = [
			ArgStruct.scalar_float('Lower'),
			ArgStruct.scalar_float('Upper')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Lower: float = None
			self.Upper: float = None

	def get_range(self) -> RangeStruct:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:RREPort:SVARiance:RANGe \n
		Snippet: value: RangeStruct = driver.sense.rreport.svariance.get_range() \n
		Returns the signal variance range, corresponding to the 'Signal Variance' index reported by the MS. \n
			:return: structure: for return value, see the help for RangeStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:GSM:SIGNaling<Instance>:RREPort:SVARiance:RANGe?', self.__class__.RangeStruct())

	def get_value(self) -> int:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:RREPort:SVARiance \n
		Snippet: value: int = driver.sense.rreport.svariance.get_value() \n
		Returns the 'Signal Variance' reported by the MS as dimensionless index. \n
			:return: signal_variance: Range: 0 to 63
		"""
		response = self._core.io.query_str('SENSe:GSM:SIGNaling<Instance>:RREPort:SVARiance?')
		return Conversions.str_to_int(response)
