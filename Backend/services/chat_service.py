from agents.agent import Context
from dependencies import get_agent


def chat_with_agent(agent, message: str, user_id: str):
    result = agent.invoke(
        {
            "messages": [
                {"role": "user", "content": message}
            ]
        },
        config={"configurable": {"thread_id": user_id}},
        context=Context(user_id=user_id)
    )

    text = result["messages"][-1].content

    structured_obj = (
        result.get("structured")
        or result.get("structured_response")
        or result.get("output")
    )

    if structured_obj is not None:
        structured = structured_obj.model_dump()
    else:
        structured = {
            "person": None,
            "events": None,
            "summary": text,
            "error": "NO_STRUCTURED_OUTPUT"
        }

    return {
        "text": text,
        "structured": structured
    }