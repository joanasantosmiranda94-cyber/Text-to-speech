import re


def clean_text(raw_text: str) -> str:
    text = raw_text

    # Remove hífens de quebra de linha (ex: exa-\nmple → example)
    text = re.sub(r"-\n", "", text)

    # Substitui quebras de linha simples por espaço
    text = re.sub(r"(?<!\n)\n(?!\n)", " ", text)

    # Normaliza parágrafos (máx 2 \n)
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Remove múltiplos espaços
    text = re.sub(r"[ \t]{2,}", " ", text)

    # Remove espaços antes de pontuação
    text = re.sub(r"\s+([.,!?;:])", r"\1", text)

    # Remove referências simples [12], [1], [23]
    text = re.sub(r"\[\d+\]", "", text)

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    return text.strip()