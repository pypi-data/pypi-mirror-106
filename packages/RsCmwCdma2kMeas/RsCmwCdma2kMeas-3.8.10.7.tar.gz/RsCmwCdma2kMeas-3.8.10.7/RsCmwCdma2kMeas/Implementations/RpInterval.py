from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RpInterval:
	"""RpInterval commands group definition. 4 total commands, 1 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rpInterval", core, parent)

	@property
	def sequence(self):
		"""sequence commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sequence'):
			from .RpInterval_.Sequence import Sequence
			self._sequence = Sequence(self._core, self._base)
		return self._sequence

	def clone(self) -> 'RpInterval':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RpInterval(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
