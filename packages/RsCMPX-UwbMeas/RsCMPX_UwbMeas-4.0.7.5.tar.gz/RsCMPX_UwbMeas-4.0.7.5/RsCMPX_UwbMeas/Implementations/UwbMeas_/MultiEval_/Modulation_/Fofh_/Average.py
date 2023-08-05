from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Average:
	"""Average commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("average", core, parent)

	def fetch(self) -> float:
		"""SCPI: FETCh:UWB:MEASurement<Instance>:MEValuation:MODulation:FOFH:AVERage \n
		Snippet: value: float = driver.uwbMeas.multiEval.modulation.fofh.average.fetch() \n
		Returns the frequency error relative to the channel center frequency in Hz for the selected packet number <PPDU>. \n
		Suppressed linked return values: reliability \n
			:return: offset: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:UWB:MEASurement<Instance>:MEValuation:MODulation:FOFH:AVERage?', suppressed)
		return Conversions.str_to_float(response)

	def read(self) -> float:
		"""SCPI: READ:UWB:MEASurement<Instance>:MEValuation:MODulation:FOFH:AVERage \n
		Snippet: value: float = driver.uwbMeas.multiEval.modulation.fofh.average.read() \n
		Returns the frequency error relative to the channel center frequency in Hz for the selected packet number <PPDU>. \n
		Suppressed linked return values: reliability \n
			:return: offset: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'READ:UWB:MEASurement<Instance>:MEValuation:MODulation:FOFH:AVERage?', suppressed)
		return Conversions.str_to_float(response)
