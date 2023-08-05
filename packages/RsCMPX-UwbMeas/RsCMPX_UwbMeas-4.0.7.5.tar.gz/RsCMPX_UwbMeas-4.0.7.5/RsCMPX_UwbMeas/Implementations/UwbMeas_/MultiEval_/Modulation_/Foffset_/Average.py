from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Average:
	"""Average commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("average", core, parent)

	def fetch(self) -> float:
		"""SCPI: FETCh:UWB:MEASurement<Instance>:MEValuation:MODulation:FOFFset:AVERage \n
		Snippet: value: float = driver.uwbMeas.multiEval.modulation.foffset.average.fetch() \n
		Returns the frequency error relative to the channel center frequency in ppm for the selected packet number <PPDU>. \n
		Suppressed linked return values: reliability \n
			:return: offset: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:UWB:MEASurement<Instance>:MEValuation:MODulation:FOFFset:AVERage?', suppressed)
		return Conversions.str_to_float(response)

	def read(self) -> float:
		"""SCPI: READ:UWB:MEASurement<Instance>:MEValuation:MODulation:FOFFset:AVERage \n
		Snippet: value: float = driver.uwbMeas.multiEval.modulation.foffset.average.read() \n
		Returns the frequency error relative to the channel center frequency in ppm for the selected packet number <PPDU>. \n
		Suppressed linked return values: reliability \n
			:return: offset: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'READ:UWB:MEASurement<Instance>:MEValuation:MODulation:FOFFset:AVERage?', suppressed)
		return Conversions.str_to_float(response)

	# noinspection PyTypeChecker
	def calculate(self) -> enums.ResultStatus2:
		"""SCPI: CALCulate:UWB:MEASurement<Instance>:MEValuation:MODulation:FOFFset:AVERage \n
		Snippet: value: enums.ResultStatus2 = driver.uwbMeas.multiEval.modulation.foffset.average.calculate() \n
		Returns the frequency error relative to the channel center frequency in ppm for the selected packet number <PPDU>. \n
		Suppressed linked return values: reliability \n
			:return: offset: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'CALCulate:UWB:MEASurement<Instance>:MEValuation:MODulation:FOFFset:AVERage?', suppressed)
		return Conversions.str_to_scalar_enum(response, enums.ResultStatus2)
