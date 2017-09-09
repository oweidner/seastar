import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

# from .models import Department as DepartmentModel
# from .models import Employee as EmployeeModel
# from .models import Role as RoleModel

from .models import Platform as PlatformModel
from .models import Node as NodeModel
from .models import Processor as ProcessorModel


class Platform(SQLAlchemyObjectType):

    class Meta:
        model = PlatformModel
        interfaces = (relay.Node, )

class ClusterNode(SQLAlchemyObjectType):

    class Meta:
        model = NodeModel
        interfaces = (relay.Node, )

class Processor(SQLAlchemyObjectType):

    class Meta:
        model = ProcessorModel
        interfaces = (relay.Node, )


# class Department(SQLAlchemyObjectType):
#
#     class Meta:
#         model = DepartmentModel
#         interfaces = (relay.Node, )
#
#
# class Employee(SQLAlchemyObjectType):
#
#     class Meta:
#         model = EmployeeModel
#         interfaces = (relay.Node, )
#
#
# class Role(SQLAlchemyObjectType):
#
#     class Meta:
#         model = RoleModel
#         interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_platforms = SQLAlchemyConnectionField(Platform)
    all_nodes = SQLAlchemyConnectionField(ClusterNode)
    # role = graphene.Field(Role)


schema = graphene.Schema(query=Query, types=[Platform, ClusterNode, Processor])
