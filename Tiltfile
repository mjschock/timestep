# Run main.py with uv and watch for changes
local_resource(
    'main',
    auto_init=True,
    deps=['main.py', 'utils.py'],
    ignore=['**/__pycache__/**', '**/.git/**'],
    serve_cmd='uv run main.py'
)
