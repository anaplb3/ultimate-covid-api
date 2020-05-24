import psycopg2
from datetime import datetime, timedelta
from database.read_data import create_connection


class CaseService:
    def __init__(self):
        self.date_class = self.processing_date("")
        self.connection = create_connection()

    def processing_date(self, date):
        if date == None or date == "":
            date = datetime.today() - timedelta(days=1)
            date = str(date.strftime("%Y-%m-%d"))
        return date

    def get_cases(self, offset, limit, date):
        cursor = self.connection.cursor()

        date = self.processing_date(date)

        query = """SELECT regiao, estado, municipio, cod_mun, cod_uf,
        casos_acumulados, obitos_acumulados, recuperados_novos,
        em_acompanhamento  
        FROM cases 
        WHERE data_registro = '{}'
        ORDER BY regiao
        OFFSET {} LIMIT {}""".format(date, offset, limit)

        cursor.execute(query)
        result = list(cursor.fetchall())

        cursor.close()
        return self.processing_query(result)

    def processing_query(self, result):
        cases = []
        final_cases = []

        for a in result:
            cases.append(list(a))

        for i in range(len(cases)):
            final_cases.append(cases[i])

        return final_cases

    def get_available_states(self):
        cursor = self.connection.cursor()

    def get_case_per_city(self, date, city, state):
        cursor = self.connection.cursor()

        date = self.processing_date(date)

        print("date = {}".format(date))

        query = """SELECT regiao, estado, municipio, cod_mun, cod_uf, 
        casos_acumulados, obitos_acumulados, recuperados_novos,
        em_acompanhamento  
        FROM cases 
        WHERE data_registro = '{}' AND municipio = '{}'
        AND estado = '{}'""".format(date, city, state)

        cursor.execute(query)
        result = list(cursor.fetchall())

        cursor.close()
        return self.processing_query(result)

    def get_cases_per_region(self, region):
        cursor = self.connection.cursor()

        query = """SELECT regiao, estado, municipio, cod_mun, cod_uf,
        casos_acumulados, obitos_acumulados, recuperados_novos,
        em_acompanhamento 
        FROM cases 
        WHERE data_registro = '{}' AND regiao = '{}'""".format(self.date_class, region)

        cursor.execute(query)
        result = list(cursor.fetchall())

        print(result[0])

        cursor.close()
        return self.processing_query(result)

    def get_cases_per_state(self, date, state, offset, limit):
        cursor = self.connection.cursor()

        date = self.processing_date(date)

        query = """SELECT regiao, estado, municipio, cod_mun, cod_uf, 
        casos_acumulados, obitos_acumulados, recuperados_novos,
        em_acompanhamento 
        FROM cases 
        WHERE data_registro = '{}' AND estado = '{}'
        ORDER BY regiao
        OFFSET {} LIMIT {}""".format(date, state, offset, limit)

        cursor.execute(query)
        result = list(cursor.fetchall())

        cursor.close()
        return self.processing_query(result)

    def get_cases_per_date(self, start_date, end_date, offset, limit):
        cursor = self.connection.cursor()

        query = """SELECT regiao, estado, municipio, cod_mun, cod_uf, 
        casos_acumulados, obitos_acumulados, recuperados_novos,
        em_acompanhamento 
        FROM cases
        WHERE data_registro BETWEEN '{}' and '{}'
        ORDER BY regiao
        OFFSET {} LIMIT {} 
        """.format(start_date, end_date, offset, limit)

        cursor.execute(query)
        result = list(cursor.fetchall())

        cursor.close()
        return self.processing_query(result)
