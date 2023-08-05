from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.RepeatedCapability import RepeatedCapability
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IpAddress:
	"""IpAddress commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: IpAddress, default value after init: IpAddress.Addr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ipAddress", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_ipAddress_get', 'repcap_ipAddress_set', repcap.IpAddress.Addr1)

	def repcap_ipAddress_set(self, enum_value: repcap.IpAddress) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to IpAddress.Default
		Default value after init: IpAddress.Addr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_ipAddress_get(self) -> repcap.IpAddress:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	# noinspection PyTypeChecker
	class IpAddressStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- First_Segment: int: First octet of the IP address, not configurable Range: 0 to 255
			- Second_Segment: int: Second octet of the IP address, not configurable Range: 0 to 255
			- System_Id: int: Third octet of the IP address Range: 5 to 255
			- Local_Id: int: Fourth octet of the IP address Range: 1 to 254"""
		__meta_args_list = [
			ArgStruct.scalar_int('First_Segment'),
			ArgStruct.scalar_int('Second_Segment'),
			ArgStruct.scalar_int('System_Id'),
			ArgStruct.scalar_int('Local_Id')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.First_Segment: int = None
			self.Second_Segment: int = None
			self.System_Id: int = None
			self.Local_Id: int = None

	def set(self, structure: IpAddressStruct, ipAddress=repcap.IpAddress.Default) -> None:
		"""SCPI: CONFigure:BASE:MMONitor:IPADdress<n> \n
		Snippet: driver.configure.mmonitor.ipAddress.set(value = [PROPERTY_STRUCT_NAME](), ipAddress = repcap.IpAddress.Default) \n
		Configures the IP address pool for logging of signaling messages via an external PC. The pool contains three IP addresses
		of external logging PCs. The first two octets cannot be configured. For a setting command, you can specify any values
		within the allowed range - they are ignored. A query returns the active values resulting from the subnet configuration,
		see CONFigure:BASE:IPSet:SNODe. \n
			:param structure: for set value, see the help for IpAddressStruct structure arguments.
			:param ipAddress: optional repeated capability selector. Default value: Addr1 (settable in the interface 'IpAddress')"""
		ipAddress_cmd_val = self._base.get_repcap_cmd_value(ipAddress, repcap.IpAddress)
		self._core.io.write_struct(f'CONFigure:BASE:MMONitor:IPADdress{ipAddress_cmd_val}', structure)

	def get(self, ipAddress=repcap.IpAddress.Default) -> IpAddressStruct:
		"""SCPI: CONFigure:BASE:MMONitor:IPADdress<n> \n
		Snippet: value: IpAddressStruct = driver.configure.mmonitor.ipAddress.get(ipAddress = repcap.IpAddress.Default) \n
		Configures the IP address pool for logging of signaling messages via an external PC. The pool contains three IP addresses
		of external logging PCs. The first two octets cannot be configured. For a setting command, you can specify any values
		within the allowed range - they are ignored. A query returns the active values resulting from the subnet configuration,
		see CONFigure:BASE:IPSet:SNODe. \n
			:param ipAddress: optional repeated capability selector. Default value: Addr1 (settable in the interface 'IpAddress')
			:return: structure: for return value, see the help for IpAddressStruct structure arguments."""
		ipAddress_cmd_val = self._base.get_repcap_cmd_value(ipAddress, repcap.IpAddress)
		return self._core.io.query_struct(f'CONFigure:BASE:MMONitor:IPADdress{ipAddress_cmd_val}?', self.__class__.IpAddressStruct())

	def clone(self) -> 'IpAddress':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IpAddress(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
