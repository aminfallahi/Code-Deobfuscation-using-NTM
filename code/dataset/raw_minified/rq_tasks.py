from django_rq import job
@job
def A(klass_str,obj_args,obj_kwargs,call_args,call_kwargs):from .base import Job;Job.job_refresh(klass_str,obj_args,obj_kwargs,call_args,call_kwargs)