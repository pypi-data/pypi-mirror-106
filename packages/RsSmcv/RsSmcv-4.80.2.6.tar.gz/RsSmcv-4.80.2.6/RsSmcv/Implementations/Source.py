from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Source:
	"""Source commands group definition. 1469 total commands, 21 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("source", core, parent)

	@property
	def am(self):
		"""am commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_am'):
			from .Source_.Am import Am
			self._am = Am(self._core, self._base)
		return self._am

	@property
	def awgn(self):
		"""awgn commands group. 5 Sub-classes, 5 commands."""
		if not hasattr(self, '_awgn'):
			from .Source_.Awgn import Awgn
			self._awgn = Awgn(self._core, self._base)
		return self._awgn

	@property
	def bb(self):
		"""bb commands group. 25 Sub-classes, 7 commands."""
		if not hasattr(self, '_bb'):
			from .Source_.Bb import Bb
			self._bb = Bb(self._core, self._base)
		return self._bb

	@property
	def bbin(self):
		"""bbin commands group. 7 Sub-classes, 9 commands."""
		if not hasattr(self, '_bbin'):
			from .Source_.Bbin import Bbin
			self._bbin = Bbin(self._core, self._base)
		return self._bbin

	@property
	def correction(self):
		"""correction commands group. 3 Sub-classes, 2 commands."""
		if not hasattr(self, '_correction'):
			from .Source_.Correction import Correction
			self._correction = Correction(self._core, self._base)
		return self._correction

	@property
	def dm(self):
		"""dm commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_dm'):
			from .Source_.Dm import Dm
			self._dm = Dm(self._core, self._base)
		return self._dm

	@property
	def fm(self):
		"""fm commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_fm'):
			from .Source_.Fm import Fm
			self._fm = Fm(self._core, self._base)
		return self._fm

	@property
	def frequency(self):
		"""frequency commands group. 3 Sub-classes, 9 commands."""
		if not hasattr(self, '_frequency'):
			from .Source_.Frequency import Frequency
			self._frequency = Frequency(self._core, self._base)
		return self._frequency

	@property
	def inputPy(self):
		"""inputPy commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_inputPy'):
			from .Source_.InputPy import InputPy
			self._inputPy = InputPy(self._core, self._base)
		return self._inputPy

	@property
	def iq(self):
		"""iq commands group. 3 Sub-classes, 4 commands."""
		if not hasattr(self, '_iq'):
			from .Source_.Iq import Iq
			self._iq = Iq(self._core, self._base)
		return self._iq

	@property
	def listPy(self):
		"""listPy commands group. 7 Sub-classes, 9 commands."""
		if not hasattr(self, '_listPy'):
			from .Source_.ListPy import ListPy
			self._listPy = ListPy(self._core, self._base)
		return self._listPy

	@property
	def modulation(self):
		"""modulation commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_modulation'):
			from .Source_.Modulation import Modulation
			self._modulation = Modulation(self._core, self._base)
		return self._modulation

	@property
	def noise(self):
		"""noise commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_noise'):
			from .Source_.Noise import Noise
			self._noise = Noise(self._core, self._base)
		return self._noise

	@property
	def path(self):
		"""path commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_path'):
			from .Source_.Path import Path
			self._path = Path(self._core, self._base)
		return self._path

	@property
	def phase(self):
		"""phase commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_phase'):
			from .Source_.Phase import Phase
			self._phase = Phase(self._core, self._base)
		return self._phase

	@property
	def pm(self):
		"""pm commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_pm'):
			from .Source_.Pm import Pm
			self._pm = Pm(self._core, self._base)
		return self._pm

	@property
	def power(self):
		"""power commands group. 7 Sub-classes, 9 commands."""
		if not hasattr(self, '_power'):
			from .Source_.Power import Power
			self._power = Power(self._core, self._base)
		return self._power

	@property
	def pulm(self):
		"""pulm commands group. 2 Sub-classes, 3 commands."""
		if not hasattr(self, '_pulm'):
			from .Source_.Pulm import Pulm
			self._pulm = Pulm(self._core, self._base)
		return self._pulm

	@property
	def roscillator(self):
		"""roscillator commands group. 3 Sub-classes, 2 commands."""
		if not hasattr(self, '_roscillator'):
			from .Source_.Roscillator import Roscillator
			self._roscillator = Roscillator(self._core, self._base)
		return self._roscillator

	@property
	def sweep(self):
		"""sweep commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_sweep'):
			from .Source_.Sweep import Sweep
			self._sweep = Sweep(self._core, self._base)
		return self._sweep

	@property
	def iqcoder(self):
		"""iqcoder commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqcoder'):
			from .Source_.Iqcoder import Iqcoder
			self._iqcoder = Iqcoder(self._core, self._base)
		return self._iqcoder

	def preset(self) -> None:
		"""SCPI: SOURce<HW>:PRESet \n
		Snippet: driver.source.preset() \n
		Presets all parameters which are related to the selected signal path. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:PRESet')

	def preset_with_opc(self) -> None:
		"""SCPI: SOURce<HW>:PRESet \n
		Snippet: driver.source.preset_with_opc() \n
		Presets all parameters which are related to the selected signal path. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmcv.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:PRESet')

	def clone(self) -> 'Source':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Source(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
