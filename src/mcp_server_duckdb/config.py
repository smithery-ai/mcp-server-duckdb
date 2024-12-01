import argparse
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Config:
    """
    Configuration for the server.
    """

    db_path: Path
    """
    Path to DuckDB database file.
    """

    readonly: bool
    """
    Run server in read-only mode.
    """

    @staticmethod
    def from_arguments() -> "Config":
        """
        Parse command line arguments.
        """
        parser = argparse.ArgumentParser(description="DuckDB MCP Server")

        parser.add_argument(
            "--db-path",
            type=Path,
            help="Path to DuckDB database file",
            required=True,
        )

        parser.add_argument(
            "--readonly",
            action="store_true",
            help="Run server in read-only mode. "
            "If the file does not exist, it is not created when connecting in read-only mode. "
            "Use duckdb.connect(), passing read_only=True. "
            "See: https://duckdb.org/docs/api/python/dbapi.html#read_only-connections",
        )

        args = parser.parse_args()
        return Config(db_path=args.db_path, readonly=args.readonly)
