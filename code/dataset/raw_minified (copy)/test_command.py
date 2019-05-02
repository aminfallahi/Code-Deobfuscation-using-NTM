from django.core import management as B
from mock import patch
from six import StringIO as C
@patch('graphene.contrib.django.management.commands.graphql_schema.Command.save_file')
def A(savefile_mock,settings):settings.GRAPHENE_SCHEMA='graphene.contrib.django.tests.test_urls';A=C();B.call_command('graphql_schema',schema='',stdout=A);assert'Successfully dumped GraphQL schema to schema.json'in A.getvalue()