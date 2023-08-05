from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.RepeatedCapability import RepeatedCapability
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Segment:
	"""Segment commands group definition. 61 total commands, 6 Sub-groups, 0 group commands
	Repeated Capability: Segment, default value after init: Segment.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("segment", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_segment_get', 'repcap_segment_set', repcap.Segment.Nr1)

	def repcap_segment_set(self, enum_value: repcap.Segment) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Segment.Default
		Default value after init: Segment.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_segment_get(self) -> repcap.Segment:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def modulation(self):
		"""modulation commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_modulation'):
			from .Segment_.Modulation import Modulation
			self._modulation = Modulation(self._core, self._base)
		return self._modulation

	@property
	def acp(self):
		"""acp commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_acp'):
			from .Segment_.Acp import Acp
			self._acp = Acp(self._core, self._base)
		return self._acp

	@property
	def obw(self):
		"""obw commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_obw'):
			from .Segment_.Obw import Obw
			self._obw = Obw(self._core, self._base)
		return self._obw

	@property
	def cp(self):
		"""cp commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_cp'):
			from .Segment_.Cp import Cp
			self._cp = Cp(self._core, self._base)
		return self._cp

	@property
	def cpo(self):
		"""cpo commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_cpo'):
			from .Segment_.Cpo import Cpo
			self._cpo = Cpo(self._core, self._base)
		return self._cpo

	@property
	def cto(self):
		"""cto commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_cto'):
			from .Segment_.Cto import Cto
			self._cto = Cto(self._core, self._base)
		return self._cto

	def clone(self) -> 'Segment':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Segment(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
