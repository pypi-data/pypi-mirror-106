from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Batch:
	"""Batch commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("batch", core, parent)

	# noinspection PyTypeChecker
	class FlexibleStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Bb_Board: enums.BbBoard: Signaling unit
			- Rx_Connector: enums.RxConnector: RF connector for the input path
			- Rx_Converter: enums.RxConverter: RX module for the input path
			- Tx_Connector: enums.TxConnector: RF connector for the first output path, used for TCH/PDCH
			- Tx_Converter: enums.TxConverter: TX module for the first output path. Select different modules for the two paths.
			- Tx_2_Connector: enums.TxConnector: RF connector for the second output path, used for BCCH
			- Tx_2_Converter: enums.TxConverter: TX module for the second output path. Select different modules for the two paths."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Bb_Board', enums.BbBoard),
			ArgStruct.scalar_enum('Rx_Connector', enums.RxConnector),
			ArgStruct.scalar_enum('Rx_Converter', enums.RxConverter),
			ArgStruct.scalar_enum('Tx_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_Converter', enums.TxConverter),
			ArgStruct.scalar_enum('Tx_2_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_2_Converter', enums.TxConverter)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Bb_Board: enums.BbBoard = None
			self.Rx_Connector: enums.RxConnector = None
			self.Rx_Converter: enums.RxConverter = None
			self.Tx_Connector: enums.TxConnector = None
			self.Tx_Converter: enums.TxConverter = None
			self.Tx_2_Connector: enums.TxConnector = None
			self.Tx_2_Converter: enums.TxConverter = None

	# noinspection PyTypeChecker
	def get_flexible(self) -> FlexibleStruct:
		"""SCPI: ROUTe:GSM:SIGNaling<Instance>:SCENario:BATCh:FLEXible \n
		Snippet: value: FlexibleStruct = driver.route.scenario.batch.get_flexible() \n
		Activates the scenario 'BCCH and TCH/PDCH' and selects the signal paths. For possible connector and converter values, see
		'Values for Signal Path Selection'. \n
			:return: structure: for return value, see the help for FlexibleStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:GSM:SIGNaling<Instance>:SCENario:BATCh:FLEXible?', self.__class__.FlexibleStruct())

	def set_flexible(self, value: FlexibleStruct) -> None:
		"""SCPI: ROUTe:GSM:SIGNaling<Instance>:SCENario:BATCh:FLEXible \n
		Snippet: driver.route.scenario.batch.set_flexible(value = FlexibleStruct()) \n
		Activates the scenario 'BCCH and TCH/PDCH' and selects the signal paths. For possible connector and converter values, see
		'Values for Signal Path Selection'. \n
			:param value: see the help for FlexibleStruct structure arguments.
		"""
		self._core.io.write_struct('ROUTe:GSM:SIGNaling<Instance>:SCENario:BATCh:FLEXible', value)
