/* eslint-disable */
'use strict'
require('eventsource-polyfill')
// 热加载
// var hotClient = require('webpack-hot-middleware/client?noInfo=true&reload=true')
var hotClient = require('webpack-hot-middleware/client?noInfo=true&reload=true')

hotClient.subscribe(function (event) {
  if (event.action === 'reload') {
    window.location.reload()
  }
})
