'Test the primary configurator interface, Delivery.'
from unittest import TestCase
from marrow.mailer.exc import DeliveryFailedException as D
def A():C='reason';B='message';A=D(B,C);assert A.msg==B;assert A.reason==C;assert A.args[0]==B;assert A.args[1]==C