import psycopg2
import database.settings as cfg


def create_connection():
    return psycopg2.connect(
        host=cfg.POSTGRES_CFG['host'],
        port=cfg.POSTGRES_CFG['port'],
        dbname=cfg.POSTGRES_CFG['dbname'],
        user=cfg.POSTGRES_CFG['user'],
        password=cfg.POSTGRES_CFG['pwd']
    )


def load_data():
    connection = create_connection()
    cursor = connection.cursor()

    drop_table_command = "DROP TABLE IF EXISTS cases"

    cursor.execute(drop_table_command)
    connection.commit()

    command2 = """
            CREATE TABLE cases(
                regiao VARCHAR,
                estado VARCHAR,
                municipio VARCHAR,
                cod_uf INTEGER,
                cod_mun INTEGER,
                cod_regiao_saude INTEGER,
                nome_reg_saude VARCHAR,
                data_registro date,
                semana_epi INTEGER,
                populacao INTEGER,
                casos_acumulados INTEGER,
                obitos_acumulados INTEGER,
                recuperados_novos INTEGER,
                em_acompanhamento INTEGER
            )
        """

    cursor.execute(command2)
    connection.commit()

    query_copy = "SET datestyle = mdy"

    cursor.execute(query_copy)
    connection.commit()

    with open('database\painel_covid.tsv', 'r', encoding='utf-8') as f:
        next(f)
        cursor.copy_from(f, 'cases', null="")

    connection.commit()

    connection.close()
