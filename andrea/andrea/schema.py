import graphene

import andreaapp.schema


class Query(ingredients.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
