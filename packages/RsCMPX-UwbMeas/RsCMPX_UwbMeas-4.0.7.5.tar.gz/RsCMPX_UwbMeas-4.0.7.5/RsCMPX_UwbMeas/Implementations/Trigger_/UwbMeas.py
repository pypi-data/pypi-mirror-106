from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UwbMeas:
	"""UwbMeas commands group definition. 7 total commands, 1 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("uwbMeas", core, parent)

	@property
	def multiEval(self):
		"""multiEval commands group. 1 Sub-classes, 6 commands."""
		if not hasattr(self, '_multiEval'):
			from .UwbMeas_.MultiEval import MultiEval
			self._multiEval = MultiEval(self._core, self._base)
		return self._multiEval

	def clone(self) -> 'UwbMeas':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UwbMeas(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
