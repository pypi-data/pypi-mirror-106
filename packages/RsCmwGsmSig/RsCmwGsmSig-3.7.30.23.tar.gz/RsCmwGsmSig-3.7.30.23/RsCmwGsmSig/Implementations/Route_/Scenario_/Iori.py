from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Iori:
	"""Iori commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("iori", core, parent)

	# noinspection PyTypeChecker
	class FlexibleStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Bb_Board: enums.BbBoard: Signaling unit
			- Rx_Connector: enums.RxConnector: RF connector for the input path
			- Rx_Converter: enums.RxConverter: RX module for the input path
			- Tx_Connector: enums.TxConnector: DIG IQ OUT rear panel connector for the output path
			- Tx_Converter: enums.TxConverter: For future use. In this software version, always send KEEP to ensure compatible settings."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Bb_Board', enums.BbBoard),
			ArgStruct.scalar_enum('Rx_Connector', enums.RxConnector),
			ArgStruct.scalar_enum('Rx_Converter', enums.RxConverter),
			ArgStruct.scalar_enum('Tx_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_Converter', enums.TxConverter)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Bb_Board: enums.BbBoard = None
			self.Rx_Connector: enums.RxConnector = None
			self.Rx_Converter: enums.RxConverter = None
			self.Tx_Connector: enums.TxConnector = None
			self.Tx_Converter: enums.TxConverter = None

	# noinspection PyTypeChecker
	def get_flexible(self) -> FlexibleStruct:
		"""SCPI: ROUTe:GSM:SIGNaling<Instance>:SCENario:IORI:FLEXible \n
		Snippet: value: FlexibleStruct = driver.route.scenario.iori.get_flexible() \n
		Activates the 'IQ out - RF in' scenario and selects the signal paths. For possible connector and converter values, see
		'Values for Signal Path Selection'. \n
			:return: structure: for return value, see the help for FlexibleStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:GSM:SIGNaling<Instance>:SCENario:IORI:FLEXible?', self.__class__.FlexibleStruct())

	def set_flexible(self, value: FlexibleStruct) -> None:
		"""SCPI: ROUTe:GSM:SIGNaling<Instance>:SCENario:IORI:FLEXible \n
		Snippet: driver.route.scenario.iori.set_flexible(value = FlexibleStruct()) \n
		Activates the 'IQ out - RF in' scenario and selects the signal paths. For possible connector and converter values, see
		'Values for Signal Path Selection'. \n
			:param value: see the help for FlexibleStruct structure arguments.
		"""
		self._core.io.write_struct('ROUTe:GSM:SIGNaling<Instance>:SCENario:IORI:FLEXible', value)
