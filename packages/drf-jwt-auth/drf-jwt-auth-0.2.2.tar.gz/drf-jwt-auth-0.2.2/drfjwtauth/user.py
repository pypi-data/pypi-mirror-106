
class JWTUser:
    pk = None
    first_name = ''
    last_name = ''
    username = ''
    email = ''
    is_staff = False
    is_active = False
    is_superuser = False
    channels = []
    groups = []
    permissions = []
    token = None

    def __str__(self):
        return self.username

    def __int__(self):
        raise self.pk

    def __init__(self, payload, token=None):
        self.pk = payload.get('pk', payload.get('id'))
        self.first_name = payload.get('first_name')
        self.last_name = payload.get('last_name')
        self.username = payload.get('username')
        self.email = payload.get('email')
        self.is_staff = payload.get('is_staff')
        self.is_active = payload.get('is_active')
        self.is_superuser = payload.get('is_superuser')
        self.channels = payload.get('channels', [])
        self.groups = payload.get('groups', [])
        self.permissions = payload.get('permissions', [])
        self.token = token

    def save(self):
        raise NotImplementedError("Django doesn't provide a DB representation for AnonymousUser.")

    def delete(self):
        raise NotImplementedError("Django doesn't provide a DB representation for AnonymousUser.")

    def set_password(self, raw_password):
        raise NotImplementedError("Django doesn't provide a DB representation for AnonymousUser.")

    def check_password(self, raw_password):
        raise NotImplementedError("Django doesn't provide a DB representation for AnonymousUser.")

    @property
    def id(self):
        return self.pk

    @property
    def user_permissions(self):
        return self.permissions

    def get_user_permissions(self, obj=None):
        return self.permissions

    def get_group_permissions(self, obj=None):
        raise NotImplemented()

    def get_all_permissions(self, obj=None):
        return self.permissions

    def has_perm(self, perm, obj=None):
        return perm in self.permissions

    def has_perms(self, perm_list, obj=None):
        return all(self.has_perm(perm, obj) for perm in perm_list)

    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return True

    def get_username(self):
        return self.username
