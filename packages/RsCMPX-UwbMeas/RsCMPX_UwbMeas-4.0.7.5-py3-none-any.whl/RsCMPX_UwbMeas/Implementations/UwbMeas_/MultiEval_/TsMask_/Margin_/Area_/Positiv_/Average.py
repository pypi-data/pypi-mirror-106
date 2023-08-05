from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Average:
	"""Average commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("average", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability Indicator'
			- Margin_Aver_Pos_X: float: X-position of the margin for the area no
			- Margin_Aver_Pos_Y: float: Y-value of the margin for the area no"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Margin_Aver_Pos_X'),
			ArgStruct.scalar_float('Margin_Aver_Pos_Y')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Margin_Aver_Pos_X: float = None
			self.Margin_Aver_Pos_Y: float = None

	def fetch(self, area=repcap.Area.Default) -> ResultData:
		"""SCPI: FETCh:UWB:MEASurement<Instance>:MEValuation:TSMask:MARGin:AREA<nr>:POSitiv:AVERage \n
		Snippet: value: ResultData = driver.uwbMeas.multiEval.tsMask.margin.area.positiv.average.fetch(area = repcap.Area.Default) \n
		Returns the margin values between the result trace and the transmission spectrum mask for the area <no> with positive
		frequency offset. A negative margin indicates that the trace is located above the limit line, i.e. the limit is exceeded.
		The current and average values can be retrieved. See also 'Square Transmit Spectrum Mask'. \n
			:param area: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Area')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		area_cmd_val = self._base.get_repcap_cmd_value(area, repcap.Area)
		return self._core.io.query_struct(f'FETCh:UWB:MEASurement<Instance>:MEValuation:TSMask:MARGin:AREA{area_cmd_val}:POSitiv:AVERage?', self.__class__.ResultData())

	def read(self, area=repcap.Area.Default) -> ResultData:
		"""SCPI: READ:UWB:MEASurement<Instance>:MEValuation:TSMask:MARGin:AREA<nr>:POSitiv:AVERage \n
		Snippet: value: ResultData = driver.uwbMeas.multiEval.tsMask.margin.area.positiv.average.read(area = repcap.Area.Default) \n
		Returns the margin values between the result trace and the transmission spectrum mask for the area <no> with positive
		frequency offset. A negative margin indicates that the trace is located above the limit line, i.e. the limit is exceeded.
		The current and average values can be retrieved. See also 'Square Transmit Spectrum Mask'. \n
			:param area: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Area')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		area_cmd_val = self._base.get_repcap_cmd_value(area, repcap.Area)
		return self._core.io.query_struct(f'READ:UWB:MEASurement<Instance>:MEValuation:TSMask:MARGin:AREA{area_cmd_val}:POSitiv:AVERage?', self.__class__.ResultData())
