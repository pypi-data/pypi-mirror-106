from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup
from ..Internal.StructBase import StructBase
from ..Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sense:
	"""Sense commands group definition. 96 total commands, 10 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sense", core, parent)

	@property
	def band(self):
		"""band commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_band'):
			from .Sense_.Band import Band
			self._band = Band(self._core, self._base)
		return self._band

	@property
	def iqOut(self):
		"""iqOut commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqOut'):
			from .Sense_.IqOut import IqOut
			self._iqOut = IqOut(self._core, self._base)
		return self._iqOut

	@property
	def connection(self):
		"""connection commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_connection'):
			from .Sense_.Connection import Connection
			self._connection = Connection(self._core, self._base)
		return self._connection

	@property
	def mssInfo(self):
		"""mssInfo commands group. 6 Sub-classes, 9 commands."""
		if not hasattr(self, '_mssInfo'):
			from .Sense_.MssInfo import MssInfo
			self._mssInfo = MssInfo(self._core, self._base)
		return self._mssInfo

	@property
	def cell(self):
		"""cell commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_cell'):
			from .Sense_.Cell import Cell
			self._cell = Cell(self._core, self._base)
		return self._cell

	@property
	def rreport(self):
		"""rreport commands group. 12 Sub-classes, 1 commands."""
		if not hasattr(self, '_rreport'):
			from .Sense_.Rreport import Rreport
			self._rreport = Rreport(self._core, self._base)
		return self._rreport

	@property
	def sms(self):
		"""sms commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_sms'):
			from .Sense_.Sms import Sms
			self._sms = Sms(self._core, self._base)
		return self._sms

	@property
	def ber(self):
		"""ber commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ber'):
			from .Sense_.Ber import Ber
			self._ber = Ber(self._core, self._base)
		return self._ber

	@property
	def rfSettings(self):
		"""rfSettings commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_rfSettings'):
			from .Sense_.RfSettings import RfSettings
			self._rfSettings = RfSettings(self._core, self._base)
		return self._rfSettings

	@property
	def elog(self):
		"""elog commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_elog'):
			from .Sense_.Elog import Elog
			self._elog = Elog(self._core, self._base)
		return self._elog

	# noinspection PyTypeChecker
	class CvInfoStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Loopback_Delay: float: Time delay measured during the loopback connection Range: 0 s to 10 s , Unit: s
			- Dl_Encoder_Delay: float: Encoder time delay in downlink measured during the connection to the speech codec board Range: 0 s to 10 s , Unit: s
			- Ul_Decoder_Delay: float: Decoder time delay in uplink measured during the connection to the speech codec board Range: 0 s to 10 s , Unit: s"""
		__meta_args_list = [
			ArgStruct.scalar_float('Loopback_Delay'),
			ArgStruct.scalar_float('Dl_Encoder_Delay'),
			ArgStruct.scalar_float('Ul_Decoder_Delay')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Loopback_Delay: float = None
			self.Dl_Encoder_Delay: float = None
			self.Ul_Decoder_Delay: float = None

	def get_cv_info(self) -> CvInfoStruct:
		"""SCPI: SENSe:GSM:SIGNaling<instance>:CVINfo \n
		Snippet: value: CvInfoStruct = driver.sense.get_cv_info() \n
		Displays the time delay of the voice connection. \n
			:return: structure: for return value, see the help for CvInfoStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:GSM:SIGNaling<Instance>:CVINfo?', self.__class__.CvInfoStruct())

	def clone(self) -> 'Sense':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sense(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
