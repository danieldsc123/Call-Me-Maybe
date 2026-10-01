import json
from pathlib import Path


def read_json(path: str) -> object:
    """Lê JSON em UTF-8 e retorna seu conteúdo.

    Args:
        path: Caminho do arquivo de entrada.

    Returns:
        Conteúdo JSON convertido em objetos Python.

    Raises:
        ValueError: Se o arquivo não puder ser lido ou contiver JSON inválido.
    """
    file_path = Path(path)

    try:
        with file_path.open("r", encoding="utf-8") as file:
            data: object = json.load(file)
    except FileNotFoundError as exc:
        raise ValueError(f"Arquivo não encontrado: {path}") from exc
    except PermissionError as exc:
        raise ValueError(f"Sem permissão para ler o arquivo: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"JSON inválido em {path}, linha {exc.lineno}, "
            f"coluna {exc.colno}: {exc.msg}"
        ) from exc
    except UnicodeDecodeError as exc:
        raise ValueError(f"O arquivo não está em UTF-8: {path}") from exc
    except (OSError, ValueError) as exc:
        raise ValueError(f"Não foi possível ler {path}: {exc}") from exc

    return data
