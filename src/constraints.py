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
