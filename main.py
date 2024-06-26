from imports import *


def creer_devoir_notion(homework):
    parent = {"database_id": infos_persos["database_uuid"]}
    icon = {"type": "emoji", "emoji": subject_dict[homework.subject.name][1]}
    properties = {
        "Description": {"rich_text": [{"text": {"content": homework.description}}]},
        "Matière": {"title": [{"text": {"content": subject_dict[homework.subject.name][0]}}]},
        "Date": {"date": {"start": str(homework.date)}}
    }

    already_exists = False
    for database_page in pages:
        description_devoir_notion = database_page["properties"]["Description"]["rich_text"][0]["text"]["content"]
        description_devoir_pronote = properties["Description"]["rich_text"][0]["text"]["content"]
        if description_devoir_notion == description_devoir_pronote:
            already_exists = True
            break
    if not already_exists:
        list_attachements = []
        for id_attachement in range(len(homework.files)):
            attachement = homework.files[id_attachement]
            list_attachements.append(attachement)
            if len(list_attachements) >= 1:
                if "Fichier N°" + str(id_attachement) not in database_properties:
                    notion.databases.update(infos_persos["database"],
                                            properties={"Fichier N°" + str(id_attachement): {"rich_text": {}}})
                properties["Fichier N°" + str(id_attachement)] = {'id': 'DMX%60', 'type': 'rich_text', 'rich_text': [
                    {'type': 'text', 'text': {'content': str(attachement.name), 'link': {'url': str(attachement.url)}},
                     'annotations': {'bold': False, 'italic': False, 'strikethrough': False, 'underline': False,
                                     'code': False, 'color': 'default'}, 'plain_text': 'Test',
                     'href': str(attachement.url)}]}
        page = notion.pages.create(parent=parent, icon=icon, properties=properties)


if client.logged_in:
    pages = notion.databases.query(infos_persos["database_uuid"]).get("results")
    database_properties = []
    properties = dict(notion.databases.retrieve(infos_persos["database_uuid"])["properties"])
    for key in properties.keys():
        database_properties.append(key)
    homeworks = client.homework(datetime.date.today())

    for homework in homeworks:
        creer_devoir_notion(homework)
