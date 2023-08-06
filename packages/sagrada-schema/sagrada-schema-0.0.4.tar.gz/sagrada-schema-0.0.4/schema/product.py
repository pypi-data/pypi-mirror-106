from dataclasses import dataclass, asdict
import dataclasses
from typing import List, Optional
import json


@dataclass
class Product:
    productID: int
    embedding: Optional[List[float]] = None
    title: Optional[str] = None
    description: Optional[str] = None
    brand: Optional[str] = None
    category: Optional[str] = None
    active: Optional[bool] = None

    def keyify(self):
        return asdict(self)


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)
