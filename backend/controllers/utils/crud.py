# DEPRECATED: probably useless

from typing import Optional

from pydantic import BaseModel
from flask import Blueprint, request
from spectree import Response

from factory import api, db
from . import wrap_resp, req_perms
from models.utils.responses import DefaultResp

NPPAGE: int = 64

class RouteInfo(BaseModel):
  resp: Optional[BaseModel] = None
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
    @api.validate(json=info.req, resp=Response(HTTP_201=DefaultResp), **fixed_params)
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
    @bp.get('/<id:int>')
    @wrap_resp
    @req_perms(info.perms)
    def crud_read(id: int):
      el = info.model.query.filter_by(id=id).first()
      if not el:
        return 'ID not found', 404
      return info.resp.model_validate(el).model_dump(), 200

  else if type == 'Q':
    @api.validate(query=info.req, resp=Response(HTTP_200=info.resp), **fixed_params)
    @bp.get('/<page:int>')
    @wrap_resp
    @req_perms(info.perms)
    def crud_read(page: int):
      q = info.model.query
      for key in info.req.fields.keys():
        v = request.get(key)
        if v is not None:
          q = q.filter_by(**{key: v})
      res = db.paginate(q, page=page, per_page=NPPAGE).items
      return info.resp.model_validate(**{info.resp.fields.keys()[0]: el}).model_dump(), 200

  else if type == 'U':
    @api.validate(json=info.req, resp=Response(HTTP_200=DefaultResp, HTTP_400=DefaultResp), **fixed_params)
    @bp.get('/<id:int>')
    @wrap_resp
    @req_perms(info.perms)
    def crud_read(id: int):
      el = info.model.query.filter_by(id=id).first()
      if not el:
        return 'ID not found', 404
      q = info.model.query()
      for key in info.req.fields.keys():
        v = request.get(key)
        if v is not None:
          el.
      res = db.paginate(q, page=page, per_page=NPPAGE).items
      return 'Updated successfully!', 200

  else if type == 'D':

def make_crud(bp: Blueprint, tag: str, routes: dict[str, RouteInfo]):
  for type, info in routes:
    make_crud_el(bp, tag, type, info)
