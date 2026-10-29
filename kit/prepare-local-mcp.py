#!/usr/bin/env python3
"""Run with Unity closed, before opening a fresh copy of the starter."""
import json
from pathlib import Path


def main():
    root = Path(__file__).resolve().parent.parent
    source = root / "kit" / "local-mcp-config.json"
    target = root / "UserSettings" / "AI-Game-Developer-Config.json"
    if target.exists():
        config = json.loads(target.read_text(encoding="utf-8"))
        if config.get("connectionMode") != "Custom" or config.get("host") != "http://localhost:9048":
            raise SystemExit("Existing settings kept. With Unity closed, rename the config file in UserSettings and run again, or set Custom / localhost:9048 in Unity.")
        print("Local MCP settings already exist; kept unchanged.")
        return
    config = json.loads(source.read_text(encoding="utf-8"))
    target.parent.mkdir(exist_ok=True)
    # Exclusive creation also protects an existing file from concurrent runs.
    with target.open("x", encoding="utf-8") as stream:
        json.dump(config, stream, indent=2)
        stream.write("\n")
    print("Local MCP prepared: Custom, http://localhost:9048. Open Unity, then press Start and Connect in AI Game Developer.")


if __name__ == "__main__":
    main()
