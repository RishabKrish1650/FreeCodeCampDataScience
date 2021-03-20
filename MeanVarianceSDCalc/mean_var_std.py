import numpy as np

def calculate(c):
  if(len(c)!=9):
    raise ValueError("List must contain nine numbers.")
  else:
    rows=np.array([c[0:3],c[3:6],c[6:9]])
    flat=np.array(c)
    calc= dict()
    calc["mean"]=[np.mean(rows,axis=0).tolist(),np.mean(rows,axis=1).tolist(), np.mean(flat).tolist()]
    calc["variance"]=[np.var(rows,axis=0).tolist(),np.var(rows,axis=1).tolist(), np.var(flat).tolist()]
    calc["standard deviation"]=[np.std(rows,axis=0).tolist(),np.std(rows,axis=1).tolist(), np.std(flat).tolist()]
    calc["max"]=[[max(i) for i in rows.transpose().tolist()],[max(i) for i in rows.tolist()],max(c)]
    calc["min"]=[[min(i) for i in rows.transpose().tolist()],[min(i) for i in rows.tolist()], min(c)]
    calc["sum"]=[[sum(i) for i in rows.transpose().tolist()],[sum(i) for i in rows.tolist()], sum(c)]
    return calc
