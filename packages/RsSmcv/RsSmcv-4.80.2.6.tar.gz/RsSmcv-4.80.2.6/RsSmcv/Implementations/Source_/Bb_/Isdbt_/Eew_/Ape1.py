from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ape1:
	"""Ape1 commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ape1", core, parent)

	def set(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:EEW:APE1 \n
		Snippet: driver.source.bb.isdbt.eew.ape1.set() \n
		Issues a seismic motion warning based on the 'EC1'/'EC2' settings. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:EEW:APE1')

	def set_with_opc(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:EEW:APE1 \n
		Snippet: driver.source.bb.isdbt.eew.ape1.set_with_opc() \n
		Issues a seismic motion warning based on the 'EC1'/'EC2' settings. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmcv.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:ISDBt:EEW:APE1')
