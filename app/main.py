from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, UUID4
from typing import Optional
from .services.data_loader import read_data_file
from cachetools import LRUCache


app = FastAPI()
data = read_data_file()

class KeyValueResponse(BaseModel):
    key: UUID4
    value: str

PARTITION_SIZE = 1000  # Define the number of keys per partition
NUM_PARTITIONS = (len(data) // PARTITION_SIZE) + 1

partitions = [{} for _ in range(NUM_PARTITIONS)]
for key, value in data.items():
    partition_idx = int(key.replace('-', ''), 16) % NUM_PARTITIONS  # Use modulo to wrap the index
    partitions[partition_idx][key] = value

# Define an LRU cache for each partition
partition_caches = [LRUCache(maxsize=1000) for _ in range(NUM_PARTITIONS)]
    
@app.get("/get_value/{key}", response_model=Optional[KeyValueResponse])
async def get_value(key: UUID4):
    partition_idx = int(str(key).replace('-', ''), 16) % NUM_PARTITIONS  # Use modulo to wrap the index
    partition = partitions[partition_idx]
    cache = partition_caches[partition_idx]
    cached_value = cache.get(str(key))
    if cached_value:
        return KeyValueResponse(key=key, value=cached_value)
    value = partition.get(str(key))
    if value:
        cache[str(key)] = value
        return KeyValueResponse(key=key, value=value)
    else:
        raise HTTPException(status_code=404, detail="Key not found")