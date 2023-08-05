from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ResetLog:
	"""ResetLog commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("resetLog", core, parent)

	def set(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:INPut:STL:RESetlog \n
		Snippet: driver.source.bb.a3Tsc.inputPy.stl.resetLog.set() \n
		Resets the log file. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:INPut:STL:RESetlog')

	def set_with_opc(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:INPut:STL:RESetlog \n
		Snippet: driver.source.bb.a3Tsc.inputPy.stl.resetLog.set_with_opc() \n
		Resets the log file. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmcv.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:A3TSc:INPut:STL:RESetlog')
