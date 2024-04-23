from constantes import *


def creation_notes():
    pages = notion.databases.query("a506dc25223d485aa95ee0b63ae773e0").get("results")

    notes_pages_properties = dict(notion.databases.retrieve("a506dc25223d485aa95ee0b63ae773e0")["properties"])
    print(notes_pages_properties)

    for grade in client.periods[2].grades:
        print(subject_dict[str(grade.subject.name)][0], "-", grade.comment, ":", grade.grade, "/", grade.out_of)
        parent = {"database_id": "a506dc25223d485aa95ee0b63ae773e0"}
        icon = {"type": "emoji", "emoji": subject_dict[grade.subject.name][1]}
        properties = {
            "Description": {"rich_text": [{"text": {"content": grade.comment}}]},
            "Note": {"rich_text": [{"text": {"content": str(grade.grade) + "/" + str(grade.out_of)}}]},
            "Matière": {"title": [{"text": {"content": (str(subject_dict[grade.subject.name][0]))}}]},
            "Date": {"date": {"start": str(grade.date)}}
        }
        #  Le devoir existe-il déjà dans la base de données ?
        for database_page in pages:
            if database_page["properties"]["Description"]["rich_text"][0]["text"]["content"] == properties["Description"]["rich_text"][0]["text"]["content"]:
                already_exists = True
                break
        page = notion.pages.create(parent=parent, icon=icon, properties=properties)
    print("Moyenne générale :", client.periods[2].overall_average)
