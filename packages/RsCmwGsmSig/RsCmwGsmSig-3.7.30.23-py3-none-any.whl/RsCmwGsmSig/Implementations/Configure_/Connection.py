from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Connection:
	"""Connection commands group definition. 72 total commands, 3 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("connection", core, parent)

	@property
	def cswitched(self):
		"""cswitched commands group. 3 Sub-classes, 12 commands."""
		if not hasattr(self, '_cswitched'):
			from .Connection_.Cswitched import Cswitched
			self._cswitched = Cswitched(self._core, self._base)
		return self._cswitched

	@property
	def pswitched(self):
		"""pswitched commands group. 4 Sub-classes, 11 commands."""
		if not hasattr(self, '_pswitched'):
			from .Connection_.Pswitched import Pswitched
			self._pswitched = Pswitched(self._core, self._base)
		return self._pswitched

	@property
	def foffset(self):
		"""foffset commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_foffset'):
			from .Connection_.Foffset import Foffset
			self._foffset = Foffset(self._core, self._base)
		return self._foffset

	def get_as_config(self) -> bool:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:ASConfig \n
		Snippet: value: bool = driver.configure.connection.get_as_config() \n
		Enables/disables the automatic setting of the PS parameters in 'Slot Configuration Dialog'. \n
			:return: auto_slot_config: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:ASConfig?')
		return Conversions.str_to_bool(response)

	def set_as_config(self, auto_slot_config: bool) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:ASConfig \n
		Snippet: driver.configure.connection.set_as_config(auto_slot_config = False) \n
		Enables/disables the automatic setting of the PS parameters in 'Slot Configuration Dialog'. \n
			:param auto_slot_config: OFF | ON
		"""
		param = Conversions.bool_to_str(auto_slot_config)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:ASConfig {param}')

	def get_ds_config(self) -> bool:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:DSConfig \n
		Snippet: value: bool = driver.configure.connection.get_ds_config() \n
		Enables/disables the automatic setting of the PS parameters in 'Slot Configuration Dialog' for dual transfer mode. \n
			:return: dtm_slot_config: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:DSConfig?')
		return Conversions.str_to_bool(response)

	def set_ds_config(self, dtm_slot_config: bool) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:DSConfig \n
		Snippet: driver.configure.connection.set_ds_config(dtm_slot_config = False) \n
		Enables/disables the automatic setting of the PS parameters in 'Slot Configuration Dialog' for dual transfer mode. \n
			:param dtm_slot_config: OFF | ON
		"""
		param = Conversions.bool_to_str(dtm_slot_config)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:DSConfig {param}')

	def get_tadvance(self) -> int:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:TADVance \n
		Snippet: value: int = driver.configure.connection.get_tadvance() \n
		Specifies the value which the MS uses to advance its UL timing. \n
			:return: timing_advance: Range: 0 to 63
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:TADVance?')
		return Conversions.str_to_int(response)

	def set_tadvance(self, timing_advance: int) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:TADVance \n
		Snippet: driver.configure.connection.set_tadvance(timing_advance = 1) \n
		Specifies the value which the MS uses to advance its UL timing. \n
			:param timing_advance: Range: 0 to 63
		"""
		param = Conversions.decimal_value_to_str(timing_advance)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:TADVance {param}')

	def get_rf_offset(self) -> bool:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:RFOFfset \n
		Snippet: value: bool = driver.configure.connection.get_rf_offset() \n
		Enables random frequency offset for the traffic channel. The R&S CMW randomly applies the positive and negative frequency
		offset. \n
			:return: random_frq_offset: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:RFOFfset?')
		return Conversions.str_to_bool(response)

	def set_rf_offset(self, random_frq_offset: bool) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:RFOFfset \n
		Snippet: driver.configure.connection.set_rf_offset(random_frq_offset = False) \n
		Enables random frequency offset for the traffic channel. The R&S CMW randomly applies the positive and negative frequency
		offset. \n
			:param random_frq_offset: OFF | ON
		"""
		param = Conversions.bool_to_str(random_frq_offset)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:RFOFfset {param}')

	def clone(self) -> 'Connection':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Connection(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
