from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class General:
	"""General commands group definition. 24 total commands, 4 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("general", core, parent)

	@property
	def am(self):
		"""am commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_am'):
			from .General_.Am import Am
			self._am = Am(self._core, self._base)
		return self._am

	@property
	def fm(self):
		"""fm commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_fm'):
			from .General_.Fm import Fm
			self._fm = Fm(self._core, self._base)
		return self._fm

	@property
	def pm(self):
		"""pm commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_pm'):
			from .General_.Pm import Pm
			self._pm = Pm(self._core, self._base)
		return self._pm

	@property
	def pulm(self):
		"""pulm commands group. 3 Sub-classes, 5 commands."""
		if not hasattr(self, '_pulm'):
			from .General_.Pulm import Pulm
			self._pulm = Pulm(self._core, self._base)
		return self._pulm

	def clone(self) -> 'General':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = General(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
