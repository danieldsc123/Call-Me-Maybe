import math


def mask_logits(
    logits: list[float],
    allowed_ids: set[int],
) -> list[float]:
    """Bloqueia os tokens que não estão entre os IDs permitidos."""
    if not allowed_ids:
        raise ValueError("Nenhum token permitido para continuar a geração.")
    if any(index < 0 or index >= len(logits) for index in allowed_ids):
        raise ValueError("ID de token permitido fora da lista de logits.")

    return [
        score if index in allowed_ids else float("-inf")
        for index, score in enumerate(logits)
    ]


def select_next_token(
    logits: list[float],
    allowed_ids: set[int],
) -> int:
    """Seleciona o próximo token com base nos logits mascarados."""
    masked_logits = mask_logits(logits, allowed_ids)
    best_id: int | None = None
    best_score = float("-inf")

    for token_id, score in enumerate(masked_logits):
        if math.isfinite(score) and score > best_score:
            best_id = token_id
            best_score = score

    if best_id is None:
        raise ValueError("Nenhum token permitido possui pontuação finita.")

    return best_id
