"""
1. Post model의 to_dict()메서드 삭제
2. tests패키지를 생성, 패키지 내부에 tests_apis.py생성
    Post Create, Photo Add를 각각 테스트 케이스로 구현
    실행할 동작을 테스트코드로 구현
3. 테스트코드가 하나씩 돌아갈 수 있도록 코드를 구현
    PostList:
        Post에 대한 List, Create
    PostDetail:
        Post에 대한 Retrieve, Update, Destroy

    3-1. serializers.py파일 생성, Post와 Photo에 대한 serializer구현
    3-2. views를 패키지로 생성, 내부에 apis모듈로 DRF의 genericAPIView를 사용
    3-3. genericAPIView와 urls를 연결
        3-3-1. urls역시 패키지로 생성, 내부에 apis모듈을 생성해서 연결
    3-4. root urls와 연결
    3-5. 정상동작 확인
"""
