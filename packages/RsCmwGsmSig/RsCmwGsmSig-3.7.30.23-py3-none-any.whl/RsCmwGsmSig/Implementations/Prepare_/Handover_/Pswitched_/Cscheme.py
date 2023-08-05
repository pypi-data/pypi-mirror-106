from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cscheme:
	"""Cscheme commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cscheme", core, parent)

	@property
	def downlink(self):
		"""downlink commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_downlink'):
			from .Cscheme_.Downlink import Downlink
			self._downlink = Downlink(self._core, self._base)
		return self._downlink

	# noinspection PyTypeChecker
	def get_uplink(self) -> enums.UplinkCodingScheme:
		"""SCPI: PREPare:GSM:SIGNaling<Instance>:HANDover:PSWitched:CSCHeme:UL \n
		Snippet: value: enums.UplinkCodingScheme = driver.prepare.handover.pswitched.cscheme.get_uplink() \n
		Specifies the coding scheme for all uplink timeslots in the destination GSM band (packet switched domain, one value) .
		The selected values must be compatible to the configured TBF level, see method RsCmwGsmSig.Configure.Connection.Pswitched.
		tlevel. \n
			:return: coding_scheme: C1 | C2 | C3 | C4 | MC1 | MC2 | MC3 | MC4 | MC5 | MC6 | MC7 | MC8 | MC9 | UA7 | UA8 | UA9 | UA10 | UA11 | ON | OFF Coding scheme for all UL slots C1 to C4: CS-1 to CS-4 MC1 to MC9: MCS-1 to MCS-9 UA7 to UA11: UAS-7 to UAS-9 OFF (ON) disables (enables) the coding scheme
		"""
		response = self._core.io.query_str_with_opc('PREPare:GSM:SIGNaling<Instance>:HANDover:PSWitched:CSCHeme:UL?')
		return Conversions.str_to_scalar_enum(response, enums.UplinkCodingScheme)

	def set_uplink(self, coding_scheme: enums.UplinkCodingScheme) -> None:
		"""SCPI: PREPare:GSM:SIGNaling<Instance>:HANDover:PSWitched:CSCHeme:UL \n
		Snippet: driver.prepare.handover.pswitched.cscheme.set_uplink(coding_scheme = enums.UplinkCodingScheme.C1) \n
		Specifies the coding scheme for all uplink timeslots in the destination GSM band (packet switched domain, one value) .
		The selected values must be compatible to the configured TBF level, see method RsCmwGsmSig.Configure.Connection.Pswitched.
		tlevel. \n
			:param coding_scheme: C1 | C2 | C3 | C4 | MC1 | MC2 | MC3 | MC4 | MC5 | MC6 | MC7 | MC8 | MC9 | UA7 | UA8 | UA9 | UA10 | UA11 | ON | OFF Coding scheme for all UL slots C1 to C4: CS-1 to CS-4 MC1 to MC9: MCS-1 to MCS-9 UA7 to UA11: UAS-7 to UAS-9 OFF (ON) disables (enables) the coding scheme
		"""
		param = Conversions.enum_scalar_to_str(coding_scheme, enums.UplinkCodingScheme)
		self._core.io.write_with_opc(f'PREPare:GSM:SIGNaling<Instance>:HANDover:PSWitched:CSCHeme:UL {param}')

	def clone(self) -> 'Cscheme':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cscheme(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
