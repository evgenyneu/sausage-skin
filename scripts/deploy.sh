#!/bin/sh

uv run -m src.generate.main
rsync -rvz web/ aws:web/evgenii.com/sausage-skin/
