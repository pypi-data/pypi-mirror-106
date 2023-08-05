from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Subframe:
	"""Subframe commands group definition. 16 total commands, 12 Sub-groups, 0 group commands
	Repeated Capability: Subframe, default value after init: Subframe.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("subframe", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_subframe_get', 'repcap_subframe_set', repcap.Subframe.Nr1)

	def repcap_subframe_set(self, enum_value: repcap.Subframe) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Subframe.Default
		Default value after init: Subframe.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_subframe_get(self) -> repcap.Subframe:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def carrier(self):
		"""carrier commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_carrier'):
			from .Subframe_.Carrier import Carrier
			self._carrier = Carrier(self._core, self._base)
		return self._carrier

	@property
	def duration(self):
		"""duration commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_duration'):
			from .Subframe_.Duration import Duration
			self._duration = Duration(self._core, self._base)
		return self._duration

	@property
	def fft(self):
		"""fft commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fft'):
			from .Subframe_.Fft import Fft
			self._fft = Fft(self._core, self._base)
		return self._fft

	@property
	def fil(self):
		"""fil commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fil'):
			from .Subframe_.Fil import Fil
			self._fil = Fil(self._core, self._base)
		return self._fil

	@property
	def guard(self):
		"""guard commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_guard'):
			from .Subframe_.Guard import Guard
			self._guard = Guard(self._core, self._base)
		return self._guard

	@property
	def mimo(self):
		"""mimo commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mimo'):
			from .Subframe_.Mimo import Mimo
			self._mimo = Mimo(self._core, self._base)
		return self._mimo

	@property
	def miso(self):
		"""miso commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_miso'):
			from .Subframe_.Miso import Miso
			self._miso = Miso(self._core, self._base)
		return self._miso

	@property
	def ndata(self):
		"""ndata commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ndata'):
			from .Subframe_.Ndata import Ndata
			self._ndata = Ndata(self._core, self._base)
		return self._ndata

	@property
	def pilot(self):
		"""pilot commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pilot'):
			from .Subframe_.Pilot import Pilot
			self._pilot = Pilot(self._core, self._base)
		return self._pilot

	@property
	def plp(self):
		"""plp commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_plp'):
			from .Subframe_.Plp import Plp
			self._plp = Plp(self._core, self._base)
		return self._plp

	@property
	def sbs(self):
		"""sbs commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_sbs'):
			from .Subframe_.Sbs import Sbs
			self._sbs = Sbs(self._core, self._base)
		return self._sbs

	@property
	def used(self):
		"""used commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_used'):
			from .Subframe_.Used import Used
			self._used = Used(self._core, self._base)
		return self._used

	def clone(self) -> 'Subframe':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Subframe(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
