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
      <el-form-item label="摄像头名称" prop="camera_name">
        <el-input
          type="text"
          v-model="devlist.camera_name"
          autocomplete="off"
        ></el-input>
      </el-form-item>
     
      <el-form-item label="摄像头ip" prop="camera_ip">
        <el-input
          type="text"
          v-model="devlist.camera_ip"
          autocomplete="off"
        ></el-input>
      </el-form-item>
      <el-form-item label="安装位置" prop="camera_position">
        <el-input
          type="text"
          v-model="devlist.camera_position"
          autocomplete="off"
        ></el-input>
      </el-form-item>
      <el-form-item label="rtsp地址" prop="rtsp_address">
        <el-input
          type="text"
          v-model="devlist.rtsp_address"
          autocomplete="off"
        ></el-input>
      </el-form-item>
      <el-form-item label="识别阈值" prop="distinguish_wide">
        <el-input type="text" v-model="devlist.distinguish_wide"></el-input>
      </el-form-item>
      <el-form-item label="检测间隔" prop="check_space">
        <el-input type="text" v-model="devlist.check_space"></el-input>
      </el-form-item>
      <el-form-item label="场景识别度" prop="scene_at_degree">
        <el-input type="text" v-model="devlist.scene_at_degree"></el-input>
      </el-form-item>
      <el-form-item label="移动检测阈值" prop="move_check_wide">
        <el-input type="text" v-model="devlist.move_check_wide"></el-input>
      </el-form-item>
      <el-form-item label="设备是否启用" prop="equipment_state">
        <el-input type="text" v-model="devlist.equipment_state"></el-input>
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
        // 设备编号
        device_no: "",
        // 摄像头名称：
        camera_name: "",
        // 摄像头IP
        camera_ip: "",
        // 安装位置：
        camera_position: "",
        // rtsp地址
        rtsp_address: "",
        // 识别阈值
        distinguish_wide: "",
        // 检测间隔
        check_space: "",
        // 场景识别度
        scene_at_degree: "",
        // 移动检测阈值
        move_check_wide: "",
        // 设备是否启用
        equipment_state: ""
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
      console.log(this.$route.query, '1111111111111111');
      console.log(this.$route.query.id, 'iddddddddddddd');
      
      this.$axios({
        method: "put",
        url: "http://192.168.0.188:5000/api/device/server/operate/" + this.$route.query.id,
        data: {
          device_no: this.devlist.device_no,
          camera_name: this.devlist.camera_name,
          camera_ip: this.devlist.camera_ip,
          camera_position: this.devlist.camera_position,
          rtsp_address: this.devlist.rtsp_address,
          distinguish_wide: this.devlist.distinguish_wide,
          check_space: this.devlist.check_space,
          scene_at_degree: this.devlist.scene_at_degree,
          move_check_wide: this.devlist.move_check_wide,
          equipment_state: this.devlist.equipment_state,
        }
      })
        .then(res => {
          this.$router
            .push({
              path: "/tables/sort"
            })
            .then(res => {
              console.log(res, 'edit_camera   res');
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
    this.devlist.device_no = this.$route.query.data.device_no;
    this.devlist.camera_name = this.$route.query.data.camera_name;
    this.devlist.camera_ip = this.$route.query.data.camera_ip;
    this.devlist.camera_position = this.$route.query.data.camera_position;
    this.devlist.rtsp_address = this.$route.query.data.rtsp_address;
    this.devlist.distinguish_wide = this.$route.query.data.distinguish_wide;
    this.devlist.check_space = this.$route.query.data.check_space;
    this.devlist.scene_at_degree = this.$route.query.data.scene_at_degree;
    this.devlist.move_check_wide = this.$route.query.data.move_check_wide;
    this.devlist.equipment_state = this.$route.query.data.equipment_state;
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
