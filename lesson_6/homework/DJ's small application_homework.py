from pprint import pprint

tiesto = {
    "name": "Tiesto",
    "age": 55,
    "equipment": "Pioneer",
    "discography": 20,
    "salary": 30_000,
    "genre": "lite-house",
}
avicci = {
    "name": "Avicci",
    "age": 22,
    "equipment": "Pioneer",
    "discography": 40,
    "salary": 0,
    "genre": "adm",
}
anna = {
    "name": "Anna",
    "age": 24,
    "equipment": "Synth",
    "discography": 3,
    "salary": 3_000,
    "genre": "techno",
}


def validate_dj_data(data):
    if len(data) != 6:
        print("The number of arguments is not correct!")
        return None

    if data[0].isdigit():
        print(f"{data[0]} is digit")
        return None

    for element in [data[1], data[3], data[4]]:
        index = data.index(element)
        if element.isdigit():
            data[index] = int(element)
        else:
            print(f"{element} is not a digit")
            return None

    if not data[5].isalnum():
        print(f"{data[5]} is not an alnum")
        return None

    return data


def add_dj(data):
    user_input = input("Enter new DJ's data: ")
    dj_data = user_input.split(",")
    validated_data = validate_dj_data(dj_data)

    if validated_data is not None:
        new_dj_data = {
            "name": validated_data[0],
            "age": validated_data[1],
            "equipment": validated_data[2],
            "discography": validated_data[3],
            "salary": validated_data[4],
            "genre": validated_data[5],
        }
        data.append(new_dj_data)
        return new_dj_data


def delete_dj(data):
    del_dj_name = input("Enter the DJ's name: ")
    dj_names_list = [dj["name"] for dj in djs]
    s = 0
    for dj_name in dj_names_list:
       if dj_name == del_dj_name:
          data.pop(s)
          print(f"DJ {dj_name} removed!")
       else:
           s += 1
    if del_dj_name not in dj_names_list:
        print("DJ is not found!")
        return None
    return data


def renew_dj(data):
    update_dj_name = input("Enter the name of the DJ whose data you want to update: ")
    dj_names_list = [dj["name"] for dj in djs]
    s = 0
    for dj_name in dj_names_list:
        if dj_name == update_dj_name:
            data.pop(s)
            print("DJ input format: name,age,equipment,discography,salary,genre")
            user_input = input("Enter new DJ's data: ")
            dj_data = user_input.split(",")
            validated_data = validate_dj_data(dj_data)

            if validated_data is not None:
                renew_dj_data = {
                    "name": validated_data[0],
                    "age": validated_data[1],
                    "equipment": validated_data[2],
                    "discography": validated_data[3],
                    "salary": validated_data[4],
                    "genre": validated_data[5],
                }
                data.append(renew_dj_data)
                return renew_dj_data
        else:
            s += 1
    if update_dj_name not in dj_names_list:
        print("DJ is not found!")
        return None
    return data






if __name__ == "__main__":
    djs = [tiesto, avicci, anna]
    allowed_options = "[add/delete/update/list/names/exit]"

    while True:
        desision = input(f"What should I do?{allowed_options}: ")
        if desision == "add":
            print("DJ input format: name,age,equipment,discography,salary,genre")
            new_dj = add_dj(djs)
            if new_dj:
                print(f"DJ {new_dj['name']} is added!")
        elif desision == "delete":
            print("Which DJ do you want to remove?")
            removed_dj = delete_dj(djs)
        elif desision == "update":
            updated_dj = renew_dj(djs)
            if updated_dj:
                print(f"DJ {updated_dj['name']} is update!")
        elif desision == "list":
            pprint(djs)
        elif desision == "names":
            data = [dj["name"] for dj in djs]
            pprint(data)
        elif desision == "exit":
            print("Exiting...")
            break
        else:
            print(f"Please use allowed options! {allowed_options}")