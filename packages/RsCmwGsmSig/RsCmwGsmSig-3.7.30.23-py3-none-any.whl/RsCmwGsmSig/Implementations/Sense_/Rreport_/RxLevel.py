from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RxLevel:
	"""RxLevel commands group definition. 4 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rxLevel", core, parent)

	@property
	def sub(self):
		"""sub commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_sub'):
			from .RxLevel_.Sub import Sub
			self._sub = Sub(self._core, self._base)
		return self._sub

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
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:RREPort:RXLevel:RANGe \n
		Snippet: value: RangeStruct = driver.sense.rreport.rxLevel.get_range() \n
		Returns the power level range, corresponding to the 'RX Level Full' index reported by the MS. \n
			:return: structure: for return value, see the help for RangeStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:GSM:SIGNaling<Instance>:RREPort:RXLevel:RANGe?', self.__class__.RangeStruct())

	def get_value(self) -> int:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:RREPort:RXLevel \n
		Snippet: value: int = driver.sense.rreport.rxLevel.get_value() \n
		Returns the 'RX Level Full' reported by the MS as dimensionless index. \n
			:return: rx_level: Range: 0 to 63
		"""
		response = self._core.io.query_str('SENSe:GSM:SIGNaling<Instance>:RREPort:RXLevel?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'RxLevel':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RxLevel(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
