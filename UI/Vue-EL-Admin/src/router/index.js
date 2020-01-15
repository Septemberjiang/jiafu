import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '@/layout'

/**
 * Note: sub-menu only appear when route children.length >= 1
 * Detail see: https://panjiachen.github.io/vue-element-admin-site/guide/essentials/router-and-nav.html
 *
 * hidden: true                   if set true, item will not show in the sidebar(default is false)
 * alwaysShow: true               if set true, will always show the root menu
 *                                if not set alwaysShow, when item has more than one children route,
 *                                it will becomes nested mode, otherwise not show the root menu
 * redirect: noRedirect           if set noRedirect will no redirect in the breadcrumb
 * name:'router-name'             the name is used by <keep-alive> (must set!!!)
 * meta : {
    roles: ['admin','editor']    control the page roles (you can set multiple roles)
    title: 'title'               the name show in sidebar and breadcrumb (recommend set)
    icon: 'svg-name'             the icon show in the sidebar
    breadcrumb: false            if set false, the item will hidden in breadcrumb(default is true)
    activeMenu: '/example/list'  if set path, the sidebar will highlight the path you set
  }
 */

/**
 * constantRoutes
 * a base page that does not have permission requirements
 * all roles can be accessed
 */
export const constantRoutes = [
  {
    path: '/login',
    component: () => import('@/views/login/index'),
    hidden: true
  },

  {
    path: '/',
    component: Layout,
    redirect: '/home',
    children: [{
      path: 'home',
      name: 'Home',
      component: () => import('@/views/home/index'),
      meta: { title: '首页', icon: 'dashboard' }
    }]
  },

  {
    path: '/devices',
    component: Layout,
    redirect: '/devices/server',
    name: 'Devices',
    meta: { title: '设备管理', icon: 'example' },
    children: [
      {
        path: 'server',
        name: 'Server',
        component: () => import('@/views/devices/server/index'),
        meta: { title: '服务器', icon: 'table' }
      },
      {
        path: 'camera',
        name: 'Camera',
        component: () => import('@/views/devices/camera/index'),
        meta: { title: '摄像头', icon: 'tree' }
      }
    ]
  },

  {
    path: '/messages',
    component: Layout,
    redirect: '/messages/alarm',
    name: 'Messages',
    meta: { title: '消息管理', icon: 'message' },
    children: [
      {
        path: 'alarm',
        name: 'Alarm',
        component: () => import('@/views/messages/alarm/index'),
        meta: { title: '告警事件', icon: 'table' }
      },
      {
        path: 'log',
        name: 'Log',
        component: () => import('@/views/messages/log/index'),
        meta: { title: '日志消息', icon: 'table' }
      }
    ]
  }
]

// 异步挂载的路由
// 动态需要根据权限加载的路由表
export const asyncRoutes = [
  {
    path: '/system',
    component: Layout,
    redirect: '/system/user',
    name: 'System',
    meta: { role: ['admin', 'super_editor'], title: '系统设置', icon: 'example' },
    children: [
      {
        path: 'user',
        name: 'User',
        component: () => import('@/views/system/user/index'),
        meta: { role: ['admin', 'super_editor'], title: '用户管理', icon: 'table' }
      },
      {
        path: 'role',
        name: 'Role',
        component: () => import('@/views/system/role/index'),
        meta: { role: ['admin', 'super_editor'], title: '角色管理', icon: 'tree' }
      },
      {
        path: 'parameter',
        name: 'Parameter',
        component: () => import('@/views/system/parameter/index'),
        meta: { role: ['admin', 'super_editor'], title: '参数管理', icon: 'tree' }
      }
    ]
  },

  // 404 page must be placed at the end !!!
  { path: '*', redirect: '/404', hidden: true }
]

const createRouter = () => new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRoutes
})

const router = createRouter()

// Detail see: https://github.com/vuejs/vue-router/issues/1234#issuecomment-357941465
export function resetRouter() {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher // reset router
}

export default router
