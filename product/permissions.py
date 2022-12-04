from rest_framework.permissions import BasePermission

class IsAdminOrAuthenticatedOrReadOnly(BasePermission):
    http_method = ["POST", "PUT", "DELETE"]
    def has_permission(self, request, view):
        message ="접근 권한이 없습니다!"
        user = request.user

        if user.is_authenticated and request.method == "GET": # 로그인하지 않은 유저이고, method가 GET일때
            return True

        elif not user.is_authenticated and request.method == "GET": # 로그인하지 않은 유저이고, method가 GET일때
            return True

        elif not user.is_authenticated and request.method in self.http_method: # 로그인하지 않은 유저이고, GET이 아닌 method를 요청할 때
            self.message = "로그인이 필요합니다"
            return False

        elif user.is_admin:
            return True

        else:
            return False
        
class DeletePermissition(BasePermission):
    
    def has_permission(self, request, view):
        message ="접근 권한이 없습니다!"
        user = request.user

        if request.method == "DELETE" and user.is_admin:
            return True

        else:
            return False