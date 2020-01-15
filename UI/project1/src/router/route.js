/**
 * @Project Name: vue-admin
 * @Author: luichooy
 * @Date: 2018-01-17 15:01
 * @Email: luichooy@163.com
 * @Idea: WebStorm
 */

import Layout from 'src/pages/layout/layout';

// 不作为main组件子页面展示的页面单独写，如下
export const loginRouter = {
  path: '/login',
  name: 'login',
  meta: {
    title: 'Login - 登录'
  },
  component: () => import('src/pages/login/login')
};

// 错误页面
export const errorRouter = {
  path: '/error/:code',
  name: 'error',
  meta: {
    title: 'error'
  },
  component: () =>
    import('src/pages/error/index')
};

// 作为main组件子页面展示  但不在左侧菜单显示的路由卸载otherRoter里
export const otherRouter = {
  path: '',
  name: 'otherRouter',
  redirect: '/home',
  meta: {
    requireAuth: true
  },
  component: Layout,
  children: [
    {
      path: 'home',
      name: 'home',
      title: '首页',
      component: () => import('src/pages/home/home')
    },
    // 新增设备信息
    {
      path: 'add_server',
      name: 'add_server',
      title: '新增设备信息',
      component: () => import('src/pages/tables/add_server')
    },
    // 编辑设备信息
    {
      path: 'edit_server',
      name: 'edit_server',
      title: '修改设备信息',
      component: () => import('src/pages/tables/edit_server')
    },
    // 新增摄像头
    {
      path: 'add_camera',
      name: 'add_camera',
      title: '新增摄像头信息',
      component: () => import('src/pages/tables/add_camera')
    },
    // 编辑摄像头信息
    {
      path: 'edit_camera',
      name: 'edit_camera',
      title: '修改摄像头信息',
      component: () => import('src/pages/tables/edit_camera')
    },
    // 新增报警信息
    {
      path: 'add_alarm_message',
      name: 'add_alarm_message',
      title: '新增报警信息',
      component: () => import('src/pages/tables/add_alarm_message')
    },
    // 编辑报警信息
    {
      path: 'edit_alarm_message',
      name: 'edit_alarm_message',
      title: '修改报警信息',
      component: () => import('src/pages/tables/edit_alarm_message')
    }
  ]
};

// 作为Main组件的子页面展示并且在左侧菜单显示的路由写在appRouter里
export const appRouter = [
  {
    path: '/tables',
    name: 'tables',
    title: '设备管理',
    meta: {
      requireAuth: true
    },
    component: Layout,
    children: [
      {
        path: 'basic',
        name: 'basic',
        title: '设备列表',
        component: () => import('src/pages/tables/basic')
      },
      {
        path: 'sort',
        name: 'sort',
        title: '摄像头列表',
        component: () => import('src/pages/tables/sort')
      },
      {
        path: 'filter',
        name: 'filter',
        title: '报警信息管理',
        component: () => import('src/pages/tables/filter')
      }
    ]
  },
  {
    path: '/charts',
    name: 'charts',
    title: 'echarts图表',
    meta: {
      requireAuth: true
    },
    component: Layout,
    children: [
      {
        path: 'bar',
        name: 'bar',
        title: '柱状图',
        component: () => import('src/pages/charts/bar')
      },
      {
        path: 'line',
        name: 'line',
        title: '折线图',
        component: () => import('src/pages/charts/line')
      },
      {
        path: 'pie',
        name: 'pie',
        title: '饼图',
        component: () => import('src/pages/charts/pie')
      }
    ]
  },
  {
    path: '/form',
    name: 'form',
    title: '表单管理',
    meta: {
      requireAuth: true
    },
    component: Layout,
    children: [
      {
        path: 'render',
        name: 'render',
        title: '渲染表单',
        component: () => import('src/pages/form/render/render')
      }
    ]
  },
  {
    path: '/system',
    name: 'system',
    title: '系统管理',
    meta: {
      requireAuth: true
    },
    component: Layout,
    children: [
      {
        path: 'index',
        name: 'system_index',
        title: '系统管理',
        component: () => import('src/pages/system/index/index')
      }
    ]
  },
  {
    path: '/user',
    name: 'user',
    title: '用户管理',
    meta: {
      requireAuth: true
    },
    component: Layout,
    children: [
      {
        path: 'index',
        name: 'user_index',
        title: '用户管理',
        component: () => import('src/pages/user/index')
      }
    ]
  },
  {
    path: '/access',
    name: 'access',
    title: '权限管理',
    meta: {
      requireAuth: true
    },
    component: Layout,
    children: [
      {
        path: 'index',
        name: 'access_index',
        title: '权限管理',
        component: () => import('src/pages/access/index')
      }
    ]
  },
  {
    path: '/log',
    name: 'log',
    title: '日志管理',
    meta: {
      requireAuth: true
    },
    component: Layout,
    children: [
      {
        path: 'index',
        name: 'log_index',
        title: '操作日志',
        component: () => import('src/pages/log/index')
      }
    ]
  },
  {
    path: '/test',
    name: 'test',
    title: '测试',
    meta: {
      requireAuth: true
    },
    component: Layout,
    children: [
      {
        path: 'index',
        name: 'test_index',
        title: '测试',
        component: () => import('src/pages/test/test')
      }
    ]
  }
];

export const routers = [
  loginRouter,
  errorRouter,
  otherRouter,
  ...appRouter
];
