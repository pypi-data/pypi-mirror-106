from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IsPy:
	"""IsPy commands group definition. 6 total commands, 6 Sub-groups, 0 group commands
	Repeated Capability: InputStream, default value after init: InputStream.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("isPy", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_inputStream_get', 'repcap_inputStream_set', repcap.InputStream.Nr1)

	def repcap_inputStream_set(self, enum_value: repcap.InputStream) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to InputStream.Default
		Default value after init: InputStream.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_inputStream_get(self) -> repcap.InputStream:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def fecFrame(self):
		"""fecFrame commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fecFrame'):
			from .IsPy_.FecFrame import FecFrame
			self._fecFrame = FecFrame(self._core, self._base)
		return self._fecFrame

	@property
	def isi(self):
		"""isi commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_isi'):
			from .IsPy_.Isi import Isi
			self._isi = Isi(self._core, self._base)
		return self._isi

	@property
	def modCod(self):
		"""modCod commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_modCod'):
			from .IsPy_.ModCod import ModCod
			self._modCod = ModCod(self._core, self._base)
		return self._modCod

	@property
	def nsym(self):
		"""nsym commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nsym'):
			from .IsPy_.Nsym import Nsym
			self._nsym = Nsym(self._core, self._base)
		return self._nsym

	@property
	def pilots(self):
		"""pilots commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pilots'):
			from .IsPy_.Pilots import Pilots
			self._pilots = Pilots(self._core, self._base)
		return self._pilots

	@property
	def tsn(self):
		"""tsn commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tsn'):
			from .IsPy_.Tsn import Tsn
			self._tsn = Tsn(self._core, self._base)
		return self._tsn

	def clone(self) -> 'IsPy':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IsPy(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
