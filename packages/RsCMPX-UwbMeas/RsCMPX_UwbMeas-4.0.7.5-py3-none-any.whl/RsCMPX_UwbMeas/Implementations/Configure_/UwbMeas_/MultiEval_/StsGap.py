from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StsGap:
	"""StsGap commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("stsGap", core, parent)

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:STSGap:ENABle \n
		Snippet: value: bool = driver.configure.uwbMeas.multiEval.stsGap.get_enable() \n
		No command help available \n
			:return: sts_gap: No help available
		"""
		response = self._core.io.query_str('CONFigure:UWB:MEASurement<Instance>:MEValuation:STSGap:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, sts_gap: bool) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:STSGap:ENABle \n
		Snippet: driver.configure.uwbMeas.multiEval.stsGap.set_enable(sts_gap = False) \n
		No command help available \n
			:param sts_gap: No help available
		"""
		param = Conversions.bool_to_str(sts_gap)
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:STSGap:ENABle {param}')
