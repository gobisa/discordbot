from unittest import mock

class MockCtx(mock.Mock):
    def __init__(self, mockSend):
        super().__init__()

        def make_coroutine(mock):
            async def coroutine(*args, **kwargs):
                return mock(*args, **kwargs)
            return coroutine

        self.send = make_coroutine(mockSend)

