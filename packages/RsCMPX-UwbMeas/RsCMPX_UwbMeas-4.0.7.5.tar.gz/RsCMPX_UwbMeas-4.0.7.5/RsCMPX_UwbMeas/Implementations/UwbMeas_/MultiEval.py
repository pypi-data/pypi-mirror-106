from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MultiEval:
	"""MultiEval commands group definition. 265 total commands, 6 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("multiEval", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .MultiEval_.State import State
			self._state = State(self._core, self._base)
		return self._state

	@property
	def tsMask(self):
		"""tsMask commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_tsMask'):
			from .MultiEval_.TsMask import TsMask
			self._tsMask = TsMask(self._core, self._base)
		return self._tsMask

	@property
	def modulation(self):
		"""modulation commands group. 17 Sub-classes, 0 commands."""
		if not hasattr(self, '_modulation'):
			from .MultiEval_.Modulation import Modulation
			self._modulation = Modulation(self._core, self._base)
		return self._modulation

	@property
	def power(self):
		"""power commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .MultiEval_.Power import Power
			self._power = Power(self._core, self._base)
		return self._power

	@property
	def sinfo(self):
		"""sinfo commands group. 7 Sub-classes, 2 commands."""
		if not hasattr(self, '_sinfo'):
			from .MultiEval_.Sinfo import Sinfo
			self._sinfo = Sinfo(self._core, self._base)
		return self._sinfo

	@property
	def trace(self):
		"""trace commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_trace'):
			from .MultiEval_.Trace import Trace
			self._trace = Trace(self._core, self._base)
		return self._trace

	def initiate(self) -> None:
		"""SCPI: INITiate:UWB:MEASurement<Instance>:MEValuation \n
		Snippet: driver.uwbMeas.multiEval.initiate() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'INITiate:UWB:MEASurement<Instance>:MEValuation')

	def initiate_with_opc(self) -> None:
		"""SCPI: INITiate:UWB:MEASurement<Instance>:MEValuation \n
		Snippet: driver.uwbMeas.multiEval.initiate_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as initiate, but waits for the operation to complete before continuing further. Use the RsCMPX_UwbMeas.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'INITiate:UWB:MEASurement<Instance>:MEValuation')

	def stop(self) -> None:
		"""SCPI: STOP:UWB:MEASurement<Instance>:MEValuation \n
		Snippet: driver.uwbMeas.multiEval.stop() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'STOP:UWB:MEASurement<Instance>:MEValuation')

	def stop_with_opc(self) -> None:
		"""SCPI: STOP:UWB:MEASurement<Instance>:MEValuation \n
		Snippet: driver.uwbMeas.multiEval.stop_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCMPX_UwbMeas.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'STOP:UWB:MEASurement<Instance>:MEValuation')

	def abort(self) -> None:
		"""SCPI: ABORt:UWB:MEASurement<Instance>:MEValuation \n
		Snippet: driver.uwbMeas.multiEval.abort() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'ABORt:UWB:MEASurement<Instance>:MEValuation')

	def abort_with_opc(self) -> None:
		"""SCPI: ABORt:UWB:MEASurement<Instance>:MEValuation \n
		Snippet: driver.uwbMeas.multiEval.abort_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsCMPX_UwbMeas.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'ABORt:UWB:MEASurement<Instance>:MEValuation')

	def clone(self) -> 'MultiEval':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MultiEval(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
