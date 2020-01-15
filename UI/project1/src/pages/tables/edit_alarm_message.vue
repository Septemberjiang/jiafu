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
     <el-form-item label="报警内容" prop="alarm_content">
        <el-input
          type="text"
          v-model="devlist.alarm_content"
          autocomplete="off"
        ></el-input>
      </el-form-item>
      <el-form-item label="报警时间" prop="alarm_time">
         <div class="block">
    <!-- <span class="demonstration">默认</span> -->
    <el-date-picker
      v-model="devlist.alarm_time"
      type="date"
      placeholder="选择日期">
    </el-date-picker>
  </div>
        <!-- <el-input
          type="text"
          v-model="devlist.alarm_time"
          autocomplete="off"
        ></el-input> -->
      </el-form-item>
     
      <el-form-item label="人脸识别姓名" prop="face_recognition">
        <el-input
          type="text"
          v-model="devlist.face_recognition"
          autocomplete="off"
        ></el-input>
      </el-form-item>
      <el-form-item label="base64图片" prop="img_base64">
        <el-input
          type="text"
          v-model="devlist.img_base64"
          autocomplete="off"
        ></el-input>
      </el-form-item>
      <el-form-item label="报警类型" prop="alarm_type">
        <el-input
          type="text"
          v-model="devlist.alarm_type"
          autocomplete="off"
        ></el-input>
      </el-form-item>
      <el-form-item label="报警级别" prop="alarm_level">
        <el-input type="text" v-model="devlist.alarm_level"></el-input>
      </el-form-item>
      <el-form-item label="报警地址" prop="alarm_address">
        <el-input type="text" v-model="devlist.alarm_address"></el-input>
      </el-form-item>
      <el-form-item label="图片名称" prop="img_name">
        <el-input type="text" v-model="devlist.img_name"></el-input>
      </el-form-item>
      <el-form-item label="图片备注" prop="img_remark">
        <el-input type="text" v-model="devlist.img_remark"></el-input>
      </el-form-item>
      <el-form-item label="图片地址" prop="img_url">
        <el-input type="text" v-model="devlist.img_url"></el-input>
      </el-form-item>
      <el-form-item label="视频url" prop="video_url">
        <el-input type="text" v-model="devlist.video_url"></el-input>
      </el-form-item>
      <el-form-item label="事件关联项" prop="link_obj">
        <el-input type="text" v-model="devlist.link_obj"></el-input>
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
        // 报警内容
        alarm_content: "",
        // 报警时间：
        alarm_time: "",
        // 人脸识别姓名：
        face_recognition: "",
        // base64图片
        img_base64: "",
        // 报警类型
        alarm_type: "",
        // 报警级别
        alarm_level: "",
        // 报警地址
        alarm_address: "",
        // 图片名称
        img_name: "",
        // 图片备注
        img_remark: "",
        // 图片地址
        img_url: "",
        // 视频url
        video_url: "",
        // 事件关联项
        link_obj: ""
      },
      rules: {
       /*   // 设备名称
        server_name: [{ validator: serverName, trigger: "blur" }],
        // 设备ip
        server_ip: [{ validator: serverIP, trigger: "blur" }],
        // 安装公司
        company: [{ validator: company, trigger: "blur" }],
        // 服务器是否开启
        server_state: [{ validator: serverState, trigger: "blur" }]
        // id: */
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
          alarm_content: this.devlist.alarm_content,
          alarm_time: this.devlist.alarm_time,
          face_recognition: this.devlist.face_recognition,
          img_base64: this.devlist.img_base64,
          alarm_type: this.devlist.alarm_type,
          alarm_level: this.devlist.alarm_level,
          alarm_address: this.devlist.alarm_address,
          img_name: this.devlist.img_name,
          img_remark: this.devlist.img_remark,
          img_url: this.devlist.img_url,
          video_url: this.devlist.video_url,
          link_obj: this.devlist.link_obj,
        }
      })
        .then(res => {
          console.log(res, 'time');
          
          // console.log(this.alarm_time, 'time');
          
          this.$router
            .push({
              path: "/tables/filter"
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
