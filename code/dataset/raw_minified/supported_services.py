from django.shortcuts import render as B,redirect
def A(req):A=req;return B(A,'supported-services-poll.html',{'voter_key':A.user['_id']if A.user else''})