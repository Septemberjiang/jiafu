<template>
  <div class="wrap">
    <div class="login_box">
      <div class="login_title">
        <h1 class="title">登录</h1>
      </div>
      <div class="login_userinfo">
        <div class="username">
          <span>用户名：</span>
          <el-input v-model="username" placeholder="请输入用户名"></el-input>
        </div>
        <div class="password">
          <span>密码：</span>
          <el-input
            placeholder="请输入密码"
            v-model="password"
            show-password
          ></el-input>
        </div>
        <div class="login_btn">
          <el-row>
            <el-button type="primary" @click="login">登录</el-button>
          </el-row>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: ""
    };
  },
  methods: {
    login() {
      console.log("login");
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.wrap {
  width: 100%;
  height: 100%;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: #d9d9d9;
}
.login_box {
  width: 300px;
  height: 300px;
  background: #bfefff;
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  margin: auto;
}
.login_title .title {
  font-size: 30px;
  color: #333;
  text-align: center;
  border: 1px solid #f90;
  margin: 0;
  line-height: 2;
}
</style>
