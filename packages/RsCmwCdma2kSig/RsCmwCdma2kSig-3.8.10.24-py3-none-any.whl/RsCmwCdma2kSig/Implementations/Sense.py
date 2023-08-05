from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup
from ..Internal.StructBase import StructBase
from ..Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sense:
	"""Sense commands group definition. 36 total commands, 5 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sense", core, parent)

	@property
	def test(self):
		"""test commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_test'):
			from .Sense_.Test import Test
			self._test = Test(self._core, self._base)
		return self._test

	@property
	def bsAddress(self):
		"""bsAddress commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bsAddress'):
			from .Sense_.BsAddress import BsAddress
			self._bsAddress = BsAddress(self._core, self._base)
		return self._bsAddress

	@property
	def atAddress(self):
		"""atAddress commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_atAddress'):
			from .Sense_.AtAddress import AtAddress
			self._atAddress = AtAddress(self._core, self._base)
		return self._atAddress

	@property
	def rxQuality(self):
		"""rxQuality commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_rxQuality'):
			from .Sense_.RxQuality import RxQuality
			self._rxQuality = RxQuality(self._core, self._base)
		return self._rxQuality

	@property
	def elog(self):
		"""elog commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_elog'):
			from .Sense_.Elog import Elog
			self._elog = Elog(self._core, self._base)
		return self._elog

	# noinspection PyTypeChecker
	class CvInfoStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Loopback_Delay: float: Time delay measured during loopback voice connection Range: 0 s to 10 s , Unit: s
			- Forward_Enc_Delay: float: Encoder time delay in forward link measured during the connection to the speech codec board Range: 0 s to 10 s , Unit: s
			- Reverse_Dec_Delay: float: Decoder time delay in reverse link measured during the connection to the speech codec board Range: 0 s to 10 s , Unit: s"""
		__meta_args_list = [
			ArgStruct.scalar_float('Loopback_Delay'),
			ArgStruct.scalar_float('Forward_Enc_Delay'),
			ArgStruct.scalar_float('Reverse_Dec_Delay')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Loopback_Delay: float = None
			self.Forward_Enc_Delay: float = None
			self.Reverse_Dec_Delay: float = None

	def get_cv_info(self) -> CvInfoStruct:
		"""SCPI: SENSe:CDMA:SIGNaling<instance>:CVINfo \n
		Snippet: value: CvInfoStruct = driver.sense.get_cv_info() \n
		Displays the time delay of a voice connection. \n
			:return: structure: for return value, see the help for CvInfoStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:CDMA:SIGNaling<Instance>:CVINfo?', self.__class__.CvInfoStruct())

	def clone(self) -> 'Sense':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sense(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
