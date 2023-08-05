from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hrate:
	"""Hrate commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("hrate", core, parent)

	# noinspection PyTypeChecker
	def get_gmsk(self) -> List[enums.NbCodec]:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:AMR:RSET:NB:HRATe:GMSK \n
		Snippet: value: List[enums.NbCodec] = driver.configure.connection.cswitched.amr.rset.nb.hrate.get_gmsk() \n
		Configures up to four supported modes for the half-rate narrowband AMR codec (GMSK modulation) , i.e. assigns data rates
		to the modes. The selected data rates must be different. They are automatically sorted so that rate (mode 4) > rate (mode
		3) > rate (mode 2) > rate (mode 1) . You can deactivate modes (OFF) to restrict the test model to less than 4 supported
		modes. \n
			:return: codec_mode: C0475 | C0515 | C0590 | C0670 | C0740 | C0795 | ON | OFF Comma-separated list of 4 values: data rates for mode 4 to 1 4.75 kbit/s, 5.15 kbit/s, 5.90 kbit/s, 6.70 kbit/s, 7.40 kbit/s, or 7.95 kbit/s, additional OFF (ON) disables (enables) codec mode.
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:AMR:RSET:NB:HRATe:GMSK?')
		return Conversions.str_to_list_enum(response, enums.NbCodec)

	def set_gmsk(self, codec_mode: List[enums.NbCodec]) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:AMR:RSET:NB:HRATe:GMSK \n
		Snippet: driver.configure.connection.cswitched.amr.rset.nb.hrate.set_gmsk(codec_mode = [NbCodec.C0475, NbCodec.ON]) \n
		Configures up to four supported modes for the half-rate narrowband AMR codec (GMSK modulation) , i.e. assigns data rates
		to the modes. The selected data rates must be different. They are automatically sorted so that rate (mode 4) > rate (mode
		3) > rate (mode 2) > rate (mode 1) . You can deactivate modes (OFF) to restrict the test model to less than 4 supported
		modes. \n
			:param codec_mode: C0475 | C0515 | C0590 | C0670 | C0740 | C0795 | ON | OFF Comma-separated list of 4 values: data rates for mode 4 to 1 4.75 kbit/s, 5.15 kbit/s, 5.90 kbit/s, 6.70 kbit/s, 7.40 kbit/s, or 7.95 kbit/s, additional OFF (ON) disables (enables) codec mode.
		"""
		param = Conversions.enum_list_to_str(codec_mode, enums.NbCodec)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:AMR:RSET:NB:HRATe:GMSK {param}')

	# noinspection PyTypeChecker
	def get_epsk(self) -> List[enums.NbCodec]:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:AMR:RSET:NB:HRATe:EPSK \n
		Snippet: value: List[enums.NbCodec] = driver.configure.connection.cswitched.amr.rset.nb.hrate.get_epsk() \n
		Configures up to four supported modes for the half-rate narrowband AMR codec (8PSK modulation) , i.e. assigns data rates
		to the modes. The four data rates must be different from each other. They are automatically sorted in descending order so
		that rate (mode 4) > rate (mode 3) > rate (mode 2) > rate (mode 1) . You can deactivate modes (OFF) to restrict the test
		model to less than 4 supported modes. \n
			:return: codec_mode: C0475 | C0515 | C0590 | C0670 | C0740 | C0795 | C1020 | C1220 | ON | OFF Comma-separated list of 4 values: data rates for mode 4 to 1 4.75 kbit/s, 5.15 kbit/s, 5.90 kbit/s, 6.70 kbit/s, 7.40 kbit/s, 7.95 kbit/s, 10.20 kbit/s, or 12.20 kbit/s, additional OFF (ON) disables (enables) codec mode.
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:AMR:RSET:NB:HRATe:EPSK?')
		return Conversions.str_to_list_enum(response, enums.NbCodec)

	def set_epsk(self, codec_mode: List[enums.NbCodec]) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:AMR:RSET:NB:HRATe:EPSK \n
		Snippet: driver.configure.connection.cswitched.amr.rset.nb.hrate.set_epsk(codec_mode = [NbCodec.C0475, NbCodec.ON]) \n
		Configures up to four supported modes for the half-rate narrowband AMR codec (8PSK modulation) , i.e. assigns data rates
		to the modes. The four data rates must be different from each other. They are automatically sorted in descending order so
		that rate (mode 4) > rate (mode 3) > rate (mode 2) > rate (mode 1) . You can deactivate modes (OFF) to restrict the test
		model to less than 4 supported modes. \n
			:param codec_mode: C0475 | C0515 | C0590 | C0670 | C0740 | C0795 | C1020 | C1220 | ON | OFF Comma-separated list of 4 values: data rates for mode 4 to 1 4.75 kbit/s, 5.15 kbit/s, 5.90 kbit/s, 6.70 kbit/s, 7.40 kbit/s, 7.95 kbit/s, 10.20 kbit/s, or 12.20 kbit/s, additional OFF (ON) disables (enables) codec mode.
		"""
		param = Conversions.enum_list_to_str(codec_mode, enums.NbCodec)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:CONNection:CSWitched:AMR:RSET:NB:HRATe:EPSK {param}')
