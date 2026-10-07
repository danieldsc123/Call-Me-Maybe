import sys

from src.cli import parse_args
from src.file_io import read_json
from src.schemas import validate_functions, validate_prompts


def main() -> int:
    """Lê as entradas, valida pedidos e retorna o código de saída."""
    args = parse_args()
    try:
        functions_data = read_json(args.functions_definition)
        functions = validate_functions(functions_data)
        data = read_json(args.input)
        prompts = validate_prompts(data)
    except ValueError as exc:
        print(f"Erro: {exc}", file=sys.stderr)
        return 1

    print(
        f"{len(functions)} funções e {len(prompts)} pedidos "
        "validados com sucesso. Processamento ainda não implementado."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
