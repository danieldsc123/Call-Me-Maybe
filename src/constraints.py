def can_extend_literal(
    current: str,
    fragment: str,
    expected: str,
) -> bool:
    """Verifica se o fragmento mantém o prefixo do texto esperado."""
    if not fragment:
        return False

    candidate = current + fragment
    return expected.startswith(candidate)


def can_extend_choice(
    current: str,
    fragment: str,
    expected: list[str],
) -> bool:
    """Verifica se o fragmento pode continuar uma das escolhas."""
    return any(
        can_extend_literal(current, fragment, choice)
        for choice in expected
    )


def allowed_choice_ids(
    current: str,
    token_fragments: dict[int, str],
    choices: list[str],
) -> set[int]:
    """Retorna os IDs dos tokens que podem continuar uma escolha."""
    allowed: set[int] = set()

    for token_id, fragment in token_fragments.items():
        if can_extend_choice(current, fragment, choices):
            allowed.add(token_id)

    return allowed
