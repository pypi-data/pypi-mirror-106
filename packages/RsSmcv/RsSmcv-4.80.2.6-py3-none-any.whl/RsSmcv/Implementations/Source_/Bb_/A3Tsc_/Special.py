from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Special:
	"""Special commands group definition. 6 total commands, 4 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("special", core, parent)

	@property
	def alp(self):
		"""alp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_alp'):
			from .Special_.Alp import Alp
			self._alp = Alp(self._core, self._base)
		return self._alp

	@property
	def bootstrap(self):
		"""bootstrap commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_bootstrap'):
			from .Special_.Bootstrap import Bootstrap
			self._bootstrap = Bootstrap(self._core, self._base)
		return self._bootstrap

	@property
	def settings(self):
		"""settings commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_settings'):
			from .Special_.Settings import Settings
			self._settings = Settings(self._core, self._base)
		return self._settings

	@property
	def stl(self):
		"""stl commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_stl'):
			from .Special_.Stl import Stl
			self._stl = Stl(self._core, self._base)
		return self._stl

	def clone(self) -> 'Special':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Special(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
