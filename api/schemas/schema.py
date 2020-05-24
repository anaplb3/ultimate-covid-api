import graphene
from api.service.case_service import CaseService
from datetime import date


class Case(graphene.ObjectType):
    regiao = graphene.String()
    estado = graphene.String()
    municipio = graphene.String()
    cod_mun = graphene.Int()
    cod_uf = graphene.Int()
    #data_registro = graphene.Date()
    casos = graphene.Int()
    obitos = graphene.Int()
    recuperados = graphene.Int()
    acompanhamento = graphene.Int()


class Query(graphene.ObjectType):

    cases = graphene.Field(
        graphene.List(Case), date=graphene.String(), offset=graphene.Int(), limit=graphene.Int()
    )

    cases_per_city = graphene.Field(
        Case, date=graphene.String(), city=graphene.String(), state=graphene.String())

    cases_per_region = graphene.Field(Case, region=graphene.String())

    cases_per_state = graphene.Field(
        graphene.List(Case), state=graphene.String(),
        offset=graphene.Int(), limit=graphene.Int(),
        date=graphene.String()
    )

    cases_per_date = graphene.Field(
        graphene.List(Case), start_date=graphene.String(),
        end_date=graphene.String(), offset=graphene.Int(),
        limit=graphene.Int()
    )

    def resolve_cases(self, info, date, offset, limit):
        service = CaseService()
        result = service.get_cases(offset, limit, date)
        return create_obj(result)

    def resolve_cases_per_city(self, info, date, city, state):
        service = CaseService()
        result = service.get_case_per_city(date, city, state)
        return create_obj(result)

    def resolve_cases_per_region(self, info, region):
        service = CaseService()
        result = service.get_cases_per_region(region)
        return create_obj(result)

    def resolve_cases_per_state(self, info, date, state, offset, limit):
        service = CaseService()
        print("args = {}, {}, {}, {}".format(date, state, offset, limit))
        result = service.get_cases_per_state(date, state, offset, limit)
        print("RESULT = {}".format(result))
        return create_obj(result)

    def resolve_cases_per_date(self, info, start_date, end_date, offset, limit):
        service = CaseService()
        result = service.get_cases_per_date(
            start_date, end_date, offset, limit)
        return create_obj(result)


schema = graphene.Schema(query=Query)


def create_obj(cases):
    try:
        if(len(cases) > 1):
            results = []
            for i in range(len(cases)):
                results.append(
                    Case(cases[i][0], cases[i][1], cases[i][2], cases[i][3],
                         cases[i][4], cases[i][5], cases[i][6], cases[i][7],
                         cases[i][8])
                )
            return results
        else:
            print("CASE = {}".format(cases))
            case = Case(cases[0][0], cases[0][1], cases[0][2], cases[0][3],
                        cases[0][4], cases[0][5], cases[0][6], cases[0][7],
                        cases[0][8])
            return case
    except:
        return None
