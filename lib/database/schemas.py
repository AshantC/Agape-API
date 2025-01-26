def individual(data):
    return {
        "id": str(data["_id"]),
        "name": data["name"],
        "email": data["email"],
        "phone_number": data["phone_1"],
        "alternate_number": data["phone_2"],
        "description": data["description"],
        "price": data["price"],
        "address": data["address"],
        "status": data["is_completed"]
    }
    
def all_info(datas):
    return [individual(data) for data in datas]

def info_by_id(datas, data_id):
    for data in datas:
        if data["_id"] == data_id:
            return individual(data)