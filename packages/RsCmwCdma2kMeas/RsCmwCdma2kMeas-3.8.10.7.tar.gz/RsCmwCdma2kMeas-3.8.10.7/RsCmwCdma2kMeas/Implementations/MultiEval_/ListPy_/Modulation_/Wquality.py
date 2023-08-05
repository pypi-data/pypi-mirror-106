from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Wquality:
	"""Wquality commands group definition. 12 total commands, 6 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("wquality", core, parent)

	@property
	def current(self):
		"""current commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_current'):
			from .Wquality_.Current import Current
			self._current = Current(self._core, self._base)
		return self._current

	@property
	def pmax(self):
		"""pmax commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pmax'):
			from .Wquality_.Pmax import Pmax
			self._pmax = Pmax(self._core, self._base)
		return self._pmax

	@property
	def pmin(self):
		"""pmin commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pmin'):
			from .Wquality_.Pmin import Pmin
			self._pmin = Pmin(self._core, self._base)
		return self._pmin

	@property
	def average(self):
		"""average commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_average'):
			from .Wquality_.Average import Average
			self._average = Average(self._core, self._base)
		return self._average

	@property
	def maximum(self):
		"""maximum commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_maximum'):
			from .Wquality_.Maximum import Maximum
			self._maximum = Maximum(self._core, self._base)
		return self._maximum

	@property
	def standardDev(self):
		"""standardDev commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_standardDev'):
			from .Wquality_.StandardDev import StandardDev
			self._standardDev = StandardDev(self._core, self._base)
		return self._standardDev

	def clone(self) -> 'Wquality':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Wquality(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
