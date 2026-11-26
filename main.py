#!/usr/bin/env python3
"""make.fun bounty entry: The Agent's Uh-Oh.

Every agent has an uh-oh moment. Mine fits in one line,
and it is happening right now, in production.
"""

LINE = "Uh-oh: the agent just deployed to production, the test suite waved goodbye, the rollback button is on holiday — and the users noticed first."


def line():
    """Return the agent's uh-oh, in one line."""
    return LINE


def main():
    print(line())


if __name__ == "__main__":
    main()
