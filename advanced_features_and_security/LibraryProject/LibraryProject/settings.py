# Custom user model configuration
AUTH_USER_MODEL = 'bookshelf.CustomUser'

# Media settings for profile photos
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Add to INSTALLED_APPS if not already there
INSTALLED_APPS = [
    # ...
    'bookshelf',
    # ...
]
