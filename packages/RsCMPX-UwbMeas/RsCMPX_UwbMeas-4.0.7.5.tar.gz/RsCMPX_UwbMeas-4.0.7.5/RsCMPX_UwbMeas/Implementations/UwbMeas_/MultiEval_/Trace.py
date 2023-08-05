from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trace:
	"""Trace commands group definition. 42 total commands, 7 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("trace", core, parent)

	@property
	def ncCorr(self):
		"""ncCorr commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ncCorr'):
			from .Trace_.NcCorr import NcCorr
			self._ncCorr = NcCorr(self._core, self._base)
		return self._ncCorr

	@property
	def tsMask(self):
		"""tsMask commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_tsMask'):
			from .Trace_.TsMask import TsMask
			self._tsMask = TsMask(self._core, self._base)
		return self._tsMask

	@property
	def stJitter(self):
		"""stJitter commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_stJitter'):
			from .Trace_.StJitter import StJitter
			self._stJitter = StJitter(self._core, self._base)
		return self._stJitter

	@property
	def spJitter(self):
		"""spJitter commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_spJitter'):
			from .Trace_.SpJitter import SpJitter
			self._spJitter = SpJitter(self._core, self._base)
		return self._spJitter

	@property
	def ctJitter(self):
		"""ctJitter commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ctJitter'):
			from .Trace_.CtJitter import CtJitter
			self._ctJitter = CtJitter(self._core, self._base)
		return self._ctJitter

	@property
	def cpJitter(self):
		"""cpJitter commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_cpJitter'):
			from .Trace_.CpJitter import CpJitter
			self._cpJitter = CpJitter(self._core, self._base)
		return self._cpJitter

	@property
	def powerVsTime(self):
		"""powerVsTime commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_powerVsTime'):
			from .Trace_.PowerVsTime import PowerVsTime
			self._powerVsTime = PowerVsTime(self._core, self._base)
		return self._powerVsTime

	def clone(self) -> 'Trace':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Trace(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
