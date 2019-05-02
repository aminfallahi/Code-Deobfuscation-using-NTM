from django import template as A
B=A.Library()
def C(context):A=context['request'].user.get_and_delete_messages();return{'visitor_messages':A}
B.inclusion_tag('shop/_messages.html',takes_context=True)(C)