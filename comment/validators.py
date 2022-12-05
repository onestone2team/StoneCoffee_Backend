from django.core.exceptions import ValidationError

## 필요한지 아직 모르겠음
def validate_point(value):
    if value>5 or value <5:
        if (value > 5) | (value < 0 ):
            message = "평점은 0 이상 5 이하입니다."
        raise ValidationError(message)

# 댓글 등록 글자수 요구조건
def validate_comment(value):
    if len(value)<10:
        message = "후기는 10자 이상이어야 등록 가능합니다."
    raise ValidationError(message)