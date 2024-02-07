async def on_startup():
    print(f'\n=== {__name__} on_startup (BEGIN) ===\n')
    print(f'\n=== {__name__} on_startup (END) ===\n')

async def on_shutdown():
    print(f'\n=== {__name__} on_shutdown (BEGIN) ===\n')
    print(f'\n=== {__name__} on_shutdown (END) ===\n')
