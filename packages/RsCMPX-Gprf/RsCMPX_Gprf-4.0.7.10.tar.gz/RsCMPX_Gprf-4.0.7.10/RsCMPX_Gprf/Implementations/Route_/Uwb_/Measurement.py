from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Measurement:
	"""Measurement commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("measurement", core, parent)

	def get_spath(self) -> str:
		"""SCPI: ROUTe:UWB:MEASurement<instance>:SPATh \n
		Snippet: value: str = driver.route.uwb.measurement.get_spath() \n
		No command help available \n
			:return: signal_path: No help available
		"""
		response = self._core.io.query_str('ROUTe:UWB:MEASurement<Instance>:SPATh?')
		return trim_str_response(response)

	def set_spath(self, signal_path: str) -> None:
		"""SCPI: ROUTe:UWB:MEASurement<instance>:SPATh \n
		Snippet: driver.route.uwb.measurement.set_spath(signal_path = '1') \n
		No command help available \n
			:param signal_path: No help available
		"""
		param = Conversions.value_to_quoted_str(signal_path)
		self._core.io.write(f'ROUTe:UWB:MEASurement<Instance>:SPATh {param}')
