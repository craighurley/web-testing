#!/usr/bin/env python

import parametrize_from_file
import dns.resolver
import pytest


@pytest.mark.dns
@parametrize_from_file
def test_records(ns, number, host_record, type, record):
    s = ""
    resolver = dns.resolver.Resolver()
    if len(ns) > 0:
        resolver.nameservers = [ns]
    answers = resolver.resolve(host_record, type, lifetime=3)
    for response in answers:
        s += str(response)
    for r in record:
        assert r in s, f"({number}/{host_record}) assert {r} in {s}"


if __name__ == "__main__":
    print("Run with: pytest FILENAME")
