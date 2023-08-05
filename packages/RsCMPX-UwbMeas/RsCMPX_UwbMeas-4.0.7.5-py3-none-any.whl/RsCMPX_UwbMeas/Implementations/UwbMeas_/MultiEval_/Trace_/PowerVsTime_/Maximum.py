from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Maximum:
	"""Maximum commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("maximum", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:UWB:MEASurement<Instance>:MEValuation:TRACe:PVTime:MAXimum \n
		Snippet: value: List[float] = driver.uwbMeas.multiEval.trace.powerVsTime.maximum.fetch() \n
		Returns the preamble power values over time. The minimum and maximum values can be retrieved. See also 'Square Power
		Versus Time'. \n
		Suppressed linked return values: reliability \n
			:return: power: Comma-separated list of preamble power values."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:UWB:MEASurement<Instance>:MEValuation:TRACe:PVTime:MAXimum?', suppressed)
		return response

	def read(self) -> List[float]:
		"""SCPI: READ:UWB:MEASurement<Instance>:MEValuation:TRACe:PVTime:MAXimum \n
		Snippet: value: List[float] = driver.uwbMeas.multiEval.trace.powerVsTime.maximum.read() \n
		Returns the preamble power values over time. The minimum and maximum values can be retrieved. See also 'Square Power
		Versus Time'. \n
		Suppressed linked return values: reliability \n
			:return: power: Comma-separated list of preamble power values."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:UWB:MEASurement<Instance>:MEValuation:TRACe:PVTime:MAXimum?', suppressed)
		return response
