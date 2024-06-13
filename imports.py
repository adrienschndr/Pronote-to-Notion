import notion_client
import pronotepy
import datetime
from subjects_dict import subject_dict
from pronotepy.ent import *
from dotenv import dotenv_values

infos_persos = dotenv_values(".env")

client = pronotepy.Client(pronote_url=infos_persos["pronote_url"],
                          username=infos_persos["username"],
                          password=infos_persos["pronote_url"],
                          ent=infos_persos["region"])

notion = notion_client.Client(auth=infos_persos["token"])
