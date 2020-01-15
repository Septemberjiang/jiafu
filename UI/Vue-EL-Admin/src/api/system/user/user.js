import request from '@/utils/request'

export function fetchList(query) {
  return request({
    url: '/vue-admin-template/userManage/list',
    method: 'get',
    params: query
  })
}

export function fetchArticle(id) {
  return request({
    url: '/vue-admin-template/userManage/detail',
    method: 'get',
    params: { id }
  })
}

export function fetchPv(pv) {
  return request({
    url: '/vue-admin-template/userManage/pv',
    method: 'get',
    params: { pv }
  })
}

export function createArticle(data) {
  console.log(data, 'ddddddddddddddd')
  return request({
    url: '/vue-admin-template/userManage/create',
    method: 'post',
    data
  })
}

export function updateArticle(data) {
  return request({
    url: '/vue-admin-template/userManage/update',
    method: 'post',
    data
  })
}
