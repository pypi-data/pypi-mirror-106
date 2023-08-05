from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("all", core, parent)

	def delete(self) -> None:
		"""SCPI: DELete:SYSTem:ATTenuation:CTABle:ALL \n
		Snippet: driver.system.attenuation.correctionTable.all.delete() \n
		No command help available \n
		"""
		self._core.io.write(f'DELete:SYSTem:ATTenuation:CTABle:ALL')

	def delete_with_opc(self) -> None:
		"""SCPI: DELete:SYSTem:ATTenuation:CTABle:ALL \n
		Snippet: driver.system.attenuation.correctionTable.all.delete_with_opc() \n
		No command help available \n
		Same as delete, but waits for the operation to complete before continuing further. Use the RsCMPX_Gprf.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'DELete:SYSTem:ATTenuation:CTABle:ALL')
