import notion_client
import pronotepy
import datetime
from subjects import subject_dict
from pronotepy.ent import ile_de_france

client = pronotepy.Client(pronote_url='https://0781951x.index-education.net/pronote/eleve.html',
                          username='schneida',
                          password='20061222Sn&*',
                          ent=ile_de_france)

notion = notion_client.Client(auth="secret_ikguoMbl0FpRwqZa4PiOjOyPC9cxi2z714HcxcJwcgM")
