"""
Class object for MediaDeleteResponse
Documentation: https://system-bridge.timmo.dev
"""
from ..base import BridgeBase


class MediaDeleteResponse(BridgeBase):
    @property
    def successful(self) -> bool:
        return self.attributes.get("successful", False)
