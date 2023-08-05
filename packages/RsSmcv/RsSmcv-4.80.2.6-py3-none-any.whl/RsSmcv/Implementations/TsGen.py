from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TsGen:
	"""TsGen commands group definition. 20 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("tsGen", core, parent)

	@property
	def configure(self):
		"""configure commands group. 4 Sub-classes, 9 commands."""
		if not hasattr(self, '_configure'):
			from .TsGen_.Configure import Configure
			self._configure = Configure(self._core, self._base)
		return self._configure

	@property
	def read(self):
		"""read commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_read'):
			from .TsGen_.Read import Read
			self._read = Read(self._core, self._base)
		return self._read

	def clone(self) -> 'TsGen':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TsGen(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
