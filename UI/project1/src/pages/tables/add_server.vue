<template>
  <div class="bg">
    <el-breadcrumb separator="/">
      <el-breadcrumb-item :to="{ path: '/wel' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>添加设备</el-breadcrumb-item>
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
        <el-button type="primary" @click="submitForm(formName)">提交</el-button>
        <el-button @click="resetForm('devlist')">重置</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
export default {
  data() {
  
    return {
      devlist: {
        // 设备名称：
        server_name: "",
        // 设备编码:
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
        // 设备名称：
        server_name: [
          { ruquired: true, message: "请输入设备名称", trigger: "blur"},
          { min: 1, max: 50, message: "长度不超多50个字符", trigger: "blur"}
        ],
        device_no: [
          { ruquired: true, message: "请输入设备编号", trigger: "blur"},
          { min: 1, max: 50, message: "长度不超多50个字符", trigger: "blur"}
        ]



        // // 设备名称
        // server_name: [{ validator: serverName, trigger: "blur" }],
        // // 设备编码
        // device_no: [{ validator: serverNo, trigger: "blur" }],
        // // 安装公司
        // // company: [{ validator: company, trigger: "blur" }],
        // // 服务器是否开启
        // server_state: [{ validator: serverState, trigger: "blur" }]
      }

      
    };
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate(valid => {
        if(valid) {
 this.$axios({
        url: "http://192.168.0.167:5000/api/device/server",
        method: "post",
        data: {
          server_name: this.devlist.server_name,
          device_no: this.devlist.device_no,
          server_ip: this.devlist.server_ip,
          province: this.devlist.province,
          city: this.devlist.city,
          county: this.devlist.county,
          company: this.devlist.company,
          server_state: this.devlist.server_state
        }
      })
        .then(res => {
          if (res.code == 1) {
            this.$swal(res.data.info);
          } else {
            this.$router
              .push({
                path: "/tables/basic"
              })
              .then(res => {
                this.$swal("添加成功");
              })
              .catch(err => {
                console.log(err, 'errrrrrrrrrrrrrrrrrrrrrrr');
                
              });
          }
        })
        .catch(err => {
          console.log(err, "errrrrrrrrrrrr");
        });
        }else {
          console.log('error submit');
          return false;
          
        }
      })
     
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    }
  }
};
</script>
<style lang="scss" scoped>
.bg {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  width: 100%;
  height: 100%;
  background: #fff;
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
