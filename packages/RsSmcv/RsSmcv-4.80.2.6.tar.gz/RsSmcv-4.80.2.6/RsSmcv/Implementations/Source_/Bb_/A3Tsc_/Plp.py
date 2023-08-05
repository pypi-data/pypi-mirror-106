from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Plp:
	"""Plp commands group definition. 28 total commands, 16 Sub-groups, 0 group commands
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
	def alpType(self):
		"""alpType commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_alpType'):
			from .Plp_.AlpType import AlpType
			self._alpType = AlpType(self._core, self._base)
		return self._alpType

	@property
	def bbfCounter(self):
		"""bbfCounter commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bbfCounter'):
			from .Plp_.BbfCounter import BbfCounter
			self._bbfCounter = BbfCounter(self._core, self._base)
		return self._bbfCounter

	@property
	def bbfPadding(self):
		"""bbfPadding commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bbfPadding'):
			from .Plp_.BbfPadding import BbfPadding
			self._bbfPadding = BbfPadding(self._core, self._base)
		return self._bbfPadding

	@property
	def constel(self):
		"""constel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_constel'):
			from .Plp_.Constel import Constel
			self._constel = Constel(self._core, self._base)
		return self._constel

	@property
	def fecType(self):
		"""fecType commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fecType'):
			from .Plp_.FecType import FecType
			self._fecType = FecType(self._core, self._base)
		return self._fecType

	@property
	def id(self):
		"""id commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_id'):
			from .Plp_.Id import Id
			self._id = Id(self._core, self._base)
		return self._id

	@property
	def inputPy(self):
		"""inputPy commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_inputPy'):
			from .Plp_.InputPy import InputPy
			self._inputPy = InputPy(self._core, self._base)
		return self._inputPy

	@property
	def layer(self):
		"""layer commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_layer'):
			from .Plp_.Layer import Layer
			self._layer = Layer(self._core, self._base)
		return self._layer

	@property
	def lls(self):
		"""lls commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lls'):
			from .Plp_.Lls import Lls
			self._lls = Lls(self._core, self._base)
		return self._lls

	@property
	def packetLength(self):
		"""packetLength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_packetLength'):
			from .Plp_.PacketLength import PacketLength
			self._packetLength = PacketLength(self._core, self._base)
		return self._packetLength

	@property
	def rate(self):
		"""rate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rate'):
			from .Plp_.Rate import Rate
			self._rate = Rate(self._core, self._base)
		return self._rate

	@property
	def scrambler(self):
		"""scrambler commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scrambler'):
			from .Plp_.Scrambler import Scrambler
			self._scrambler = Scrambler(self._core, self._base)
		return self._scrambler

	@property
	def size(self):
		"""size commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_size'):
			from .Plp_.Size import Size
			self._size = Size(self._core, self._base)
		return self._size

	@property
	def til(self):
		"""til commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_til'):
			from .Plp_.Til import Til
			self._til = Til(self._core, self._base)
		return self._til

	@property
	def typePy(self):
		"""typePy commands group. 3 Sub-classes, 0 commands."""
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
