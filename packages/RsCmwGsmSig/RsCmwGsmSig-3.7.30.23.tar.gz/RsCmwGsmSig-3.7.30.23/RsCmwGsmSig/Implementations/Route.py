from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup
from ..Internal.StructBase import StructBase
from ..Internal.ArgStruct import ArgStruct
from .. import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Route:
	"""Route commands group definition. 9 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("route", core, parent)

	@property
	def scenario(self):
		"""scenario commands group. 5 Sub-classes, 1 commands."""
		if not hasattr(self, '_scenario'):
			from .Route_.Scenario import Scenario
			self._scenario = Scenario(self._core, self._base)
		return self._scenario

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Scenario: enums.Scenario: SCEL | IORI | BATC | SCF | SCFDiversity SCEL: 'Standard Cell' IORI: 'IQ out - RF in' BATC: 'BCCH and TCH/PDCH' SCF: 'Standard Cell Fading' SCFDiversity: 'Standard Cell Fading with RX Diversity'
			- Controller: str: For future use - returned value not relevant
			- Rx_Connector: enums.RxConnector: RF connector for the input path
			- Rx_Converter: enums.RxConverter: RX module for the input path
			- Tx_Connector_1: enums.TxConnector: RF or DIG IQ OUT connector for output path 1
			- Tx_Converter_1: enums.TxConverter: TX or I/Q module for output path 1
			- Tx_Connector_2: enums.TxConnector: RF connector for output path 2, only returned for scenarios with two RF output paths
			- Tx_Converter_2: enums.TxConverter: TX module for output path 2, only returned for scenarios with two RF output paths
			- Iq_1_Connector: enums.TxConnector: DIG IQ OUT connector for the first output path, only returned for scenarios with external fading
			- Iq_2_Connector: enums.TxConnector: DIG IQ OUT connector for the second output path, only returned for scenarios with external fading with two paths
			- Fader: enums.FadingBoard: I/Q board used for internal fading"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Scenario', enums.Scenario),
			ArgStruct.scalar_str('Controller'),
			ArgStruct.scalar_enum('Rx_Connector', enums.RxConnector),
			ArgStruct.scalar_enum('Rx_Converter', enums.RxConverter),
			ArgStruct.scalar_enum('Tx_Connector_1', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_Converter_1', enums.TxConverter),
			ArgStruct.scalar_enum('Tx_Connector_2', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_Converter_2', enums.TxConverter),
			ArgStruct.scalar_enum('Iq_1_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Iq_2_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Fader', enums.FadingBoard)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Scenario: enums.Scenario = None
			self.Controller: str = None
			self.Rx_Connector: enums.RxConnector = None
			self.Rx_Converter: enums.RxConverter = None
			self.Tx_Connector_1: enums.TxConnector = None
			self.Tx_Converter_1: enums.TxConverter = None
			self.Tx_Connector_2: enums.TxConnector = None
			self.Tx_Converter_2: enums.TxConverter = None
			self.Iq_1_Connector: enums.TxConnector = None
			self.Iq_2_Connector: enums.TxConnector = None
			self.Fader: enums.FadingBoard = None

	# noinspection PyTypeChecker
	def get_value(self) -> ValueStruct:
		"""SCPI: ROUTe:GSM:SIGNaling<Instance> \n
		Snippet: value: ValueStruct = driver.route.get_value() \n
		Returns the configured routing settings. The number of returned values depends on the active scenario (6 to 10 values) .
		For possible connector, converter and fader values, see 'Values for Signal Path Selection'. \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:GSM:SIGNaling<Instance>?', self.__class__.ValueStruct())

	def clone(self) -> 'Route':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Route(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
