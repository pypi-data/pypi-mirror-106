from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SpJitter:
	"""SpJitter commands group definition. 6 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("spJitter", core, parent)

	@property
	def current(self):
		"""current commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_current'):
			from .SpJitter_.Current import Current
			self._current = Current(self._core, self._base)
		return self._current

	@property
	def average(self):
		"""average commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_average'):
			from .SpJitter_.Average import Average
			self._average = Average(self._core, self._base)
		return self._average

	@property
	def xvalues(self):
		"""xvalues commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_xvalues'):
			from .SpJitter_.Xvalues import Xvalues
			self._xvalues = Xvalues(self._core, self._base)
		return self._xvalues

	def clone(self) -> 'SpJitter':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SpJitter(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
