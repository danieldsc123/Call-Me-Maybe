from llm_sdk import Small_LLM_Model


def load_model() -> Small_LLM_Model:
    """Carrega o modelo padrão usando o SDK fornecido."""
    return Small_LLM_Model()
