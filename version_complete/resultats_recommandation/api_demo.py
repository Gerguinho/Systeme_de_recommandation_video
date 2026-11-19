
"""API locale de démonstration. Ne pas exposer telle quelle sur Internet."""
import json
from pathlib import Path
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs
import numpy as np
ROOT = Path(__file__).resolve().parent
class Recommender:
    def __init__(self, path=ROOT/'modele_demo.npz'):
        with np.load(path, allow_pickle=False) as data:
            self.users=data['users']; self.items=data['items']; self.scores=data['scores']
            self.seen=data['seen']; self.pop=data['popularity']
        self.lookup={int(u):i for i,u in enumerate(self.users)}
    def recommend(self, user_id, k=10, seen=()):
        if not 1 <= k <= 100: raise ValueError('k doit être entre 1 et 100')
        u=self.lookup.get(int(user_id))
        scores=self.pop if u is None else self.scores[u]
        available=np.ones(len(self.items),bool) if u is None else ~self.seen[u].copy()
        available &= ~np.isin(self.items,list(seen))
        candidates=np.flatnonzero(available)
        order=np.lexsort((self.items[candidates],-scores[candidates]))
        videos=self.items[candidates[order[:k]]].astype(int).tolist()
        return {'user_id':int(user_id),'video_ids':videos,'nombre_retourne':len(videos),
                'mode':'repli_popularite' if u is None else 'modele_selectionne'}

def traiter(path, service):
    """Route pure, testable sans connexion réseau."""
    url=urlparse(path)
    if url.path=='/health': return 200, {'status':'ok'}
    if url.path!='/recommendations': return 404, {'error':'Route inconnue'}
    try:
        q=parse_qs(url.query)
        uid=int(q['user_id'][0]); k=int(q.get('k',['10'])[0])
        seen=[int(x) for x in q.get('seen',[''])[0].split(',') if x]
        return 200, service.recommend(uid,k,seen)
    except (KeyError,ValueError,TypeError):
        return 400, {'error':'Paramètres invalides : user_id entier, k entre 1 et 100, seen IDs séparés par virgules'}

if __name__=='__main__':
    service=Recommender()
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            status,payload=traiter(self.path,service)
            body=json.dumps(payload,ensure_ascii=False).encode('utf-8')
            self.send_response(status)
            self.send_header('Content-Type','application/json; charset=utf-8')
            self.send_header('Content-Length',str(len(body)))
            self.end_headers(); self.wfile.write(body)
    server=ThreadingHTTPServer(('127.0.0.1',8000),Handler)
    print('API locale : http://127.0.0.1:8000 ; arrêt Ctrl+C')
    try: server.serve_forever()
    except KeyboardInterrupt: server.server_close()
