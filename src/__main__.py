import sys

from src.cli import parse_args
from src.file_io import read_json


def main() -> int:
    """Lê as entradas e retorna zero no sucesso ou um em caso de erro."""
    args = parse_args()
    try:
        read_json(args.functions_definition)
        read_json(args.input)
    except ValueError as exc:
        print(f"Erro: {exc}", file=sys.stderr)
        return 1

    print(
        "Arquivos JSON lidos com sucesso. "
        "Processamento ainda não implementado."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
