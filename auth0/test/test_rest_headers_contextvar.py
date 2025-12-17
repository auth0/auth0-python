"""Tests for context-var based response headers in RestClient.

Tests verify that headers are properly isolated across threads and async contexts.
"""

import threading
import time
import unittest
from unittest import mock

import responses

from auth0.rest import RestClient, RestClientOptions


class TestRestClientHeadersContextVar(unittest.TestCase):
    """Test that response headers are properly stored and accessed via contextvars."""

    @responses.activate
    def test_headers_accessible_after_request(self):
        """Test that headers are stored and accessible after a successful request."""
        responses.add(
            responses.GET,
            "https://example.com/api/test",
            json={"result": "ok"},
            status=200,
            headers={
                "X-RateLimit-Limit": "60",
                "X-RateLimit-Remaining": "59",
                "X-RateLimit-Reset": "1640000000",
            },
        )

        client = RestClient(jwt="test-token")
        result = client.get("https://example.com/api/test")

        self.assertEqual(result, {"result": "ok"})
        headers = client.last_response_headers
        self.assertEqual(headers.get("X-RateLimit-Limit"), "60")
        self.assertEqual(headers.get("X-RateLimit-Remaining"), "59")
        self.assertEqual(headers.get("X-RateLimit-Reset"), "1640000000")

    @responses.activate
    def test_headers_on_204_response(self):
        """Test that headers are preserved on 204 No Content responses."""
        responses.add(
            responses.DELETE,
            "https://example.com/api/resource/123",
            status=204,
            headers={
                "X-RateLimit-Limit": "30",
                "X-RateLimit-Remaining": "25",
                "X-RateLimit-Reset": "1640000100",
            },
        )

        client = RestClient(jwt="test-token")
        result = client.delete("https://example.com/api/resource/123")

        # 204 returns empty content
        self.assertEqual(result, "")
        # But headers should still be accessible
        headers = client.last_response_headers
        self.assertEqual(headers.get("X-RateLimit-Limit"), "30")
        self.assertEqual(headers.get("X-RateLimit-Remaining"), "25")

    @responses.activate
    def test_headers_updated_on_successive_requests(self):
        """Test that headers are updated with each new request."""
        # First request
        responses.add(
            responses.GET,
            "https://example.com/api/test1",
            json={"id": 1},
            status=200,
            headers={"X-RateLimit-Remaining": "59"},
        )

        # Second request
        responses.add(
            responses.GET,
            "https://example.com/api/test2",
            json={"id": 2},
            status=200,
            headers={"X-RateLimit-Remaining": "58"},
        )

        client = RestClient(jwt="test-token")

        # First request
        client.get("https://example.com/api/test1")
        self.assertEqual(client.last_response_headers.get("X-RateLimit-Remaining"), "59")

        # Second request should update headers
        client.get("https://example.com/api/test2")
        self.assertEqual(client.last_response_headers.get("X-RateLimit-Remaining"), "58")

    @responses.activate
    def test_headers_empty_initially(self):
        """Test that headers are empty before any request is made."""
        client = RestClient(jwt="test-token")
        headers = client.last_response_headers
        self.assertEqual(headers, {})

    @responses.activate
    def test_thread_isolation(self):
        """Test that response headers are isolated between threads.
        
        This is the key thread-safety test: each thread should have its own
        response headers when using contextvars.
        """
        results = {}
        errors = []

        # Setup responses with different headers for each endpoint
        responses.add(
            responses.GET,
            "https://example.com/api/thread1",
            json={"thread": 1},
            status=200,
            headers={"X-RateLimit-Remaining": "100"},
        )

        responses.add(
            responses.GET,
            "https://example.com/api/thread2",
            json={"thread": 2},
            status=200,
            headers={"X-RateLimit-Remaining": "200"},
        )

        def thread_worker(thread_id: int, endpoint: str, remaining: str):
            """Worker function for thread test."""
            try:
                client = RestClient(jwt="test-token")
                client.get(f"https://example.com/api/{endpoint}")
                # Each thread should see its own headers, not contaminated by other threads
                results[thread_id] = client.last_response_headers.get(
                    "X-RateLimit-Remaining"
                )
            except Exception as e:
                errors.append(str(e))

        # Start two threads that make requests simultaneously
        thread1 = threading.Thread(target=thread_worker, args=(1, "thread1", "100"))
        thread2 = threading.Thread(target=thread_worker, args=(2, "thread2", "200"))

        thread1.start()
        thread2.start()

        thread1.join()
        thread2.join()

        # Verify no errors occurred
        self.assertEqual(errors, [], f"Errors in threads: {errors}")

        # Verify each thread got the correct headers for its request
        self.assertEqual(results[1], "100", "Thread 1 should see its own headers")
        self.assertEqual(results[2], "200", "Thread 2 should see its own headers")

    @responses.activate
    def test_headers_in_same_context_reflect_latest_request(self):
        """Test that in the same execution context, headers reflect the latest request.
        
        Contextvars are context-specific (thread or async task), not client-specific.
        When multiple clients make requests in the same context, the contextvar reflects
        the most recent response. For isolation per client, use different threads.
        """
        responses.add(
            responses.GET,
            "https://example.com/api/request1",
            json={"request": 1},
            status=200,
            headers={"X-Request-ID": "request1"},
        )

        responses.add(
            responses.GET,
            "https://example.com/api/request2",
            json={"request": 2},
            status=200,
            headers={"X-Request-ID": "request2"},
        )

        client1 = RestClient(jwt="token1")
        client2 = RestClient(jwt="token2")

        # First request
        client1.get("https://example.com/api/request1")
        self.assertEqual(client1.last_response_headers.get("X-Request-ID"), "request1")

        # Second request in same context overwrites the contextvar
        client2.get("https://example.com/api/request2")
        # Both clients see the latest headers because they're in the same context
        self.assertEqual(client1.last_response_headers.get("X-Request-ID"), "request2")
        self.assertEqual(client2.last_response_headers.get("X-Request-ID"), "request2")

    @responses.activate
    def test_post_request_headers(self):
        """Test that headers are captured on POST requests."""
        responses.add(
            responses.POST,
            "https://example.com/api/create",
            json={"id": "new-id"},
            status=201,
            headers={"X-RateLimit-Remaining": "55"},
        )

        client = RestClient(jwt="test-token")
        result = client.post("https://example.com/api/create", data={"name": "test"})

        self.assertEqual(result["id"], "new-id")
        self.assertEqual(client.last_response_headers.get("X-RateLimit-Remaining"), "55")

    @responses.activate
    def test_patch_request_headers(self):
        """Test that headers are captured on PATCH requests."""
        responses.add(
            responses.PATCH,
            "https://example.com/api/update/123",
            json={"id": "123", "updated": True},
            status=200,
            headers={"X-RateLimit-Remaining": "54"},
        )

        client = RestClient(jwt="test-token")
        result = client.patch("https://example.com/api/update/123", data={"name": "updated"})

        self.assertEqual(result["updated"], True)
        self.assertEqual(client.last_response_headers.get("X-RateLimit-Remaining"), "54")


if __name__ == "__main__":
    unittest.main()
