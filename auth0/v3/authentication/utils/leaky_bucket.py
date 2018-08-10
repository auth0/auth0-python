import time


class Bucket(object):

    def __init__(self, size=5, leak_rate=10*60):
        if size < 1:
            raise ValueError("size must be a positive int")
        if leak_rate < 5:
            raise ValueError("leak_rate must be a positive int bigger than 5")
        self._size = size
        self._available = size
        self._leak_rate = leak_rate
        self._last_addition = time.time()
        self._remainder_delta = 0
        
    def leaks_in(self, amount=1):
        if amount < 1:
            raise ValueError("amount must be a positive int")
        self._calculate_available_tokens()
        if self._available >= amount:
            return 0
        ellapsed_time = self._get_ellapsed_time()
        if ellapsed_time < self._leak_rate:
            ellapsed_time = self._leak_rate - ellapsed_time
        remaining = amount - self._available - 1
        if remaining > 0:
            ellapsed_time = ellapsed_time + self._leak_rate * remaining
        return ellapsed_time

    def consume(self, amount=1):
        if amount < 1:
            raise ValueError("amount must be a positive int")
        self._calculate_available_tokens()
        if self._available >= amount:
            self._available = self._available - amount
            return True
        return False

    def _calculate_available_tokens(self):
        ellapsed_time = self._get_ellapsed_time()
        if ellapsed_time < self._leak_rate:
            return None
        tokens_to_add = int(ellapsed_time / self._leak_rate)
        self._remainder_delta = ellapsed_time % self._leak_rate
        if tokens_to_add > 0:
            self._last_addition = time.time()
            self._available = self._available + tokens_to_add
            if self._available > self._size:
                self._available = self._size

    def _get_ellapsed_time(self):
        return time.time() - self._last_addition + self._remainder_delta