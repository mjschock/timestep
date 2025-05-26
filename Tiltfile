# Run main.py with uv and watch for changes
local_resource(
    'main',
    auto_init=True,
    cmd='uv run main.py',
    cmd_bat='uv run main.py',
    deps=['main.py', '*.py'],
    ignore=['**/__pycache__/**', '**/.git/**'],
    serve_cmd='uv run main.py'
)
