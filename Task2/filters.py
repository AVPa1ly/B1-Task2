import decimal

from app import app


@app.template_filter()
def table_cell(value):
    if isinstance(value, (decimal.Decimal, float)):
        return round(value, 2)
    return value
