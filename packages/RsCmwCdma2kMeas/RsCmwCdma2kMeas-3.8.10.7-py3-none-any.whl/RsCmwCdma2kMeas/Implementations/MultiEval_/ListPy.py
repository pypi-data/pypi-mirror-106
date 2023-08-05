from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPy:
	"""ListPy commands group definition. 455 total commands, 8 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("listPy", core, parent)

	@property
	def sreliability(self):
		"""sreliability commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_sreliability'):
			from .ListPy_.Sreliability import Sreliability
			self._sreliability = Sreliability(self._core, self._base)
		return self._sreliability

	@property
	def modulation(self):
		"""modulation commands group. 17 Sub-classes, 0 commands."""
		if not hasattr(self, '_modulation'):
			from .ListPy_.Modulation import Modulation
			self._modulation = Modulation(self._core, self._base)
		return self._modulation

	@property
	def segment(self):
		"""segment commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_segment'):
			from .ListPy_.Segment import Segment
			self._segment = Segment(self._core, self._base)
		return self._segment

	@property
	def acp(self):
		"""acp commands group. 12 Sub-classes, 0 commands."""
		if not hasattr(self, '_acp'):
			from .ListPy_.Acp import Acp
			self._acp = Acp(self._core, self._base)
		return self._acp

	@property
	def obw(self):
		"""obw commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_obw'):
			from .ListPy_.Obw import Obw
			self._obw = Obw(self._core, self._base)
		return self._obw

	@property
	def cp(self):
		"""cp commands group. 11 Sub-classes, 0 commands."""
		if not hasattr(self, '_cp'):
			from .ListPy_.Cp import Cp
			self._cp = Cp(self._core, self._base)
		return self._cp

	@property
	def cpo(self):
		"""cpo commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_cpo'):
			from .ListPy_.Cpo import Cpo
			self._cpo = Cpo(self._core, self._base)
		return self._cpo

	@property
	def cto(self):
		"""cto commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_cto'):
			from .ListPy_.Cto import Cto
			self._cto = Cto(self._core, self._base)
		return self._cto

	def clone(self) -> 'ListPy':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ListPy(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
