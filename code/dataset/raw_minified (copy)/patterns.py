def A(*A,**B):C=dict(zip(A,range(len(A))),**B);return type('Enum',(),C)