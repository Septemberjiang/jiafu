/**
 * Created by PanJiaChen on 16/11/18.
 */

/**
 * @param {string} path
 * @returns {Boolean}
 */
export function isExternal(path) {
  return /^(https?:|mailto:|tel:)/.test(path)
}

/**
 * @param {string} str
 * @returns {Boolean}
 */
/* export function validUsername(str) {
  const valid_map = ['admin', 'editor']
  return valid_map.indexOf(str.trim()) >= 0
}
 */
/**
 * 密码 password
 * 验证密码长度是否少于六位
 * @param {string} str 
 * @return {Boolean}
*/
export function validPassword(str){
  const valid_length = str.trim().length
  console.log(valid_length,'长度');
  return valid_length >= 6
}
