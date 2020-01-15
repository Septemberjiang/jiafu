<template>
  <div class="bg">
    <el-breadcrumb separator="/">
      <el-breadcrumb-item :to="{ path: '/wel' }">首页</el-breadcrumb-item>
      <!-- <el-breadcrumb-item :to="{ path: '/wel' }">首页</el-breadcrumb-item> -->
      <el-breadcrumb-item>添加报警信息</el-breadcrumb-item>
    </el-breadcrumb>

    <el-form
      :model="camera_list"
      status-icon
      :rules="rules"
      ref="camera_list"
      label-width="auto"
      class="demo-devlist"
    >
      <el-form-item label="设备编号" prop="device_no">
        <el-input
          type="text"
          v-model="camera_list.device_no"
          autocomplete="off"
        ></el-input>
      </el-form-item>
      <el-form-item label="摄像头名称" prop="server_no">
        <el-input
          type="text"
          v-model="camera_list.camera_name"
          autocomplete="off"
        ></el-input>
      </el-form-item>
      <el-form-item label="摄像头ip" prop="camera_ip">
        <el-input
          type="text"
          v-model="camera_list.camera_ip"
          autocomplete="off"
        ></el-input>
      </el-form-item>
      <el-form-item label="安装位置" prop="camera_position">
        <el-input type="text" v-model="camera_list.camera_position"></el-input>
      </el-form-item>
      <el-form-item label="rtsp地址" prop="rtsp_address">
        <el-input type="text" v-model="camera_list.rtsp_address"></el-input>
      </el-form-item>
      <el-form-item label="识别阈值" prop="distinguish_wide">
        <el-input type="text" v-model="camera_list.distinguish_wide"></el-input>
      </el-form-item>
      <el-form-item label="检测间隔" prop="check_space">
        <el-input type="text" v-model="camera_list.check_space"></el-input>
      </el-form-item>
      <el-form-item label="场景识别度" prop="scene_at_degree">
        <el-input type="text" v-model="camera_list.scene_at_degree"></el-input>
      </el-form-item>
      <el-form-item label="移动检测阈值" prop="move_check_wide">
        <el-input type="text" v-model="camera_list.move_check_wide"></el-input>
      </el-form-item>
      <el-form-item label="设备是否启用" prop="equipment_state">
        <el-input type="text" v-model="camera_list.equipment_state"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm()">提交</el-button>
        <el-button @click="resetForm('camera_list')">重置</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
export default {
  data() {
   /*  //服务器名字
    var serverName = (rule, value, callback) => {
      if (!value) {
        return callback(new Error("设备名字不能为空"));
      } else {
        callback();
      }
    };
    // 设备编码
    var serverNo = (rule, value, callback) => {
      if (!value) {
        return callback(new Error("设备编码不能为空"));
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
    }; */

    return {
      camera_list: {
        // 设备编号
        device_no: "",
        // 摄像头名称
        camera_name: "",
        // 摄像头ip
        camera_ip: "",
        // 安装位置
        camera_position: "",
        // rtsp地址:
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
        equipment_state: "",
      },
      rules: {
       /*  // 设备名称
        server_name: [{ validator: serverName, trigger: "blur" }],
        // 设备编码
        server_no: [{ validator: serverNo, trigger: "blur" }],
        // 安装公司
        company: [{ validator: company, trigger: "blur" }],
        // 服务器是否开启
        server_state: [{ validator: serverState, trigger: "blur" }] */
      }
    };
  },
  methods: {
    submitForm() {
      this.$axios({
        url: "http://192.168.0.188:5000/api/device/camera",
        method: "post",
        data: {
          // 设备编号
          device_no: this.camera_list.server_name,
          // 摄像头名称
          camera_name: this.camera_list.server_no,
          // 摄像头ip
          camera_ip: this.camera_list.server_ip,
          // 摄像头安装位置
          camera_position: this.camera_list.province,
          // rtsp地址
          rtsp_address: this.camera_list.city,
          // 识别阈值equipment_state
          distinguish_wide: this.camera_list.county,
          // 检测间隔
          check_space: this.camera_list.company,
          // 场景识别度
          scene_at_degree: this.camera_list.scene_at_degree,
          // 移动检测阈值
          move_check_wide: this.camera_list.move_check_wide,
          // 设备是否启用
          equipment_state: this.camera_list.equipment_state,
          // 服务器的id
          // unique_server_id: this.camera_list.unique_server_id 
        }
      })
        .then(res => {
          console.log(res, "res111111111111111111111");
          if (res.code == 1) {
            this.$swal(res.data.info);
          } else {
            this.$router
              .push({
                path: "/tables/filter"
              })
              .then(res => {
                this.$swal("添加成功");
              })
              .catch(err => {});
          }
        })
        .catch(err => {
          console.log(err, "errrrrrrrrrrrr");
        });
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
  padding:-moz-submit-invalid 0 0 0 20px;
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
