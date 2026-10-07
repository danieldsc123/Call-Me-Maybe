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
