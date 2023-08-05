from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Extreme:
	"""Extreme commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("extreme", core, parent)

	def fetch(self) -> float:
		"""SCPI: FETCh:UWB:MEASurement<Instance>:MEValuation:MODulation:CTJittter:EXTReme \n
		Snippet: value: float = driver.uwbMeas.multiEval.modulation.ctJitter.extreme.fetch() \n
		Returns the RMS time jitter value averaged over all chips of the detected preamble symbols for the selected packet number
		<PPDU>. \n
		Suppressed linked return values: reliability \n
			:return: jitter: Chip time jitter"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:UWB:MEASurement<Instance>:MEValuation:MODulation:CTJittter:EXTReme?', suppressed)
		return Conversions.str_to_float(response)

	def read(self) -> float:
		"""SCPI: READ:UWB:MEASurement<Instance>:MEValuation:MODulation:CTJittter:EXTReme \n
		Snippet: value: float = driver.uwbMeas.multiEval.modulation.ctJitter.extreme.read() \n
		Returns the RMS time jitter value averaged over all chips of the detected preamble symbols for the selected packet number
		<PPDU>. \n
		Suppressed linked return values: reliability \n
			:return: jitter: Chip time jitter"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'READ:UWB:MEASurement<Instance>:MEValuation:MODulation:CTJittter:EXTReme?', suppressed)
		return Conversions.str_to_float(response)
