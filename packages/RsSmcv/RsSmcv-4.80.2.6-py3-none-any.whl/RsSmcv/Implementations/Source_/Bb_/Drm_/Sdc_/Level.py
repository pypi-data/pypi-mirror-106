from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Level:
	"""Level commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: Index, default value after init: Index.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("level", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_index_get', 'repcap_index_set', repcap.Index.Nr1)

	def repcap_index_set(self, enum_value: repcap.Index) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Index.Default
		Default value after init: Index.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_index_get(self) -> repcap.Index:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	# noinspection PyTypeChecker
	def get(self, index=repcap.Index.Default) -> enums.DrmCodingProtectionLevelSdc:
		"""SCPI: [SOURce<HW>]:BB:DRM:SDC:LEVel<CH> \n
		Snippet: value: enums.DrmCodingProtectionLevelSdc = driver.source.bb.drm.sdc.level.get(index = repcap.Index.Default) \n
		Queries the protection level of the . \n
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Level')
			:return: drm_sdc_lev: 0| 1| INV 0|1 Available protection levels INV Invalid protection level"""
		index_cmd_val = self._base.get_repcap_cmd_value(index, repcap.Index)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:DRM:SDC:LEVel{index_cmd_val}?')
		return Conversions.str_to_scalar_enum(response, enums.DrmCodingProtectionLevelSdc)

	def clone(self) -> 'Level':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Level(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
