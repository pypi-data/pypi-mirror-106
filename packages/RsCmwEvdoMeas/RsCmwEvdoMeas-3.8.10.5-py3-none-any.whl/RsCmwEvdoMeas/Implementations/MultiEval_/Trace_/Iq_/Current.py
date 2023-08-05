from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("current", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability Indicator'
			- Iphase: List[float]: No parameter help available
			- Qphase: List[float]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Iphase', DataType.FloatList, None, False, True, 1),
			ArgStruct('Qphase', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Iphase: List[float] = None
			self.Qphase: List[float] = None

	def read(self) -> ResultData:
		"""SCPI: READ:EVDO:MEASurement<instance>:MEValuation:TRACe:IQ:CURRent \n
		Snippet: value: ResultData = driver.multiEval.trace.iq.current.read() \n
		Returns the results in the I/Q constellation diagram. Every fourth value corresponds to a constellation point. The other
		values are on the path between two constellation points. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:EVDO:MEASurement<Instance>:MEValuation:TRACe:IQ:CURRent?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:EVDO:MEASurement<instance>:MEValuation:TRACe:IQ:CURRent \n
		Snippet: value: ResultData = driver.multiEval.trace.iq.current.fetch() \n
		Returns the results in the I/Q constellation diagram. Every fourth value corresponds to a constellation point. The other
		values are on the path between two constellation points. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:EVDO:MEASurement<Instance>:MEValuation:TRACe:IQ:CURRent?', self.__class__.ResultData())
