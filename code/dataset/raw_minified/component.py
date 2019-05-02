from .object import Object as C,field as A
class B(C):game_object=A('m_GameObject')
class D(B):enabled=A('m_Enabled',bool)
class E(B):position=A('m_LocalPosition');rotation=A('m_LocalRotation');scale=A('m_LocalScale');parent=A('m_Father');children=A('m_Children')