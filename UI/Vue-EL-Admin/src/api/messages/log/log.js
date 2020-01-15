import request from '@/utils/request'

export function fetchList(query) {
  return request({
    url: '/vue-admin-template/log/list',
    method: 'get',
    params: query
  })
}

export function fetchArticle(id) {
  return request({
    url: '/vue-admin-template/log/detail',
    method: 'get',
    params: { id }
  })
}

export function fetchPv(pv) {
  return request({
    url: '/vue-admin-template/log/pv',
    method: 'get',
    params: { pv }
  })
}

export function createArticle(data) {
  console.log(data, 'ddddddddddddddd');
  return request({
    url: '/vue-admin-template/log/create',
    method: 'post',
    data
  })
}

export function updateArticle(data) {
  return request({
    url: '/vue-admin-template/log/update',
    method: 'post',
    data
  })
}
