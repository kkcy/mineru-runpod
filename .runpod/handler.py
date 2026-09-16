"""RunPod GitHub-import / Hub static handler path.

Runtime workers use repo-root ``handler.py`` (Dockerfile
``CMD ["python3", "-u", "handler.py"]``). This file exists because RunPod's
Import scanner looks under ``.runpod/`` first and does **not** follow
symlinks — the previous ``.runpod/handler.py -> ../handler.py`` link made
the scanner see only the link text and fail with:

    runpod.serverless.start() handler not found in your repo

Keep a real file here with a top-level ``runpod.serverless.start(...)`` Call.
Do not reintroduce the symlink.
"""

from __future__ import annotations

from typing import Any

import runpod


async def handler(job: dict[str, Any]) -> dict[str, Any]:
    """Placeholder for static detection; not invoked in production."""
    raise RuntimeError(
        ".runpod/handler.py is detection-only; Docker runs repo-root handler.py"
    )


# Required top-level Call for RunPod Import / Hub static detection.
# This module is not the Docker entrypoint and is not imported by tests.
runpod.serverless.start({"handler": handler})
