import request from '@/utils/request'

export function getServerList(query) {
  return request({
    url: '/device/server',
    method: 'get',
    params: query
  })
}

export function getServerDetail(id) {
  return request({
    url: '/device/server/'+ id,
    method: 'get'
  })
}

export function addServer(data) {
  return request({
    url: '/device/server',
    method: 'post',
    data
  })
}

export function editServer(data,id) {
  return request({
    url: '/device/server/' + data.id,
    method: 'PUT',
    data
  })
}

export function deleteServer(id) {
  return request({
    url: '/device/server/' + id,
    method: 'DELETE'
  })
}
