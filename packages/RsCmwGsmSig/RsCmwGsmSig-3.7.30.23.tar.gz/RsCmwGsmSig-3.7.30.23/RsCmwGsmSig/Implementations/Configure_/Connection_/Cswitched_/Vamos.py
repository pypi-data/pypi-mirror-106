from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Vamos:
	"""Vamos commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("vamos", core, parent)

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:VAMos:ENABle \n
		Snippet: value: bool = driver.configure.connection.cswitched.vamos.get_enable() \n
		Activates or deactivates voice services over adaptive multi-user channels on one slot (VAMOS) . \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:VAMos:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:VAMos:ENABle \n
		Snippet: driver.configure.connection.cswitched.vamos.set_enable(enable = False) \n
		Activates or deactivates voice services over adaptive multi-user channels on one slot (VAMOS) . \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:VAMos:ENABle {param}')

	# noinspection PyTypeChecker
	def get_ms_level(self) -> enums.VamosMode:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:VAMos:MSLevel \n
		Snippet: value: enums.VamosMode = driver.configure.connection.cswitched.vamos.get_ms_level() \n
		Selects the VAMOS support level of the mobile. \n
			:return: mode: AUTO | VAM1 | VAM2 AUTO: according to the reported MS capabilities VAM1: VAMOS support level I VAM2: VAMOS support level II
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:VAMos:MSLevel?')
		return Conversions.str_to_scalar_enum(response, enums.VamosMode)

	def set_ms_level(self, mode: enums.VamosMode) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:VAMos:MSLevel \n
		Snippet: driver.configure.connection.cswitched.vamos.set_ms_level(mode = enums.VamosMode.AUTO) \n
		Selects the VAMOS support level of the mobile. \n
			:param mode: AUTO | VAM1 | VAM2 AUTO: according to the reported MS capabilities VAM1: VAMOS support level I VAM2: VAMOS support level II
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.VamosMode)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:VAMos:MSLevel {param}')

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Sub_Channel: int: VAMOS subchannel to be used for the DUT (active subchannel) Range: 0 to 1
			- Tsc_Active_Subch: int: TSC to be used for the DUT (active subchannel) Range: 0 to 7
			- Tsc_Set_Act_Subch: int: TSC set to be used for the DUT (active subchannel) Range: 1 to 2
			- Tsc_Other_Subch: int: TSC to be used for the virtual second VAMOS user (other subchannel) Range: 0 to 7
			- Tsc_Set_Oth_Subch: int: TSC set to be used for the virtual second VAMOS user (other subchannel) Range: 1 to 2
			- Subch_Pow_Imb_Rat: float: Subchannel power imbalance ratio, i.e. power of VAMOS subchannel 0 relative to subchannel 1 Range: -15 dB to 15 dB, Unit: dB
			- Profile: enums.Profile: SUSer | TUSer | TUDTx | ON | OFF VAMOS profile, determines that the DL signal is generated for: SUSer: Single VAMOS user. There is no second VAMOS user (not even in DTX mode) . TUSer: Two active VAMOS users. The downlink signal contains speech frames and signaling data for both users. TUDTx: Two VAMOS users, DUT active, second user in DTX mode. The downlink signal contains speech frames for the DUT only. For the virtual user DTX is transmitted. OFF (ON) disables (enables) the profile."""
		__meta_args_list = [
			ArgStruct.scalar_int('Sub_Channel'),
			ArgStruct.scalar_int('Tsc_Active_Subch'),
			ArgStruct.scalar_int('Tsc_Set_Act_Subch'),
			ArgStruct.scalar_int('Tsc_Other_Subch'),
			ArgStruct.scalar_int('Tsc_Set_Oth_Subch'),
			ArgStruct.scalar_float('Subch_Pow_Imb_Rat'),
			ArgStruct.scalar_enum('Profile', enums.Profile)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Sub_Channel: int = None
			self.Tsc_Active_Subch: int = None
			self.Tsc_Set_Act_Subch: int = None
			self.Tsc_Other_Subch: int = None
			self.Tsc_Set_Oth_Subch: int = None
			self.Subch_Pow_Imb_Rat: float = None
			self.Profile: enums.Profile = None

	def get_value(self) -> ValueStruct:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:VAMos \n
		Snippet: value: ValueStruct = driver.configure.connection.cswitched.vamos.get_value() \n
		Configures VAMOS. For background information, see 'VAMOS'. \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:VAMos?', self.__class__.ValueStruct())

	def set_value(self, value: ValueStruct) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:VAMos \n
		Snippet: driver.configure.connection.cswitched.vamos.set_value(value = ValueStruct()) \n
		Configures VAMOS. For background information, see 'VAMOS'. \n
			:param value: see the help for ValueStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:VAMos', value)
