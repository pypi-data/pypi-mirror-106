from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RxQuality:
	"""RxQuality commands group definition. 4 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rxQuality", core, parent)

	@property
	def sub(self):
		"""sub commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_sub'):
			from .RxQuality_.Sub import Sub
			self._sub = Sub(self._core, self._base)
		return self._sub

	# noinspection PyTypeChecker
	class RangeStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Lower: float: Range: 0 % to 12.8 %, Unit: %
			- Upper: float: Range: 0.2 % to 100 %, Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_float('Lower'),
			ArgStruct.scalar_float('Upper')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Lower: float = None
			self.Upper: float = None

	def get_range(self) -> RangeStruct:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:RREPort:RXQuality:RANGe \n
		Snippet: value: RangeStruct = driver.sense.rreport.rxQuality.get_range() \n
		Returns the bit error rate range, corresponding to the 'RX Quality Full' index reported by the MS. \n
			:return: structure: for return value, see the help for RangeStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:GSM:SIGNaling<Instance>:RREPort:RXQuality:RANGe?', self.__class__.RangeStruct())

	def get_value(self) -> int:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:RREPort:RXQuality \n
		Snippet: value: int = driver.sense.rreport.rxQuality.get_value() \n
		Returns the 'RX Quality Full' reported by the MS as dimensionless index. \n
			:return: rx_quality: Range: 0 to 7
		"""
		response = self._core.io.query_str('SENSe:GSM:SIGNaling<Instance>:RREPort:RXQuality?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'RxQuality':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RxQuality(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
