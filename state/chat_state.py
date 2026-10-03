from typing import TypedDict

class ChatState(TypedDict, total=False):
    question: str
    student_id: int
    category: str
    context: str
    answer: str

    #state is ued to store the info and  state will go as a input for all the node in our application