from dataclasses import dataclass
from typing import List, Dict

from .common import Dataset, DataRecord, Ground, Player
from .pitch import Point


@dataclass
class Frame(DataRecord):
    frame_id: int
    players_coordinates: Dict[Player, Point]
    ball_position: Point


@dataclass
class TrackingDataset(Dataset):
    records: List[Frame]

    @property
    def frames(self):
        return self.records

    @property
    def frame_rate(self):
        return self.meta_data.frame_rate


__all__ = ["Frame", "TrackingDataset"]
