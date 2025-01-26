from fastapi import FastAPI, APIRouter, HTTPException
# from configurations import collection
from .database.schemas import all_info, info_by_id
from bson.objectid import ObjectId
from .database.models import ClientDetails
from datetime import datetime
from .configurations import collection

app = FastAPI()
router = APIRouter()

@router.get("/")
async def get_all_data():
    try:
        
        data = collection.find({"is_deleted":False})
        return {"status_code": 200, "data": all_info(data)}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured: {e}")
    
@router.get("/{data_id}")
async def get_all_data(data_id: str):
    try:
        data = collection.find({"is_deleted":False})
        id = ObjectId(data_id)
        existing_data = collection.find_one({"_id": id, "is_deleted":False})
        if not existing_data:
            return HTTPException(status_code=404, detail="Data not found")
        return {"status_code": 200, "data": info_by_id(data, id)}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured: {e}")

@router.post("/")
async def create_data(new_data: ClientDetails):
    try:
        resp = collection.insert_one(dict(new_data))
        return {"status_code":200, "id": str(resp.inserted_id)}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured: {e}")
    
@router.put("/{data_id}")
async def update_data(data_id: str, updated_data: ClientDetails):
    try:
        # Convert data_id to ObjectId
        object_id = ObjectId(data_id)

        # Check if the data exists and is not deleted
        existing_data = collection.find_one({"_id": object_id, "is_deleted": False})
        if not existing_data:
            raise HTTPException(status_code=404, detail="Data does not exist.")

        # Update the updated_at field
        updated_data_dict = updated_data.dict(exclude_unset=True)
        updated_data_dict["updated_at"] = datetime.now()

        # Update the document in the collection
        result = collection.update_one({"_id": object_id}, {"$set": updated_data_dict})
        if result.modified_count == 0:
            raise HTTPException(status_code=400, detail="No changes made to the data.")

        return {"status_code": 200, "message": "Data updated successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Some error occurred: {str(e)}")
    
@router.delete("/{data_id}")
async def delete_data(data_id: str):
    try:
        id = ObjectId(data_id)
        existing_data = collection.find_one({"_id":id, "is_deleted":False})
        if not existing_data:
            return HTTPException(status_code=404, detail="Data does not exist")
        resp = collection.update({"_id":id}, {"$set":{"is_deleted": True}})
        return {"status_code": 200, "message": f"ID: {id} deleted successfully."}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured: {e}")

app.include_router(router)


