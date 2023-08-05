from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Handover:
	"""Handover commands group definition. 22 total commands, 5 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("handover", core, parent)

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .Handover_.Catalog import Catalog
			self._catalog = Catalog(self._core, self._base)
		return self._catalog

	@property
	def channel(self):
		"""channel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_channel'):
			from .Handover_.Channel import Channel
			self._channel = Channel(self._core, self._base)
		return self._channel

	@property
	def level(self):
		"""level commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_level'):
			from .Handover_.Level import Level
			self._level = Level(self._core, self._base)
		return self._level

	@property
	def pswitched(self):
		"""pswitched commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_pswitched'):
			from .Handover_.Pswitched import Pswitched
			self._pswitched = Pswitched(self._core, self._base)
		return self._pswitched

	@property
	def external(self):
		"""external commands group. 0 Sub-classes, 7 commands."""
		if not hasattr(self, '_external'):
			from .Handover_.External import External
			self._external = External(self._core, self._base)
		return self._external

	def get_destination(self) -> str:
		"""SCPI: PREPare:GSM:SIGNaling<Instance>:HANDover:DESTination \n
		Snippet: value: str = driver.prepare.handover.get_destination() \n
		Selects the handover destination. A complete list of all supported values can be displayed using method RsCmwGsmSig.
		Prepare.Handover.Catalog.destination. \n
			:return: destination: Destination as string
		"""
		response = self._core.io.query_str_with_opc('PREPare:GSM:SIGNaling<Instance>:HANDover:DESTination?')
		return trim_str_response(response)

	def set_destination(self, destination: str) -> None:
		"""SCPI: PREPare:GSM:SIGNaling<Instance>:HANDover:DESTination \n
		Snippet: driver.prepare.handover.set_destination(destination = '1') \n
		Selects the handover destination. A complete list of all supported values can be displayed using method RsCmwGsmSig.
		Prepare.Handover.Catalog.destination. \n
			:param destination: Destination as string
		"""
		param = Conversions.value_to_quoted_str(destination)
		self._core.io.write_with_opc(f'PREPare:GSM:SIGNaling<Instance>:HANDover:DESTination {param}')

	# noinspection PyTypeChecker
	def get_mmode(self) -> enums.HandoverMode:
		"""SCPI: PREPare:GSM:SIGNaling<instance>:HANDover:MMODe \n
		Snippet: value: enums.HandoverMode = driver.prepare.handover.get_mmode() \n
		Selects the mechanism to be used for handover to another signaling application.
			INTRO_CMD_HELP: The flag is true (ON) in the following cases: \n
			- For CS connections are supported: Redirection, dual band intra-RAT handover, inter-RAT handover.
			- For PS connections are supported: dual band intra-RAT handover and cell change order. \n
			:return: mode: REDirection | DUALband | HANDover | CCORder Redirection, dual-band intra-RAT handover, inter-RAT handover, cell change order
		"""
		response = self._core.io.query_str('PREPare:GSM:SIGNaling<Instance>:HANDover:MMODe?')
		return Conversions.str_to_scalar_enum(response, enums.HandoverMode)

	def set_mmode(self, mode: enums.HandoverMode) -> None:
		"""SCPI: PREPare:GSM:SIGNaling<instance>:HANDover:MMODe \n
		Snippet: driver.prepare.handover.set_mmode(mode = enums.HandoverMode.CCORder) \n
		Selects the mechanism to be used for handover to another signaling application.
			INTRO_CMD_HELP: The flag is true (ON) in the following cases: \n
			- For CS connections are supported: Redirection, dual band intra-RAT handover, inter-RAT handover.
			- For PS connections are supported: dual band intra-RAT handover and cell change order. \n
			:param mode: REDirection | DUALband | HANDover | CCORder Redirection, dual-band intra-RAT handover, inter-RAT handover, cell change order
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.HandoverMode)
		self._core.io.write(f'PREPare:GSM:SIGNaling<Instance>:HANDover:MMODe {param}')

	# noinspection PyTypeChecker
	def get_target(self) -> enums.OperBandGsm:
		"""SCPI: PREPare:GSM:SIGNaling<Instance>:HANDover:TARGet \n
		Snippet: value: enums.OperBandGsm = driver.prepare.handover.get_target() \n
		Selects a handover destination band/network used for TCH/PDCH; see 'GSM Bands and Channels'. \n
			:return: band: G085 | G09 | G18 | G19 GSM 850, GSM 900, GSM 1800, GSM 1900
		"""
		response = self._core.io.query_str('PREPare:GSM:SIGNaling<Instance>:HANDover:TARGet?')
		return Conversions.str_to_scalar_enum(response, enums.OperBandGsm)

	def set_target(self, band: enums.OperBandGsm) -> None:
		"""SCPI: PREPare:GSM:SIGNaling<Instance>:HANDover:TARGet \n
		Snippet: driver.prepare.handover.set_target(band = enums.OperBandGsm.G04) \n
		Selects a handover destination band/network used for TCH/PDCH; see 'GSM Bands and Channels'. \n
			:param band: G085 | G09 | G18 | G19 GSM 850, GSM 900, GSM 1800, GSM 1900
		"""
		param = Conversions.enum_scalar_to_str(band, enums.OperBandGsm)
		self._core.io.write(f'PREPare:GSM:SIGNaling<Instance>:HANDover:TARGet {param}')

	def get_pcl(self) -> int:
		"""SCPI: PREPare:GSM:SIGNaling<Instance>:HANDover:PCL \n
		Snippet: value: int = driver.prepare.handover.get_pcl() \n
		Selects the PCL of the mobile in the destination GSM band. \n
			:return: pcl: Range: 0 to 31
		"""
		response = self._core.io.query_str('PREPare:GSM:SIGNaling<Instance>:HANDover:PCL?')
		return Conversions.str_to_int(response)

	def set_pcl(self, pcl: int) -> None:
		"""SCPI: PREPare:GSM:SIGNaling<Instance>:HANDover:PCL \n
		Snippet: driver.prepare.handover.set_pcl(pcl = 1) \n
		Selects the PCL of the mobile in the destination GSM band. \n
			:param pcl: Range: 0 to 31
		"""
		param = Conversions.decimal_value_to_str(pcl)
		self._core.io.write(f'PREPare:GSM:SIGNaling<Instance>:HANDover:PCL {param}')

	def get_tslot(self) -> int:
		"""SCPI: PREPare:GSM:SIGNaling<Instance>:HANDover:TSLot \n
		Snippet: value: int = driver.prepare.handover.get_tslot() \n
		Selects the timeslot for the circuit switched connection in the target GSM band. \n
			:return: slot: Range: 1 to 7
		"""
		response = self._core.io.query_str('PREPare:GSM:SIGNaling<Instance>:HANDover:TSLot?')
		return Conversions.str_to_int(response)

	def set_tslot(self, slot: int) -> None:
		"""SCPI: PREPare:GSM:SIGNaling<Instance>:HANDover:TSLot \n
		Snippet: driver.prepare.handover.set_tslot(slot = 1) \n
		Selects the timeslot for the circuit switched connection in the target GSM band. \n
			:param slot: Range: 1 to 7
		"""
		param = Conversions.decimal_value_to_str(slot)
		self._core.io.write(f'PREPare:GSM:SIGNaling<Instance>:HANDover:TSLot {param}')

	def clone(self) -> 'Handover':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Handover(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
