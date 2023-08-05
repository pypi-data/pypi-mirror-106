from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cto:
	"""Cto commands group definition. 20 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cto", core, parent)

	@property
	def isignal(self):
		"""isignal commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_isignal'):
			from .Cto_.Isignal import Isignal
			self._isignal = Isignal(self._core, self._base)
		return self._isignal

	@property
	def qsignal(self):
		"""qsignal commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_qsignal'):
			from .Cto_.Qsignal import Qsignal
			self._qsignal = Qsignal(self._core, self._base)
		return self._qsignal

	def clone(self) -> 'Cto':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cto(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
