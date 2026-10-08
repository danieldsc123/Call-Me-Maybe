from llm_sdk import Small_LLM_Model

from src.file_io import read_json


def load_model() -> Small_LLM_Model:
    """Carrega o modelo padrão usando o SDK fornecido."""
    return Small_LLM_Model()


def load_vocabulary(model: Small_LLM_Model) -> dict[str, int]:
    """Lê e valida o vocabulário pela interface pública do SDK."""
    path: str = model.get_path_to_vocab_file()
    data = read_json(path)
    if not isinstance(data, dict):
        raise ValueError("O vocabulário deve ser um objeto JSON.")
    if not data:
        raise ValueError("O vocabulário não pode estar vazio.")

    vocabulary: dict[str, int] = {}
    for token, token_id in data.items():
        if not isinstance(token, str):
            raise ValueError("As chaves do vocabulário devem ser textos.")
        if (
            not isinstance(token_id, int)
            or isinstance(token_id, bool)
            or token_id < 0
        ):
            raise ValueError(
                f"ID inválido para o token {token!r}: "
                "esperado um inteiro não negativo."
            )
        vocabulary[token] = token_id

    return vocabulary
