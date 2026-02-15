from dataclasses import dataclass, field
from typing import List


@dataclass
class Student:
    student_id: str
    name: str
    email: str
    grades: List[float] = field(default_factory=list)

    def average(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)
