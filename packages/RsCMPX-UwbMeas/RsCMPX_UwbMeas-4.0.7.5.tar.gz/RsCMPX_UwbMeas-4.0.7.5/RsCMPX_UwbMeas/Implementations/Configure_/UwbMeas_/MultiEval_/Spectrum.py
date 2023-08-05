from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Spectrum:
	"""Spectrum commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("spectrum", core, parent)

	def get_scount(self) -> int:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:SPECtrum:SCOunt \n
		Snippet: value: int = driver.configure.uwbMeas.multiEval.spectrum.get_scount() \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. The statistic count applies to spectrum measurements. \n
			:return: statistic_count: No help available
		"""
		response = self._core.io.query_str('CONFigure:UWB:MEASurement<Instance>:MEValuation:SPECtrum:SCOunt?')
		return Conversions.str_to_int(response)

	def set_scount(self, statistic_count: int) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:SPECtrum:SCOunt \n
		Snippet: driver.configure.uwbMeas.multiEval.spectrum.set_scount(statistic_count = 1) \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. The statistic count applies to spectrum measurements. \n
			:param statistic_count: No help available
		"""
		param = Conversions.decimal_value_to_str(statistic_count)
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:SPECtrum:SCOunt {param}')
