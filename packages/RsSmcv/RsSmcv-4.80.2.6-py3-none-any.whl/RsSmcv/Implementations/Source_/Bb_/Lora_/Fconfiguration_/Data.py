from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.Utilities import trim_str_response
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("data", core, parent)

	# noinspection PyTypeChecker
	class DpatternStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Dpattern: List[str]: No parameter help available
			- Bitcount: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct('Dpattern', DataType.RawStringList, None, False, True, 1),
			ArgStruct.scalar_int('Bitcount')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Dpattern: List[str] = None
			self.Bitcount: int = None

	def get_dpattern(self) -> DpatternStruct:
		"""SCPI: [SOURce<HW>]:BB:LORA:FCONfiguration:DATA:DPATtern \n
		Snippet: value: DpatternStruct = driver.source.bb.lora.fconfiguration.data.get_dpattern() \n
		No command help available \n
			:return: structure: for return value, see the help for DpatternStruct structure arguments.
		"""
		return self._core.io.query_struct('SOURce<HwInstance>:BB:LORA:FCONfiguration:DATA:DPATtern?', self.__class__.DpatternStruct())

	def set_dpattern(self, value: DpatternStruct) -> None:
		"""SCPI: [SOURce<HW>]:BB:LORA:FCONfiguration:DATA:DPATtern \n
		Snippet: driver.source.bb.lora.fconfiguration.data.set_dpattern(value = DpatternStruct()) \n
		No command help available \n
			:param value: see the help for DpatternStruct structure arguments.
		"""
		self._core.io.write_struct('SOURce<HwInstance>:BB:LORA:FCONfiguration:DATA:DPATtern', value)

	def get_dselection(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:LORA:FCONfiguration:DATA:DSELection \n
		Snippet: value: str = driver.source.bb.lora.fconfiguration.data.get_dselection() \n
		No command help available \n
			:return: dselection: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:LORA:FCONfiguration:DATA:DSELection?')
		return trim_str_response(response)

	def set_dselection(self, dselection: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:LORA:FCONfiguration:DATA:DSELection \n
		Snippet: driver.source.bb.lora.fconfiguration.data.set_dselection(dselection = '1') \n
		No command help available \n
			:param dselection: No help available
		"""
		param = Conversions.value_to_quoted_str(dselection)
		self._core.io.write(f'SOURce<HwInstance>:BB:LORA:FCONfiguration:DATA:DSELection {param}')

	# noinspection PyTypeChecker
	def get_value(self) -> enums.TdmaDataSource:
		"""SCPI: [SOURce<HW>]:BB:LORA:FCONfiguration:DATA \n
		Snippet: value: enums.TdmaDataSource = driver.source.bb.lora.fconfiguration.data.get_value() \n
		No command help available \n
			:return: data: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:LORA:FCONfiguration:DATA?')
		return Conversions.str_to_scalar_enum(response, enums.TdmaDataSource)

	def set_value(self, data: enums.TdmaDataSource) -> None:
		"""SCPI: [SOURce<HW>]:BB:LORA:FCONfiguration:DATA \n
		Snippet: driver.source.bb.lora.fconfiguration.data.set_value(data = enums.TdmaDataSource.DLISt) \n
		No command help available \n
			:param data: No help available
		"""
		param = Conversions.enum_scalar_to_str(data, enums.TdmaDataSource)
		self._core.io.write(f'SOURce<HwInstance>:BB:LORA:FCONfiguration:DATA {param}')
