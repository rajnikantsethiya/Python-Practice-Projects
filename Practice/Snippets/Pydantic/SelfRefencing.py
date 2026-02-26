from pydantic import BaseModel
from typing import Optional, List

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None

Comment.model_rebuild() # This is to resolve the depency and re run the comment class model

comment = Comment(
    id=1,
    content="Hello",
    replies=[
        Comment(id=2, content="Hi"),
        Comment(id=3, content="Hi there", replies=[
            Comment(id=4, content="I am good")
        ])
    ]
)

