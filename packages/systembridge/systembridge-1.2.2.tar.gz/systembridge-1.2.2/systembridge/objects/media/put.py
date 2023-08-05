"""
Class object for MediaPutResponse
Documentation: https://system-bridge.timmo.dev
"""
from __future__ import annotations

from ..base import BridgeBase


class MediaPutPayload(BridgeBase):
    @property
    def value(self) -> bool | float | None:
        return self.attributes.get("value")


class MediaPutResponse(BridgeBase):
    @property
    def successful(self) -> bool | None:
        return self.attributes.get("successful")
