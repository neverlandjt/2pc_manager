from sqlalchemy import  text
from manager import Manager

# pass valid credentials here
manager = Manager(['postgresql:///db1',
                   'postgresql://db2',
                   'postgresql://db3'])

manager.execute_all([
    text(" INSERT INTO fly VALUES ('{}');".format(
        "', '".join(['12345d', 'Nik', 'KLM 1382', 'KBP', 'AMS', '2021-11-29']))),
    text(" INSERT INTO hotel VALUES ('{}');".format(
        "', '".join(['54321d', 'Nik', 'Hilton', '2021-11-29', '2021-11-30']))),
    text(f"UPDATE account SET amount = amount- {10} WHERE client_name = '{'Nik'}'")

])
