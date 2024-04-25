from fastapi import APIRouter

route = APIRouter()


@route.post("/ticket")
async def open_ticket():
    ...


@route.delete("/ticket")
async def close_ticket():
    ...


@route.put("ticket")
async def att_ticket():
    ...


@route.get("/ticket/{id}")
async def read_ticket():
    ...


@route.get("/ticket")
async def read_tickets():
    ...
