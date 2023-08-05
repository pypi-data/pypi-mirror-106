from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pstep:
	"""Pstep commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pstep", core, parent)

	# noinspection PyTypeChecker
	def get_direction(self) -> enums.UpDownDirection:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:OLTR:PSTep:DIRection \n
		Snippet: value: enums.UpDownDirection = driver.configure.oltr.pstep.get_direction() \n
		Defines the direction of the first power step within an OLTR measurement. For each subsequent power step, the direction
		is toggled. \n
			:return: pstep_direction: DOWN | UP
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:OLTR:PSTep:DIRection?')
		return Conversions.str_to_scalar_enum(response, enums.UpDownDirection)

	def set_direction(self, pstep_direction: enums.UpDownDirection) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:OLTR:PSTep:DIRection \n
		Snippet: driver.configure.oltr.pstep.set_direction(pstep_direction = enums.UpDownDirection.DOWN) \n
		Defines the direction of the first power step within an OLTR measurement. For each subsequent power step, the direction
		is toggled. \n
			:param pstep_direction: DOWN | UP
		"""
		param = Conversions.enum_scalar_to_str(pstep_direction, enums.UpDownDirection)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:OLTR:PSTep:DIRection {param}')

	def get_value(self) -> float:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:OLTR:PSTep \n
		Snippet: value: float = driver.configure.oltr.pstep.get_value() \n
		Defines the size of the power steps, i.e. the increases and decreases in the total BSS power during the OLTR measurement. \n
			:return: power_step: numeric The power step is relative to the measured reference power. Range: 0 dB to 40 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:OLTR:PSTep?')
		return Conversions.str_to_float(response)

	def set_value(self, power_step: float) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:OLTR:PSTep \n
		Snippet: driver.configure.oltr.pstep.set_value(power_step = 1.0) \n
		Defines the size of the power steps, i.e. the increases and decreases in the total BSS power during the OLTR measurement. \n
			:param power_step: numeric The power step is relative to the measured reference power. Range: 0 dB to 40 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(power_step)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:OLTR:PSTep {param}')
