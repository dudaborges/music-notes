NOTAS = 'C C# D D# E F F# G G# A A# B'.split()
ESCALAS = {'maior': (0, 2, 4, 5, 7, 9, 11), 'menor': (0, 2, 3, 5, 7, 8, 10)}


def escala(tonica: str, tonalidade: str) -> dict[str, list[str]]:
    """
    Gera uma escala a partir de uma tônica e uma tonalidade.

    Args:
        tonica: Nota que será a tônica da escala
        tonalidade: Tonalidade da escala

    Returns:
        Um dicionário com as notas da escala e os graus

    Raises:
        ValueError: Caso a tônica não seja uma nota válida
        KeyError: Caso a escala não exista ou não tenha sido implementada

    Examples:
        >>> escala('A', 'maior')
        {'notas': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """
    tonica = tonica.upper()
    try:
        intervalos = ESCALAS[tonalidade]
        tonica_posicao = NOTAS.index(tonica)
    except ValueError:
        raise ValueError(f'Essa nota não existe, tente uma dessas {NOTAS}')
    except KeyError:
        raise KeyError(
            'Essa escala não existe ou não foi implementada. '
            f'Tente uma dessas {list(ESCALAS.keys())}'
        )

    temp = []

    for intervalo in intervalos:
        index_nota = (tonica_posicao + intervalo) % 12
        temp.append(NOTAS[index_nota])

    return {'notas': temp, 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
