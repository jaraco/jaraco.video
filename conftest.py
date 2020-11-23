import platform


collect_ignore_glob = (
    [
        'jaraco/video/*',
    ]
    if platform.system() != 'Windows'
    else []
)
