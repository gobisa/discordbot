import datetime as dt
from tests.test_helpers import MockCtx

import unittest
from unittest import mock
import aiounittest
from commands import Commands
import bot

class TestSmoketest(unittest.TestCase):
    
    def test_smoke(self):
        self.assertTrue(True)

class TestApp(aiounittest.AsyncTestCase):

    def test_import(self):
        self.assertTrue(hasattr(bot, "on_ready"))

    async def test_bing(self):
        mockSend = mock.Mock()
        ctx = MockCtx(mockSend)
        await Commands.bing(ctx)
        mockSend.assert_called_once_with("bong")

    async def test_ping(self):
        mockSend = mock.Mock()
        ctx = MockCtx(mockSend)
        await Commands.ping(ctx)
        mockSend.assert_called_once_with("pong")
    
    async def test_day(self):
        with mock.patch('commands.datetime') as mock_date:
            mock_date.today.return_value = dt.datetime(2021, 8, 30)
            mockSend = mock.Mock()
            ctx = MockCtx(mockSend)
            await Commands.day(ctx)
            mockSend.assert_called_once_with("It is Monday")

    async def test_add(self):
        mockSend = mock.Mock()
        ctx = MockCtx(mockSend)
        await Commands.add(ctx, "7", "8")
        mockSend.assert_called_once_with("78")


