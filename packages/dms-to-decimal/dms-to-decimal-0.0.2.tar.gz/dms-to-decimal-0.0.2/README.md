dms-to-decimal
A Python library for converting degrees, minutes, and seconds to decimal

Installation

pip install dms-to-decimal

Example

import dms_to_decimal as dms

degree = 46
minutes = 59
seconds = 5
direction = 'N'

converDms2Decimal = dms.DMS2Decimal(degree, minutes, seconds, direction)

print(converDms2Decimal); # Output: 46.984722222222224