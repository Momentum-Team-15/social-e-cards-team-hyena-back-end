from rest_framework import permissions

class IsUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if obj.owner == request.user:
            return True
        else:
            return False

    

class IsCreatorOrReadOnly(permissions.BasePermission):
    

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if obj.owner == request.user:
            return True
        return False
def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user