// import Mock from 'mockjs'

// const data = Mock.mock({
//   'items|30': [{
//     device_no: '@sentence(1,2)',
//     server_name: '@sentence(1,2)',
//     server_ip: '@sentence(1,2)',
//     province: '@sentence(1,2)',
//     city: '@sentence(1,2)',
//     county: '@sentence(1,2)',
//     company: '@sentence(1,2)',
//     server_state: '@sentence(1,2)'
//     // id: '@id',
//     // title: '@sentence(10, 20)',
//     // 'status|1': ['published', 'draft', 'deleted'],
//     // author: 'name',
//     // display_time: 'name',
//     // pageviews: '@integer(300, 5000)'
//   }]
// })

// export default [
//   {
//     url: '/vue-admin-template/devices/list',
//     type: 'get',
//     response: config => {
//       const items = data.items
//       return {
//         code: 20000,
//         data: {
//           total: items.length,
//           items: items
//         }
//       }
//     }
//   }
// ]
import Mock from 'mockjs'

const List = []
const count = 100

const baseContent = '<p>I am testing data, I am testing data.</p><p><img src="https://wpimg.wallstcn.com/4c69009c-0fd4-4153-b112-6cb53d1cf943"></p>'
const image_uri = 'https://wpimg.wallstcn.com/e4558086-631c-425c-9430-56ffb46e70b3'

for (let i = 0; i < count; i++) {
  List.push(Mock.mock({
    id: '@first',
    parameter_name: '@first',
    parameter_value: '@first',
    remark: '@first',

    // title: '@title(5, 10)',
    // content_short: 'mock data',
    // content: baseContent,
    // forecast: '@float(0, 100, 2, 2)',
    // importance: '@integer(1, 3)',
    // 'type|1': ['CN', 'US', 'JP', 'EU'],
    // 'status|1': ['published', 'draft'],
    // display_time: '@datetime',
    // comment_disabled: true,
    // pageviews: '@integer(300, 5000)',
    // image_uri,
    // platforms: ['a-platform']
  }))
}

export default [
  {
    url: '/vue-admin-template/parameter/list',
    type: 'get',
    response: config => {
      const { importance, type, title, page = 1, limit = 20, sort } = config.query

      let mockList = List.filter(item => {
        if (importance && item.importance !== +importance) return false
        if (type && item.type !== type) return false
        if (title && item.title.indexOf(title) < 0) return false
        return true
      })

      if (sort === '-id') {
        mockList = mockList.reverse()
      }

      const pageList = mockList.filter((item, index) => index < limit * page && index >= limit * (page - 1))

      return {
        code: 20000,
        data: {
          total: mockList.length,
          items: pageList
        }
      }
    }
  },

  {
    url: '/vue-admin-template/parameter/detail',
    type: 'get',
    response: config => {
      const { id } = config.query
      for (const parameter of List) {
        if (parameter.id === +id) {
          return {
            code: 20000,
            data: parameter
          }
        }
      }
    }
  },

  {
    url: '/vue-admin-template/parameter/pv',
    type: 'get',
    response: _ => {
      return {
        code: 20000,
        data: {
          pvData: [
            { key: 'PC', pv: 1024 },
            { key: 'mobile', pv: 1024 },
            { key: 'ios', pv: 1024 },
            { key: 'android', pv: 1024 }
          ]
        }
      }
    }
  },

  {
    url: '/vue-admin-template/parameter/create',
    type: 'post',
    response: _ => {
      return {
        code: 20000,
        data: 'success'
      }
    }
  },

  {
    url: '/vue-admin-template/parameter/update',
    type: 'post',
    response: _ => {
      return {
        code: 20000,
        data: 'success'
      }
    }
  }
]

