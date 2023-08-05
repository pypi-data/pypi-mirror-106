from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pilot:
	"""Pilot commands group definition. 2 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pilot", core, parent)

	@property
	def boost(self):
		"""boost commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_boost'):
			from .Pilot_.Boost import Boost
			self._boost = Boost(self._core, self._base)
		return self._boost

	@property
	def siso(self):
		"""siso commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_siso'):
			from .Pilot_.Siso import Siso
			self._siso = Siso(self._core, self._base)
		return self._siso

	def clone(self) -> 'Pilot':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pilot(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
