import dataclasses 

# @dataclasses.dataclass(frozen=True)
@dataclasses.dataclass
class Misc:
    value: int = 1
    value2: bool = False

x = Misc(10)
