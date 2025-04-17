# Backend service
docker_compose('docker-compose.yaml', env_file='./src/timestep/services/backend/.env')

# Configure live updates for backend
docker_build(
    'mschock/timestep-backend',
    context='./src/timestep/services/backend',
    dockerfile='./src/timestep/services/backend/Dockerfile',
    ignore=[
        '**/__pycache__',
        '**/*.pyc',
        '**/.pytest_cache',
        '**/*.egg-info',
    ],
    live_update=[
        # fall_back_on must be at the start of the list
        # This tells Tilt to trigger a full rebuild when pyproject.toml changes
        # instead of trying to sync it (which causes update loops)
        fall_back_on('./src/timestep/services/backend/pyproject.toml'),
        
        # Sync everything except pyproject.toml to prevent update loops
        sync('./src/timestep/services/backend', '/app/src'),
        sync('./src/timestep/services/backend/main.py', '/app/main.py'),
        sync('./src/timestep/services/backend/LICENSE', '/app/LICENSE'),
        sync('./src/timestep/services/backend/README.md', '/app/README.md'),
        # Sync the .env file
        sync('./src/timestep/services/backend/.env', '/app/.env'),
    ]
)

# Configure live updates for frontend
docker_build(
    'mschock/timestep-frontend',
    context='./src/timestep/services/frontend',
    dockerfile='./src/timestep/services/frontend/Dockerfile',
    target='dev',
    ignore=[
        '**/node_modules',
        '**/.next',
        # Add additional ignore patterns to prevent update loops
        '**/.DS_Store',
        '**/dist',
        '**/.cache',
        '**/coverage',
        # Temporary files that might be created during development
        '**/*.swp',
        '**/*.swo',
        '**/*.bak',
        '**/*.tmp',
    ],
    live_update=[
        # More selective syncing - only sync relevant directories
        sync('./src/timestep/services/frontend/src', '/app/src'),
        sync('./src/timestep/services/frontend/public', '/app/public'),
        sync('./src/timestep/services/frontend/app', '/app/app'),
        sync('./src/timestep/services/frontend/styles', '/app/styles'),
        sync('./src/timestep/services/frontend/components', '/app/components'),
        # Additional files that might be needed
        sync('./src/timestep/services/frontend/package.json', '/app/package.json'),
        sync('./src/timestep/services/frontend/package-lock.json', '/app/package-lock.json'),
        sync('./src/timestep/services/frontend/next.config.js', '/app/next.config.js'),
        sync('./src/timestep/services/frontend/tsconfig.json', '/app/tsconfig.json'),
        # Run npm install when package files change
        run('npm install', trigger=['./src/timestep/services/frontend/package.json', './src/timestep/services/frontend/package-lock.json']),
    ]
)

# Define resources for better control and organization
dc_resource('backend', 
    # labels=['api', 'backend'],
    labels=['backend'],
    resource_deps=[],
)

dc_resource('frontend', 
    # labels=['ui', 'frontend'],
    labels=['frontend'],
    resource_deps=['backend'],
    auto_init=True,
)
