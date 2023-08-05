from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StandardDev:
	"""StandardDev commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("standardDev", core, parent)

	def fetch(self) -> float:
		"""SCPI: FETCh:UWB:MEASurement<Instance>:MEValuation:POWer:PPPower:SDEViation \n
		Snippet: value: float = driver.uwbMeas.multiEval.power.ppPower.standardDev.fetch() \n
		Returns the value of the preamble peak power for the selected packet number <PPDU>. \n
		Suppressed linked return values: reliability \n
			:return: power: Preamble peak power"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:UWB:MEASurement<Instance>:MEValuation:POWer:PPPower:SDEViation?', suppressed)
		return Conversions.str_to_float(response)

	def read(self) -> float:
		"""SCPI: READ:UWB:MEASurement<Instance>:MEValuation:POWer:PPPower:SDEViation \n
		Snippet: value: float = driver.uwbMeas.multiEval.power.ppPower.standardDev.read() \n
		Returns the value of the preamble peak power for the selected packet number <PPDU>. \n
		Suppressed linked return values: reliability \n
			:return: power: Preamble peak power"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'READ:UWB:MEASurement<Instance>:MEValuation:POWer:PPPower:SDEViation?', suppressed)
		return Conversions.str_to_float(response)
