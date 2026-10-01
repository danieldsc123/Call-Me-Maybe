import argparse


def parse_args() -> argparse.Namespace:
    """Interpreta os argumentos da linha de comando."""
    parser = argparse.ArgumentParser(
        description=(
            "Transforma pedidos em linguagem natural "
            "em chamadas de função."
        )
    )
    parser.add_argument(
        "--functions_definition",
        default="data/input/functions_definition.json",
        help="Caminho do arquivo com as definições das funções.",
    )
    parser.add_argument(
        "--input",
        default="data/input/function_calling_tests.json",
        help="Caminho do arquivo com os pedidos a processar.",
    )
    parser.add_argument(
        "--output",
        default="data/output/function_calls.json",
        help="Caminho do arquivo onde salvar os resultados.",
    )
    return parser.parse_args()
