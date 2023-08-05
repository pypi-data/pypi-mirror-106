from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MultiEval:
	"""MultiEval commands group definition. 21 total commands, 5 Sub-groups, 10 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("multiEval", core, parent)

	@property
	def stsGap(self):
		"""stsGap commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stsGap'):
			from .MultiEval_.StsGap import StsGap
			self._stsGap = StsGap(self._core, self._base)
		return self._stsGap

	@property
	def spectrum(self):
		"""spectrum commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_spectrum'):
			from .MultiEval_.Spectrum import Spectrum
			self._spectrum = Spectrum(self._core, self._base)
		return self._spectrum

	@property
	def result(self):
		"""result commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_result'):
			from .MultiEval_.Result import Result
			self._result = Result(self._core, self._base)
		return self._result

	@property
	def modulation(self):
		"""modulation commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_modulation'):
			from .MultiEval_.Modulation import Modulation
			self._modulation = Modulation(self._core, self._base)
		return self._modulation

	@property
	def tsMask(self):
		"""tsMask commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_tsMask'):
			from .MultiEval_.TsMask import TsMask
			self._tsMask = TsMask(self._core, self._base)
		return self._tsMask

	# noinspection PyTypeChecker
	def get_scondition(self) -> enums.StopCondition:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:SCONdition \n
		Snippet: value: enums.StopCondition = driver.configure.uwbMeas.multiEval.get_scondition() \n
		Qualifies whether the measurement is stopped after a failed limit check or continued. SLFail means that the measurement
		is stopped and reaches the RDY state when one of the results exceeds the limits. \n
			:return: stop_condition: NONE: Continue measurement irrespective of the limit check SLFail: Stop measurement on limit failure
		"""
		response = self._core.io.query_str('CONFigure:UWB:MEASurement<Instance>:MEValuation:SCONdition?')
		return Conversions.str_to_scalar_enum(response, enums.StopCondition)

	def set_scondition(self, stop_condition: enums.StopCondition) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:SCONdition \n
		Snippet: driver.configure.uwbMeas.multiEval.set_scondition(stop_condition = enums.StopCondition.NONE) \n
		Qualifies whether the measurement is stopped after a failed limit check or continued. SLFail means that the measurement
		is stopped and reaches the RDY state when one of the results exceeds the limits. \n
			:param stop_condition: NONE: Continue measurement irrespective of the limit check SLFail: Stop measurement on limit failure
		"""
		param = Conversions.enum_scalar_to_str(stop_condition, enums.StopCondition)
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:SCONdition {param}')

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:TOUT \n
		Snippet: value: float = driver.configure.uwbMeas.multiEval.get_timeout() \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually (ON | OFF key or RESTART | STOP key) . When the measurement
		has completed the first measurement cycle (first single shot) , the statistical depth is reached and the timer is reset.
		If the first measurement cycle has not been completed when the timer expires, the measurement is stopped. The measurement
		state changes to RDY. The reliability indicator is set to 1, indicating that a measurement timeout occurred.
		Still running READ, FETCh or CALCulate commands are completed, returning the available results. At least for some results,
		there are no values at all or the statistical depth has not been reached. A timeout of 0 s corresponds to an infinite
		measurement timeout. \n
			:return: tcd_timeout: No help available
		"""
		response = self._core.io.query_str('CONFigure:UWB:MEASurement<Instance>:MEValuation:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, tcd_timeout: float) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:TOUT \n
		Snippet: driver.configure.uwbMeas.multiEval.set_timeout(tcd_timeout = 1.0) \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually (ON | OFF key or RESTART | STOP key) . When the measurement
		has completed the first measurement cycle (first single shot) , the statistical depth is reached and the timer is reset.
		If the first measurement cycle has not been completed when the timer expires, the measurement is stopped. The measurement
		state changes to RDY. The reliability indicator is set to 1, indicating that a measurement timeout occurred.
		Still running READ, FETCh or CALCulate commands are completed, returning the available results. At least for some results,
		there are no values at all or the statistical depth has not been reached. A timeout of 0 s corresponds to an infinite
		measurement timeout. \n
			:param tcd_timeout: No help available
		"""
		param = Conversions.decimal_value_to_str(tcd_timeout)
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:TOUT {param}')

	def get_scount(self) -> int:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:SCOunt \n
		Snippet: value: int = driver.configure.uwbMeas.multiEval.get_scount() \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. The statistic count applies to TX modulation and jitter measurements. \n
			:return: statistic_count: No help available
		"""
		response = self._core.io.query_str('CONFigure:UWB:MEASurement<Instance>:MEValuation:SCOunt?')
		return Conversions.str_to_int(response)

	def set_scount(self, statistic_count: int) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:SCOunt \n
		Snippet: driver.configure.uwbMeas.multiEval.set_scount(statistic_count = 1) \n
		Specifies the statistic count of the measurement. The statistic count is equal to the number of measurement intervals per
		single shot. The statistic count applies to TX modulation and jitter measurements. \n
			:param statistic_count: No help available
		"""
		param = Conversions.decimal_value_to_str(statistic_count)
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:SCOunt {param}')

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.Repeat:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:REPetition \n
		Snippet: value: enums.Repeat = driver.configure.uwbMeas.multiEval.get_repetition() \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single shot or repeated continuously. Use CONFigure:..:MEAS<i>:...:SCOunt to determine the number of measurement
		intervals per single shot. \n
			:return: repetition: SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		response = self._core.io.query_str('CONFigure:UWB:MEASurement<Instance>:MEValuation:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.Repeat)

	def set_repetition(self, repetition: enums.Repeat) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:REPetition \n
		Snippet: driver.configure.uwbMeas.multiEval.set_repetition(repetition = enums.Repeat.CONTinuous) \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single shot or repeated continuously. Use CONFigure:..:MEAS<i>:...:SCOunt to determine the number of measurement
		intervals per single shot. \n
			:param repetition: SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.Repeat)
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:REPetition {param}')

	def get_mo_exception(self) -> bool:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:MOEXception \n
		Snippet: value: bool = driver.configure.uwbMeas.multiEval.get_mo_exception() \n
		Specifies whether measurement results identified as faulty or inaccurate are rejected. \n
			:return: meas_on_exception: OFF: Faulty results are rejected. ON: Results are never rejected.
		"""
		response = self._core.io.query_str('CONFigure:UWB:MEASurement<Instance>:MEValuation:MOEXception?')
		return Conversions.str_to_bool(response)

	def set_mo_exception(self, meas_on_exception: bool) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:MOEXception \n
		Snippet: driver.configure.uwbMeas.multiEval.set_mo_exception(meas_on_exception = False) \n
		Specifies whether measurement results identified as faulty or inaccurate are rejected. \n
			:param meas_on_exception: OFF: Faulty results are rejected. ON: Results are never rejected.
		"""
		param = Conversions.bool_to_str(meas_on_exception)
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:MOEXception {param}')

	def get_ps_format(self) -> int:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:PSFormat \n
		Snippet: value: int = driver.configure.uwbMeas.multiEval.get_ps_format() \n
		Specifies the PPDU STS packet structure configuration. See also 'HRP-ERDEV'. \n
			:return: ppdu_sts_format: No help available
		"""
		response = self._core.io.query_str('CONFigure:UWB:MEASurement<Instance>:MEValuation:PSFormat?')
		return Conversions.str_to_int(response)

	def set_ps_format(self, ppdu_sts_format: int) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:PSFormat \n
		Snippet: driver.configure.uwbMeas.multiEval.set_ps_format(ppdu_sts_format = 1) \n
		Specifies the PPDU STS packet structure configuration. See also 'HRP-ERDEV'. \n
			:param ppdu_sts_format: No help available
		"""
		param = Conversions.decimal_value_to_str(ppdu_sts_format)
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:PSFormat {param}')

	def get_pp_length(self) -> int:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:PPLength \n
		Snippet: value: int = driver.configure.uwbMeas.multiEval.get_pp_length() \n
		Specifies the bit length of the PHR payload length field. This setting is only relevant in HPRF mode (RHML or RHMH set
		viamethod RsCMPX_UwbMeas.Configure.UwbMeas.MultiEval.phrRate ) . \n
			:return: phr_payload_len: No help available
		"""
		response = self._core.io.query_str('CONFigure:UWB:MEASurement<Instance>:MEValuation:PPLength?')
		return Conversions.str_to_int(response)

	def set_pp_length(self, phr_payload_len: int) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:PPLength \n
		Snippet: driver.configure.uwbMeas.multiEval.set_pp_length(phr_payload_len = 1) \n
		Specifies the bit length of the PHR payload length field. This setting is only relevant in HPRF mode (RHML or RHMH set
		viamethod RsCMPX_UwbMeas.Configure.UwbMeas.MultiEval.phrRate ) . \n
			:param phr_payload_len: No help available
		"""
		param = Conversions.decimal_value_to_str(phr_payload_len)
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:PPLength {param}')

	def get_st_segments(self) -> int:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:STSegments \n
		Snippet: value: int = driver.configure.uwbMeas.multiEval.get_st_segments() \n
		Specifies the number of STS segments inserted according to the STS packet configuration. \n
			:return: no_sts_segments: No help available
		"""
		response = self._core.io.query_str('CONFigure:UWB:MEASurement<Instance>:MEValuation:STSegments?')
		return Conversions.str_to_int(response)

	def set_st_segments(self, no_sts_segments: int) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:STSegments \n
		Snippet: driver.configure.uwbMeas.multiEval.set_st_segments(no_sts_segments = 1) \n
		Specifies the number of STS segments inserted according to the STS packet configuration. \n
			:param no_sts_segments: No help available
		"""
		param = Conversions.decimal_value_to_str(no_sts_segments)
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:STSegments {param}')

	# noinspection PyTypeChecker
	def get_sts_length(self) -> enums.StsSegmentLen:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:STSLength \n
		Snippet: value: enums.StsSegmentLen = driver.configure.uwbMeas.multiEval.get_sts_length() \n
		Specifies the length of the STS segment in units of 512 chips. \n
			:return: sts_segment_len: No help available
		"""
		response = self._core.io.query_str('CONFigure:UWB:MEASurement<Instance>:MEValuation:STSLength?')
		return Conversions.str_to_scalar_enum(response, enums.StsSegmentLen)

	def set_sts_length(self, sts_segment_len: enums.StsSegmentLen) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:STSLength \n
		Snippet: driver.configure.uwbMeas.multiEval.set_sts_length(sts_segment_len = enums.StsSegmentLen.L128) \n
		Specifies the length of the STS segment in units of 512 chips. \n
			:param sts_segment_len: No help available
		"""
		param = Conversions.enum_scalar_to_str(sts_segment_len, enums.StsSegmentLen)
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:STSLength {param}')

	# noinspection PyTypeChecker
	def get_phr_rate(self) -> enums.PhrDataRate:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:PHRRate \n
		Snippet: value: enums.PhrDataRate = driver.configure.uwbMeas.multiEval.get_phr_rate() \n
		Specifies the data rate of the PHY header (PHR) . \n
			:return: phr_data_rate: DRMD: 110 kb/s or 850 kb/s (DRMDR) DRLP: 850 kb/s (DRBM_LP) DRHP: 6.8 Mb/s (DRBM_HP) RHML: 3.9 Mb/s or 7.8 Mb/s (DRHM_LR) RHMH: 15.6 Mb/s or 31.2 Mb/s (DRHM_HR)
		"""
		response = self._core.io.query_str('CONFigure:UWB:MEASurement<Instance>:MEValuation:PHRRate?')
		return Conversions.str_to_scalar_enum(response, enums.PhrDataRate)

	def set_phr_rate(self, phr_data_rate: enums.PhrDataRate) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:PHRRate \n
		Snippet: driver.configure.uwbMeas.multiEval.set_phr_rate(phr_data_rate = enums.PhrDataRate.DRHP) \n
		Specifies the data rate of the PHY header (PHR) . \n
			:param phr_data_rate: DRMD: 110 kb/s or 850 kb/s (DRMDR) DRLP: 850 kb/s (DRBM_LP) DRHP: 6.8 Mb/s (DRBM_HP) RHML: 3.9 Mb/s or 7.8 Mb/s (DRHM_LR) RHMH: 15.6 Mb/s or 31.2 Mb/s (DRHM_HR)
		"""
		param = Conversions.enum_scalar_to_str(phr_data_rate, enums.PhrDataRate)
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:PHRRate {param}')

	def clone(self) -> 'MultiEval':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MultiEval(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
