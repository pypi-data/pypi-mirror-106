from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Average:
	"""Average commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("average", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:UWB:MEASurement<Instance>:MEValuation:TRACe:TSMask:AVERage \n
		Snippet: value: List[float] = driver.uwbMeas.multiEval.trace.tsMask.average.fetch() \n
		Returns the values of the transmit spectrum trace. The current and average values can be retrieved. See also 'Square
		Transmit Spectrum Mask'. \n
		Suppressed linked return values: reliability \n
			:return: ratio: Comma-separated list of transmit spectrum values."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:UWB:MEASurement<Instance>:MEValuation:TRACe:TSMask:AVERage?', suppressed)
		return response

	def read(self) -> List[float]:
		"""SCPI: READ:UWB:MEASurement<Instance>:MEValuation:TRACe:TSMask:AVERage \n
		Snippet: value: List[float] = driver.uwbMeas.multiEval.trace.tsMask.average.read() \n
		Returns the values of the transmit spectrum trace. The current and average values can be retrieved. See also 'Square
		Transmit Spectrum Mask'. \n
		Suppressed linked return values: reliability \n
			:return: ratio: Comma-separated list of transmit spectrum values."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:UWB:MEASurement<Instance>:MEValuation:TRACe:TSMask:AVERage?', suppressed)
		return response
