def parse_record(line: str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError("Неверное число полей")
    city, temp, date = (p.strip() for p in parts)
    if not city or not date:
        raise ValueError("Пустой город или дата")
    try:
        temp = float(temp)
    except ValueError:
        raise ValueError("Температура не число")
    return {"city": city, "temp": temp, "date": date}

def read_valid(lines: list[str]) -> list[dict]:
    records = []
    for line in lines:
        if not line.strip():
            continue
        try:
            records.append(parse_record(line))
        except ValueError:
            continue
    return records