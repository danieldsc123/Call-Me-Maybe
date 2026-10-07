import json

from src.schemas import FunctionDefinition


def serialize_functions(functions: list[FunctionDefinition]) -> str:
    """Converte as definições validadas em texto JSON."""
    definitions = [function.model_dump() for function in functions]
    return json.dumps(definitions, ensure_ascii=False)


def build_prompt(
    functions: list[FunctionDefinition],
    user_prompt: str,
) -> str:
    """Monta as instruções e os dados para escolher uma chamada."""
    catalog = serialize_functions(functions)

    return (
        "Select exactly one function from the available functions.\n"
        "Extract its arguments from the user request.\n"
        "Do not execute the function or answer the request directly.\n"
        'Return JSON with exactly the keys "name" and "parameters".\n'
        f"Available functions:\n{catalog}\n"
        f"User request:\n{user_prompt}\n"
        "JSON response:\n"
    )
