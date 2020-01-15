import request from '@/utils/request'

export function fetchList(query) {
  return request({
    url: '/vue-admin-template/parameter/list',
    method: 'get',
    params: query
  })
}

export function fetchArticle(id) {
  return request({
    url: '/vue-admin-template/parameter/detail',
    method: 'get',
    params: { id }
  })
}

export function fetchPv(pv) {
  return request({
    url: '/vue-admin-template/parameter/pv',
    method: 'get',
    params: { pv }
  })
}

export function createArticle(data) {
  console.log(data, 'ddddddddddddddd')
  return request({
    url: '/vue-admin-template/parameter/create',
    method: 'post',
    data
  })
}

export function updateArticle(data) {
  return request({
    url: '/vue-admin-template/parameter/update',
    method: 'post',
    data
  })
}
