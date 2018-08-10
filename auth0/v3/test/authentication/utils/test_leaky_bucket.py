import unittest
import time
from ....authentication.utils.leaky_bucket import Bucket


class TestBucket(unittest.TestCase):

    def test_creates_with_default_size(self):
        bucket = Bucket()
        self.assertEqual(bucket._size, 5)
    
    def test_creates_with_custom_size(self):
        bucket = Bucket(size=123)
        self.assertEqual(bucket._size, 123)

    def test_creates_with_default_leak_rate(self):
        bucket = Bucket()
        self.assertEqual(bucket._leak_rate, 60*10)
    
    def test_creates_with_custom_leak_rate(self):
        bucket = Bucket(leak_rate=98765)
        self.assertEqual(bucket._leak_rate, 98765)

    def test_fails_when_size_is_below_1(self):
        self.assertRaises(ValueError, Bucket, size=0)

    def test_fails_when_leak_rate_is_below_5(self):
        self.assertRaises(ValueError, Bucket, leak_rate=4)

    def test_fails_when_consuming_less_than_1(self):
        bucket = Bucket()
        self.assertRaises(ValueError, bucket.consume, 0)
    
    def test_fails_when_checking_wait_time_for_less_than_1(self):
        bucket = Bucket()
        self.assertRaises(ValueError, bucket.leaks_in, 0)

    def test_can_consume_up_to_size(self):
        bucket = Bucket(size=5, leak_rate=60)
        self.assertTrue(bucket.consume(3))
        self.assertTrue(bucket.consume(2))
        self.assertFalse(bucket.consume(1))
    
    def test_refills_when_size_times_leak_rate_ellapsed(self):
        bucket = Bucket(size=2, leak_rate=5)
        self.assertTrue(bucket.consume(2))
        self.assertFalse(bucket.consume(1))
        time.sleep(2*5)
        self.assertTrue(bucket.consume(2))
        self.assertFalse(bucket.consume(1))

    def test_no_wait_time_when_available(self):
        bucket = Bucket(size=1, leak_rate=60)
        self.assertEqual(bucket.leaks_in(), 0)

    def test_leak_rate_wait_time_when_just_consumed(self):
        bucket = Bucket(size=3, leak_rate=60)
        self.assertTrue(bucket.consume(3))
        self.assertAlmostEqual(bucket.leaks_in(), 60, delta=0.01)
        self.assertAlmostEqual(bucket.leaks_in(3), 3*60, delta=0.01)

    def test_calculates_proper_wait_time_with_delta(self):
        bucket = Bucket(size=3, leak_rate=5)
        self.assertTrue(bucket.consume(3))
        # Bucket is empty. Should refill in 3 * 5 seconds
        time.sleep(7)
        self.assertTrue(bucket.consume(1))
        # Bucket empty again. Will refill completely in 3 * 5 - 2 seconds
        self.assertAlmostEqual(bucket.leaks_in(3), 3*5-2, delta=0.01)


