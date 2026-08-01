from typing import Optional

from pydantic import BaseModel
from flask import Blueprint, request
from spectree import Response

from factory import api, db
from . import wrap_resp, req_perms
from models.utils.responses import DefaultResp

class RouteInfo(BaseModel):
  resp: BaseModel | None = None
  model: db.Model
  req: Optional[BaseModel] = None
  perms: Optional[list[UserPerm]] = None
  sec: bool = False

def make_crud_el(bp: Blueprint, tag: str, type: str, info: RouteInfo):
  fixed_params = {
      'tags'=[tag],
      'security' = [{'BearerAuth': []}] if info.sec else None
    }

  if type == 'C':
    @api.validate(json=info.req, resp=Response(HTTP_200=DefaultResp), **fixed_params)
    @bp.post('/')
    @wrap_resp
    @req_perms(info.perms)
    def crud_create():
      el = info.model(**(info.req.model_validate(request.get_json()).model_dump() if info.req else {}))
      db.session.add(el)
      db.session.commit()
      return 'Created successfully!', 201

  else if type == 'R':
    @api.validate(resp=Response(HTTP_200=info.resp, HTTP_400=DefaultResp), **fixed_params)
    @bp.post('/<id:int>')
    @wrap_resp
    @req_perms(info.perms)
    def crud_read(id: int):
      el = info.model.query.filter_by(id=id).first()
      if not el:
        return 'ID not found', 404
      return info.resp.model_validate(el).model_dump(), 200

  else if type == 'Q':
    @api.validate(resp=Response(HTTP_200=info.resp, HTTP_400=DefaultResp), **fixed_params)
    @bp.post('/<id:int>')
    @wrap_resp
    @req_perms(info.perms)
    def crud_read(id: int):
      el = info.model.query.filter_by(id=id).first()
      if not el:
        return 'ID not found', 404
      return info.resp.model_validate(el).model_dump(), 200

  else if type == 'U':

  else if type == 'D':

def make_crud(bp: Blueprint, tag: str, routes: dict[str, RouteInfo]):
  for type, info in routes:
    make_crud_el(bp, tag, type, info)
