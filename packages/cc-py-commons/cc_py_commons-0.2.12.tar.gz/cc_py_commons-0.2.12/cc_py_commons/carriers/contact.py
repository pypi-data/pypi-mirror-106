import uuid
from dataclasses import dataclass, field
@dataclass
class Contact:
  id: uuid.UUID
  carrier_id: uuid.UUID
  first_name: str = field(default=None)
  last_name: str = field(default=None)
  phone: str = field(default=None)
  mobile: str = field(default=None)
  email_address: str = field(default=None)
  primary_contact: bool = field(default=False)
