<template>
  <div class="bg">
    <el-breadcrumb separator="/">
      <el-breadcrumb-item :to="{ path: '/wel' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>编辑设备</el-breadcrumb-item>
    </el-breadcrumb>
    <el-form
      :model="devlist"
      status-icon
      :rules="rules"
      ref="devlist"
      label-width="auto"
      class="demo-devlist"
    >
      <el-form-item label="设备编号" prop="device_no">
        <el-input
          type="text"
          v-model="devlist.device_no"
          autocomplete="off"
        ></el-input>
      </el-form-item>
      <el-form-item label="设备名称" prop="server_name">
        <el-input
          type="text"
          v-model="devlist.server_name"
          autocomplete="off"
        ></el-input>
      </el-form-item>
      <el-form-item label="设备ip" prop="server_ip">
        <el-input
          type="text"
          v-model="devlist.server_ip"
          autocomplete="off"
        ></el-input>
      </el-form-item>
      <el-form-item label="安装省份" prop="province">
        <el-input type="text" v-model="devlist.province"></el-input>
      </el-form-item>
      <el-form-item label="安装地市" prop="city">
        <el-input type="text" v-model="devlist.city"></el-input>
      </el-form-item>
      <el-form-item label="安装县区" prop="county">
        <el-input type="text" v-model="devlist.county"></el-input>
      </el-form-item>
      <el-form-item label="安装公司" prop="company">
        <el-input type="text" v-model="devlist.company"></el-input>
      </el-form-item>
      <el-form-item label="服务器是否开启" prop="server_state">
        <el-input type="text" v-model="devlist.server_state"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm()">修改</el-button>
        <el-button @click="resetForm('devlist')">重置</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
export default {
  data() {
    //服务器名字
    var serverName = (rule, value, callback) => {
      if (!value) {
        return callback(new Error("设备名字不能为空"));
      } else {
        callback();
      }
    };
    // 设备IP
    var serverIP = (rule, value, callback) => {
      if (!value) {
        return callback(new Error("设备IP不能为空"));
      } else {
        callback();
      }
    };
    // 安装公司
    var company = (rule, value, callback) => {
      if (!value) {
        return callback(new Error("安装公司不能为空"));
      } else {
        callback();
      }
    };
    // 服务器是否开启
    var serverState = (rule, value, callback) => {
      if (!value) {
        return callback(new Error("服务器是否开启不能为空"));
      } else {
        callback();
      }
    };

    return {
      devlist: {
        // 设备名称：
        server_name: "",
        // 设备编号
        device_no: "",
        // 设备IP
        server_ip: "",
        // 安装省份：
        province: "",
        // 安装地市：
        city: "",
        // 安装区县
        county: "",
        // 安装公司：
        company: "",
        // 服务器是否开否
        server_state: ""
      },
      rules: {
         // 设备名称
        server_name: [{ validator: serverName, trigger: "blur" }],
        // 设备ip
        server_ip: [{ validator: serverIP, trigger: "blur" }],
        // 安装公司
        company: [{ validator: company, trigger: "blur" }],
        // 服务器是否开启
        server_state: [{ validator: serverState, trigger: "blur" }]
        // id:
      }
    };
  },
  methods: {
    submitForm() {
      // console.log(this.$route.query, '1111111111111111');
      // console.log(this.$route.query.unique_server_id, 'iddddddddddddd');
      this.$axios({
        method: "put",
        url: "http://192.168.0.167:5000/api/device/server/operate/" + this.$route.query.unique_server_id,
        data: {
          device_no: this.devlist.device_no,
          server_name: this.devlist.server_name,
          server_ip: this.devlist.server_ip,
          province: this.devlist.province,
          city: this.devlist.city,
          county: this.devlist.county,
          company: this.devlist.company,
          server_state: this.devlist.server_state
        }
      })
        .then(res => {
          this.$router
            .push({
              path: "/tables/basic"
            })
            .then(res => {
              // console.log(res, 'edit_server   res');
            })
            .catch(err => {});
        })
        .catch(err => {
          console.log(err);
        });
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    }
  },
  mounted() {
    console.log(this.$route.query, 'this.$route.query' );
    this.devlist.server_name = this.$route.query.data.server_name;
    this.devlist.device_no = this.$route.query.data.device_no;
    this.devlist.server_ip = this.$route.query.data.server_ip;
    this.devlist.province = this.$route.query.data.province;
    this.devlist.city = this.$route.query.data.city;
    this.devlist.county = this.$route.query.data.county;
    this.devlist.company = this.$route.query.data.company;
    this.devlist.server_state = this.$route.query.data.server_state;
  }
};
</script>
<style lang="scss" scoped>
.bg {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  width: 100%;
  height: 100%;
  background-color: #fff;
}
.el-breadcrumb {
  height: 30px;
  line-height: 30px;
  padding: 0 0 0 20px;
  background: #fff;
  border-bottom: 1px solid #ddd;
}
.el-input {
  width: 70%;
}
.el-form-item {
    margin: 20px 0;
}
</style>
