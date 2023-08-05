from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RsCh:
	"""RsCh commands group definition. 18 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rsCh", core, parent)

	@property
	def ztef(self):
		"""ztef commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_ztef'):
			from .RsCh_.Ztef import Ztef
			self._ztef = Ztef(self._core, self._base)
		return self._ztef

	@property
	def zoet(self):
		"""zoet commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_zoet'):
			from .RsCh_.Zoet import Zoet
			self._zoet = Zoet(self._core, self._base)
		return self._zoet

	def clone(self) -> 'RsCh':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RsCh(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
