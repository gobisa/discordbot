from unittest import mock
import datetime

import pytest

class MockCtx(mock.Mock):
    @pytest.mark.asyncio
    async def send(message):
        return

def make_coroutine(mock):
    async def coroutine(*args, **kwargs):
        return mock(*args, **kwargs)
    return coroutine


def create_mock_ctx(mockSend):
    mockObj = MockCtx()
    mockObj.send = make_coroutine(mockSend)
    return mockObj
