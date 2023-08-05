"""
Class object for Media
Documentation: https://system-bridge.timmo.dev
"""
from __future__ import annotations
from ..base import BridgeBase


class Source(BridgeBase):
    @property
    def type(self) -> str:
        return self.attributes.get("type")

    @property
    def source(self) -> str:
        return self.attributes.get("source")

    @property
    def volumeInitial(self) -> str:
        return self.attributes.get("volumeInitial")

    @property
    def album(self) -> str | None:
        return self.attributes.get("album")

    @property
    def artist(self) -> str | None:
        return self.attributes.get("artist")

    @property
    def title(self) -> str | None:
        return self.attributes.get("title")


class Media(BridgeBase):
    @property
    def muted(self) -> bool | None:
        return self.attributes.get("muted")

    @property
    def playing(self) -> bool | None:
        return self.attributes.get("playing")

    @property
    def volume(self) -> float | None:
        return self.attributes.get("volume")

    @property
    def duration(self) -> float | None:
        return self.attributes.get("duration")

    @property
    def position(self) -> float | None:
        return self.attributes.get("position")

    @property
    def source(self) -> Source | None:
        return self.attributes.get("source")
