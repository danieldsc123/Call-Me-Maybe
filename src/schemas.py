from typing import Literal

from pydantic import BaseModel, TypeAdapter


class PromptInput(BaseModel):
    """Representa um pedido em linguagem natural."""

    prompt: str


class TypeDefinition(BaseModel):
    """Representa o tipo declarado de um parâmetro ou retorno."""

    type: Literal["number", "string", "boolean", "integer", "array", "object"]


class FunctionDefinition(BaseModel):
    """Representa uma função disponível e sua assinatura."""

    name: str
    description: str
    parameters: dict[str, TypeDefinition]
    returns: TypeDefinition


def validate_prompts(data: object) -> list[PromptInput]:
    """Valida a lista de pedidos carregada do JSON."""
    adapter = TypeAdapter(list[PromptInput])
    return adapter.validate_python(data)


def validate_functions(data: object) -> list[FunctionDefinition]:
    """Valida a lista de definições carregada do JSON."""
    adapter = TypeAdapter(list[FunctionDefinition])
    functions = adapter.validate_python(data)

    if not functions:
        raise ValueError("A lista de funções não pode estar vazia.")

    names = [function.name for function in functions]

    if len(names) != len(set(names)):
        raise ValueError("Os nomes das funções não podem se repetir.")

    return functions
