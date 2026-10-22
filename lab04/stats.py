def parse_record(line: str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError("Неверное число полей")
    city, temp, date = (p.strip() for p in parts)
    if not city or not date:
        raise ValueError("Пустой город или дата")
    try:
        temp = float(temp.replace(",", "."))
    except ValueError:
        raise ValueError("Температура не число")
    return {"city": city, "temperature": temp, "date": date}

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


def average_by_city(records: list[dict]) -> dict:
    total = {}
    count = {}
    for rec in records:
        city = rec["city"]
        total[city] = total.get(city, 0.0) + rec["temperature"]
        count[city] = count.get(city, 0) + 1
    return {c: round(total[c]/count[c], 1) for c in total}

def warmest_city(records: list[dict]) -> str:
    total = {}
    count = {}
    for rec in records:
        city = rec["city"]
        total[city] = total.get(city, 0.0) + rec["temperature"]
        count[city] = count.get(city, 0) + 1
    averages = {c: total[c] / count[c] for c in total}
    return min(averages, key=lambda c: (-averages[c], c))