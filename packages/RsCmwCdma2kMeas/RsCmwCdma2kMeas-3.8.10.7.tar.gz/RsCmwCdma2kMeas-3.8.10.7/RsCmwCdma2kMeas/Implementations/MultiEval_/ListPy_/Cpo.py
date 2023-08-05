from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cpo:
	"""Cpo commands group definition. 56 total commands, 10 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cpo", core, parent)

	@property
	def rpiCh(self):
		"""rpiCh commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_rpiCh'):
			from .Cpo_.RpiCh import RpiCh
			self._rpiCh = RpiCh(self._core, self._base)
		return self._rpiCh

	@property
	def rdcCh(self):
		"""rdcCh commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_rdcCh'):
			from .Cpo_.RdcCh import RdcCh
			self._rdcCh = RdcCh(self._core, self._base)
		return self._rdcCh

	@property
	def rccCh(self):
		"""rccCh commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_rccCh'):
			from .Cpo_.RccCh import RccCh
			self._rccCh = RccCh(self._core, self._base)
		return self._rccCh

	@property
	def reaCh(self):
		"""reaCh commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_reaCh'):
			from .Cpo_.ReaCh import ReaCh
			self._reaCh = ReaCh(self._core, self._base)
		return self._reaCh

	@property
	def rfch(self):
		"""rfch commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_rfch'):
			from .Cpo_.Rfch import Rfch
			self._rfch = Rfch(self._core, self._base)
		return self._rfch

	@property
	def rsCh(self):
		"""rsCh commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_rsCh'):
			from .Cpo_.RsCh import RsCh
			self._rsCh = RsCh(self._core, self._base)
		return self._rsCh

	@property
	def current(self):
		"""current commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_current'):
			from .Cpo_.Current import Current
			self._current = Current(self._core, self._base)
		return self._current

	@property
	def average(self):
		"""average commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_average'):
			from .Cpo_.Average import Average
			self._average = Average(self._core, self._base)
		return self._average

	@property
	def maximum(self):
		"""maximum commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_maximum'):
			from .Cpo_.Maximum import Maximum
			self._maximum = Maximum(self._core, self._base)
		return self._maximum

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .Cpo_.State import State
			self._state = State(self._core, self._base)
		return self._state

	def clone(self) -> 'Cpo':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cpo(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
