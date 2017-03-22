from rest_framework.views import APIView

__all__ = (
    'DeleteToken',
)


class DeleteToken(APIView):
    """
    POST요청이 오면 request.user가 인증되어 있는 경우, request.auth의 Token을 삭제
    """
    pass
