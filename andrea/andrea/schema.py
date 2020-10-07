import graphene

import website.schema
import andreaapp.schema


class Query(website.schema.Query, graphene.ObjectType):
    
    pass

class Query(andreaapp.schema.Query, graphene.ObjectType):
    
    pass

schema = graphene.Schema(query=Query)