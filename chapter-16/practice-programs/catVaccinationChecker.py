from os import error
import sqlite3, pprint

conn = sqlite3.connect('sweigartcats.db', isolation_level=None)

unvaccinated_cats = conn.execute('SELECT * FROM cats INNER JOIN vaccinations ON cats.rowid = vaccinations.cat_id WHERE vaccine NOT IN ("rabies", "FeLV", "FVRCP")').fetchall()

print('Unvaccinated Cats:')
pprint.pprint(unvaccinated_cats)

erroneous_vaccinations = conn.execute('SELECT * FROM cats INNER JOIN vaccinations ON cats.rowid = vaccinations.cat_id WHERE birthdate > date_administered').fetchall()

print('Erroneous Vaccinations:')
pprint.pprint(erroneous_vaccinations)
