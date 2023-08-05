from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UwbMeas:
	"""UwbMeas commands group definition. 26 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("uwbMeas", core, parent)

	@property
	def multiEval(self):
		"""multiEval commands group. 5 Sub-classes, 10 commands."""
		if not hasattr(self, '_multiEval'):
			from .UwbMeas_.MultiEval import MultiEval
			self._multiEval = MultiEval(self._core, self._base)
		return self._multiEval

	@property
	def rfSettings(self):
		"""rfSettings commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_rfSettings'):
			from .UwbMeas_.RfSettings import RfSettings
			self._rfSettings = RfSettings(self._core, self._base)
		return self._rfSettings

	def clone(self) -> 'UwbMeas':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UwbMeas(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
