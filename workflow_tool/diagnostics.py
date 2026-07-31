"""Safe toolchain diagnostics."""

import platform
import shutil
import subprocess
import sys


def tool_version(command: str) -> str:
    """Return the first version line without invoking a shell."""
    executable = shutil.which(command)
    if not executable:
        return "not installed"
    try:
        result = subprocess.run([executable, "--version"], check=False, capture_output=True, text=True, timeout=5)
    except (OSError, subprocess.TimeoutExpired) as error:
        return f"unavailable: {error.__class__.__name__}"
    return (result.stdout or result.stderr).strip().splitlines()[0]


def system_report() -> dict[str, str]:
    """Collect reproducible operating-system and toolchain information."""
    return {
        "platform": platform.platform(),
        "python": sys.version.split()[0],
        "git": tool_version("git"),
        "node": tool_version("node"),
    }
