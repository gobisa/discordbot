import datetime as dt
from tests.test_helpers import create_mock_ctx, mock_datetime

import unittest
from unittest import mock
import aiounittest
import bot

class TestSmoketest(unittest.TestCase):
    
    def test_smoke(self):
        self.assertTrue(True)

class TestApp(aiounittest.AsyncTestCase):

    def test_import(self):
        self.assertTrue(hasattr(bot, "on_ready"))

    async def test_bing(self):
        mockSend = mock.MagicMock()
        ctx = create_mock_ctx(mockSend)
        await bot.bing(ctx)
        mockSend.assert_called_once_with("bong")

    async def test_ping(self):
        mockSend = mock.MagicMock()
        ctx = create_mock_ctx(mockSend)
        await bot.ping(ctx)
        mockSend.assert_called_once_with("pong")
    
    async def test_day(self):
        mock_datetime()
        mockSend = mock.MagicMock()
        ctx = create_mock_ctx(mockSend)
        await bot.day(ctx)
        mockSend.assert_called_once_with("It is Sunday")

    async def test_add_basic(self):
        mockSend = mock.MagicMock()
        ctx = create_mock_ctx(mockSend)
        await bot.add(ctx, 7, 8)
        mockSend.assert_called_once_with(15)
    
    async def test_add_negative(self):
        mockSend = mock.MagicMock()
        ctx = create_mock_ctx(mockSend)
        await bot.add(ctx, -9, 8)
        mockSend.assert_called_once_with(-1)

