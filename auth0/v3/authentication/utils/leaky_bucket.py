import threading
import time

class Bucket(object):
    """Bucket. A 'leaky bucket' implementation to rate limit an operation

    Args:
        size (int, optional): The number of tokens this bucket will hold. Defaults to 10
        leak_rate (int, optional): The number of seconds to wait for a new token to be added to the bucket. Defaults to 60 seconds (1 minute)
    
    Raises:
        ValueError: If the size is less than 1 or the leak_rate is less than 5
    """

    def __init__(self, size=10, leak_rate=1*60):
        if size < 1:
            raise ValueError("size must be a positive int")
        if leak_rate < 5:
            raise ValueError("leak_rate must be a positive int of at least 5")
        self._size = size
        self._available = size
        self._leak_rate = leak_rate
        self._last_addition = time.time()
        self._remainder_delta = 0
        self._lock = threading.Lock()
        
    def leaks_in(self, amount=1):
        """Calculates how much time to wait to consume the given amount of tokens. This call is thread-safe

        Args:
            amount (int, optional): The amount of tokens planned to consume. Defaults to 1

        Returns:
            int: The number of seconds to wait to consume the given amount of tokens
        
        Raises:
            ValueError: when the amount is less than 1
        """
        if amount < 1:
            raise ValueError("amount must be a positive int")
        with self._lock:
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
        """Attempts to consume the given amount of tokens. This call is thread-safe

        Args:
            amount (int, optional): The amount of tokens to consume. Defaults to 1

        Returns:
            bool: Whether the tokens could be consumed or not
        
        Raises:
            ValueError: when the amount is less than 1
        """
        if amount < 1:
            raise ValueError("amount must be a positive int")
        with self._lock:
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