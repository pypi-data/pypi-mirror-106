from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Carrier:
	"""Carrier commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: Carrier, default value after init: Carrier.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("carrier", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_carrier_get', 'repcap_carrier_set', repcap.Carrier.Nr1)

	def repcap_carrier_set(self, enum_value: repcap.Carrier) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Carrier.Default
		Default value after init: Carrier.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_carrier_get(self) -> repcap.Carrier:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	# noinspection PyTypeChecker
	class CarrierStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Enable_Dl: List[bool]: OFF | ON List of 8 values for downlink slot 0 to 7, specifying for each slot whether the MS has to listen to a signal in the slot. Timeslot 0 cannot be enabled (always OFF) .
			- Level_Dl: List[float or bool]: ON | OFF List of 8 signal levels for downlink slot 0 to 7, defining the downlink signal level relative to the reference level Option R&S CMW-KS210 is required to modify this setting. Without the option, only KEEP is allowed. Range: -40 dB to 0 dB, Unit: dB Additional parameters: OFF | ON (disables | enables DL signal transmission using the previous/default power values)
			- Coding_Scheme_Dl: List[enums.CodingSchemeDownlink]: C1 | C2 | C3 | C4 | MC1 | MC2 | MC3 | MC4 | MC5 | MC6 | MC7 | MC8 | MC9 | DA5 | DA6 | DA7 | DA8 | DA9 | DA10 | DA11 | DA12 List of 8 coding schemes for downlink slot 0 to 7. All 8 values must be identical. In the current software version, the same value applies to all downlink slots and to both carriers. The value must be compatible to the configured TBF level, see [CMDLINK: CONFigure:GSM:SIGNi:CONNection:PSWitched:TLEVel CMDLINK]. C1 to C4: CS-1 to CS-4 MC1 to MC9: MCS-1 to MCS-9 DA5 to DA12: DAS-5 to DAS-12
			- Enable_Ul: List[bool]: OFF | ON List of 8 values enabling/disabling uplink slot 0 to 7 Timeslot 0 cannot be enabled (always OFF) .
			- Gamma_Ul: List[int]: List of 8 gamma values for uplink slot 0 to 7, specifying the power control parameter ΓCH Range: 0 to 31
			- Coding_Scheme_Ul: enums.CodingSchemeUplink: C1 | C2 | C3 | C4 | MC1 | MC2 | MC3 | MC4 | MC5 | MC6 | MC7 | MC8 | MC9 | UA7 | UA8 | UA9 | UA10 | UA11 Coding scheme for uplink packet data channels. The value must be compatible to the configured TBF level, see [CMDLINK: CONFigure:GSM:SIGNi:CONNection:PSWitched:TLEVel CMDLINK]. C1 to C4: CS-1 to CS-4 MC1 to MC9: MCS-1 to MCS-9 UA7 to UA11: UAS-7 to UAS-11
			- Channel: int: GSM channel number for TCH and PDCH. The range of values depends on the selected band; for an overview see 'GSM Bands and Channels'. The values below are for GSM 900. Range: 1 to 124, 940 to 1023"""
		__meta_args_list = [
			ArgStruct('Enable_Dl', DataType.BooleanList, None, False, False, 8),
			ArgStruct('Level_Dl', DataType.FloatList, None, False, False, 8),
			ArgStruct('Coding_Scheme_Dl', DataType.EnumList, enums.CodingSchemeDownlink, False, False, 8),
			ArgStruct('Enable_Ul', DataType.BooleanList, None, False, False, 8),
			ArgStruct('Gamma_Ul', DataType.IntegerList, None, False, False, 8),
			ArgStruct.scalar_enum('Coding_Scheme_Ul', enums.CodingSchemeUplink),
			ArgStruct.scalar_int('Channel')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable_Dl: List[bool] = None
			self.Level_Dl: List[float or bool] = None
			self.Coding_Scheme_Dl: List[enums.CodingSchemeDownlink] = None
			self.Enable_Ul: List[bool] = None
			self.Gamma_Ul: List[int] = None
			self.Coding_Scheme_Ul: enums.CodingSchemeUplink = None
			self.Channel: int = None

	def set(self, structure: CarrierStruct, carrier=repcap.Carrier.Default) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:SCONfig:COMBined:CARRier<Carrier> \n
		Snippet: driver.configure.connection.pswitched.sconfig.combined.carrier.set(value = [PROPERTY_STRUCT_NAME](), carrier = repcap.Carrier.Default) \n
		Specifies most slot configuration parameters and some other important packet switched connection parameters. This command
		is especially useful for consistent and efficient reconfiguration in state 'TBF Established'. It combines several
		alternative commands into a single command. \n
			:param structure: for set value, see the help for CarrierStruct structure arguments.
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')"""
		carrier_cmd_val = self._base.get_repcap_cmd_value(carrier, repcap.Carrier)
		self._core.io.write_struct(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:SCONfig:COMBined:CARRier{carrier_cmd_val}', structure)

	def get(self, carrier=repcap.Carrier.Default) -> CarrierStruct:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:SCONfig:COMBined:CARRier<Carrier> \n
		Snippet: value: CarrierStruct = driver.configure.connection.pswitched.sconfig.combined.carrier.get(carrier = repcap.Carrier.Default) \n
		Specifies most slot configuration parameters and some other important packet switched connection parameters. This command
		is especially useful for consistent and efficient reconfiguration in state 'TBF Established'. It combines several
		alternative commands into a single command. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: structure: for return value, see the help for CarrierStruct structure arguments."""
		carrier_cmd_val = self._base.get_repcap_cmd_value(carrier, repcap.Carrier)
		return self._core.io.query_struct(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:PSWitched:SCONfig:COMBined:CARRier{carrier_cmd_val}?', self.__class__.CarrierStruct())

	def clone(self) -> 'Carrier':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Carrier(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
