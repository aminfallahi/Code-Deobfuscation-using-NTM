from ..  import vsreenqueue as A,trigger_pull,is_down
def enqueue(fsq_id,trg_queue,data):' Enqueue an item pushed from a remote client ';return A(fsq_id,data,[trg_queue])
__all__=['enqueue','trigger_pull','is_down']