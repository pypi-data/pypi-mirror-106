from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Plp:
	"""Plp commands group definition. 29 total commands, 21 Sub-groups, 0 group commands
	Repeated Capability: PhysicalLayerPipe, default value after init: PhysicalLayerPipe.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("plp", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_physicalLayerPipe_get', 'repcap_physicalLayerPipe_set', repcap.PhysicalLayerPipe.Nr1)

	def repcap_physicalLayerPipe_set(self, enum_value: repcap.PhysicalLayerPipe) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to PhysicalLayerPipe.Default
		Default value after init: PhysicalLayerPipe.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_physicalLayerPipe_get(self) -> repcap.PhysicalLayerPipe:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def blocks(self):
		"""blocks commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_blocks'):
			from .Plp_.Blocks import Blocks
			self._blocks = Blocks(self._core, self._base)
		return self._blocks

	@property
	def cmType(self):
		"""cmType commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cmType'):
			from .Plp_.CmType import CmType
			self._cmType = CmType(self._core, self._base)
		return self._cmType

	@property
	def constel(self):
		"""constel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_constel'):
			from .Plp_.Constel import Constel
			self._constel = Constel(self._core, self._base)
		return self._constel

	@property
	def crotation(self):
		"""crotation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_crotation'):
			from .Plp_.Crotation import Crotation
			self._crotation = Crotation(self._core, self._base)
		return self._crotation

	@property
	def fecFrame(self):
		"""fecFrame commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fecFrame'):
			from .Plp_.FecFrame import FecFrame
			self._fecFrame = FecFrame(self._core, self._base)
		return self._fecFrame

	@property
	def frameIndex(self):
		"""frameIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frameIndex'):
			from .Plp_.FrameIndex import FrameIndex
			self._frameIndex = FrameIndex(self._core, self._base)
		return self._frameIndex

	@property
	def group(self):
		"""group commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_group'):
			from .Plp_.Group import Group
			self._group = Group(self._core, self._base)
		return self._group

	@property
	def ibs(self):
		"""ibs commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_ibs'):
			from .Plp_.Ibs import Ibs
			self._ibs = Ibs(self._core, self._base)
		return self._ibs

	@property
	def id(self):
		"""id commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_id'):
			from .Plp_.Id import Id
			self._id = Id(self._core, self._base)
		return self._id

	@property
	def inputPy(self):
		"""inputPy commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_inputPy'):
			from .Plp_.InputPy import InputPy
			self._inputPy = InputPy(self._core, self._base)
		return self._inputPy

	@property
	def issy(self):
		"""issy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_issy'):
			from .Plp_.Issy import Issy
			self._issy = Issy(self._core, self._base)
		return self._issy

	@property
	def maxBlocks(self):
		"""maxBlocks commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_maxBlocks'):
			from .Plp_.MaxBlocks import MaxBlocks
			self._maxBlocks = MaxBlocks(self._core, self._base)
		return self._maxBlocks

	@property
	def npd(self):
		"""npd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_npd'):
			from .Plp_.Npd import Npd
			self._npd = Npd(self._core, self._base)
		return self._npd

	@property
	def oibPlp(self):
		"""oibPlp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_oibPlp'):
			from .Plp_.OibPlp import OibPlp
			self._oibPlp = OibPlp(self._core, self._base)
		return self._oibPlp

	@property
	def packetLength(self):
		"""packetLength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_packetLength'):
			from .Plp_.PacketLength import PacketLength
			self._packetLength = PacketLength(self._core, self._base)
		return self._packetLength

	@property
	def padFlag(self):
		"""padFlag commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_padFlag'):
			from .Plp_.PadFlag import PadFlag
			self._padFlag = PadFlag(self._core, self._base)
		return self._padFlag

	@property
	def rate(self):
		"""rate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rate'):
			from .Plp_.Rate import Rate
			self._rate = Rate(self._core, self._base)
		return self._rate

	@property
	def staFlag(self):
		"""staFlag commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_staFlag'):
			from .Plp_.StaFlag import StaFlag
			self._staFlag = StaFlag(self._core, self._base)
		return self._staFlag

	@property
	def til(self):
		"""til commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_til'):
			from .Plp_.Til import Til
			self._til = Til(self._core, self._base)
		return self._til

	@property
	def typePy(self):
		"""typePy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_typePy'):
			from .Plp_.TypePy import TypePy
			self._typePy = TypePy(self._core, self._base)
		return self._typePy

	@property
	def useful(self):
		"""useful commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_useful'):
			from .Plp_.Useful import Useful
			self._useful = Useful(self._core, self._base)
		return self._useful

	def clone(self) -> 'Plp':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Plp(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
