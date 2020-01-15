<template>
  <div class='basic'>
    <el-row>
      <el-col :span='24'>
        <el-card>
          <div slot="header">
            <!-- 面包屑 -->
            <el-breadcrumb separator="/" style="margin-bottom: 10px">
              <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
              <el-breadcrumb-item>报警信息</el-breadcrumb-item>
            </el-breadcrumb>
            <el-button type="primary" class="add_button" size="mini" @click="add_server()">新增设备</el-button>
          </div>
          <div class="table-wrapper">
              <!-- v-loading="loading" -->
            <el-table
              element-loading-text="加载数据中"
              :data='tableData'
              border
              :row-class-name="addRowClass"
               fit="true">
              <el-table-column label="设备编号" prop="device_no" align="center" width="90"></el-table-column>
              <el-table-column label="报警内容" prop="alarm_context" align="center" width="90"></el-table-column>
              <el-table-column label="报警事件" prop="alarm_time" align="center" width="100"></el-table-column>
              <el-table-column label="人脸识别姓名" prop="face_recognition" align="center" width="100"></el-table-column>
              <el-table-column label="base64图片" prop="img_base64" align="center" width="90"></el-table-column>
              <el-table-column label="报警类型" prop="alarm_type" align="center" width="100"></el-table-column>
              <el-table-column label="报警级别" prop="alarm_level" align="center" width="100"></el-table-column>
              <el-table-column label="报警地址" prop="alarm_address" align="center" width="100"></el-table-column>
              <el-table-column label="图片名称" prop="img_name" align="center" width="100"></el-table-column>
              <el-table-column label="图片备注" prop="img_remark" align="center" width="100"></el-table-column>
              <el-table-column label="图片地址" prop="img_url" align="center" width="100"></el-table-column>
              <el-table-column label="视频url" prop="video_url" align="center" width="100"></el-table-column>
              <el-table-column label="事件关联项" prop="link_obj" align="center" width="110"></el-table-column>
             
              <el-table-column label="操作" align="center" header-align="center" fixed="right" width="250px">
                <template slot-scope="scope">
                  <el-button type="primary" size="mini" @click="view(scope.$index, scope.row)">查看</el-button>
                  <el-button type="primary" size="mini" @click="edit(scope.$index, scope.row)">编辑</el-button>
                  <el-button type="danger" size="mini" @click="del(scope.$index, scope.row)">删除</el-button>
                </template>
                
              </el-table-column>
             
            </el-table>
            <!-- 分页 pagination -->
            <el-pagination
              style="margin-top: 16px; text-align:right;"
              layout="total, sizes, prev, pager, next, jumper"
              :page-sizes="[5, 10, 15, 20]"
              :total="total"
              @size-change="handleSizeChange"
              @current-change="handleCurrentChange">
            </el-pagination>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>
<script>
  import {formatDate} from 'src/utils/utils';
  // import score from 'src/components/Score/index';

  const POSITIVE = 0;
  const NEGATIVE = 1;
  export default {
    created () {
      // this.getTableData();
    },
    data () {
      return {
        tableData: [],
        loading: true,
        // 默认分页条数
        pagesize: 10,
        currentpage: 1,
        total: 0,
        show_server: "",
        alarm_message: [
        ]
      }
    },
    methods: {
      // 添加
      add_server() {
        this.$router.push({
          path: '/add_alarm_message'
        })
        console.log('00000000000');
      },
      // 查看
      view(index, row) {
        console.log(row, '11111111111111111111111111')
          // 警报详细信息
         /*  this.show_alarm_messages = `
            报警内容：${ row.alarm_content }
            报警事件${ row.alarm_time }
            人脸识别姓名：${ row.face_recognition }
            base64图片：${ row.img_base64 }
            报警类型：${ row.alarm_type }
            报警级别：${ row.alarm_level }
            报警地址：${ row.alarm_address }
            图片名称：${ row.img_name }
            图片备注：${ row.img_remark }
            图片地址：${ row.img_url }
            视频url：${ row.video_url }
            事件关联项：${ row.link_obj }
          `; */

          this.show_alarm_messages = 
           `
            报警内容：${ row.alarm_content }
            报警事件${ row.alarm_time }
            人脸识别姓名：${ row.face_recognition }
            base64图片：${ row.img_base64 }
            报警类型：${ row.alarm_type }
            报警级别：${ row.alarm_level }
            报警地址：${ row.alarm_address }
            图片名称：${ row.img_name }
            图片备注：${ row.img_remark }
            图片地址：${ row.img_url }
            视频url：${ row.video_url }
            事件关联项：${ row.link_obj }
          `;
          this.$alert(this.show_alarm_messages, '设备详细信息', {
          confirmButtonText: '确定',
        });
      },
      // 编辑
      edit(index, row) {
        console.log(index, '22222222222222222222');
        this.$router.push({
          path: '/edit_alarm_message',
           query: {
            id: index,
            data: row
          }
        })
        .then(res => {})
        .catch(err => {})
      },
      // 删除
      del(index, row) {
        /* 调取删除接口， 传入unique_server_id   进行确定 */
        this.tableData.splice(index, 1);

        this.axios({
          // url: `getTableData?per_page=${this.pagesize}&cur_page=${this.currentpage}`,
          // method: "get",
         url: "",
         data: {
            // unique_server_id: 1
          }
        })
        .then(res => {
            this.loading = false;

          console.log(res, 'res  delete');
        })
        .catch(err => {
          console.log(err, 'errr   delete');
        })
        console.log('333333333333333333');
      },
      // getTableData () {
      //   this.axios.get(`getTableData?per_page=${this.pagesize}&cur_page=${this.currentpage}`)
      //   .then(data => {
      //     if (data.errno === 0) {
      //       this.tableData = data.data.table;
      //       this.total = data.data.total;
      //       this.loading = false;
      //     } else {
      //       console.log(data.msg);
      //     }
      //   })
      //   .catch(error => {
      //     console.log(error);
      //   });
      // },
      show (scope) {
        console.log(scope, 'scope');
      },
      handleSizeChange (value) {
        this.pagesize = value;
        // this.getTableData();
      },
      handleCurrentChange (value) {
        this.currentpage = value;
        // this.getTableData();
      },
      addRowClass ({row, rowIndex}) {
        if (row.rateType === NEGATIVE) {
          return 'warning-row';
        }
      }
    },
    filters: {
      rateTypeToText (rateType) {
        return rateType === POSITIVE ? '满意' : '不满意';
      },
      formatDate (time) {
        let date = new Date(time);
        return formatDate(date, 'yyyy-MM-dd hh:mm:ss');
      }
    },
    components: {
      // score
    }
  };
</script>
<style lang='scss'>
  .basic {
    .el-table {
      .warning-row {
        background-color: oldlace;
      }
    }

    .recommend-tag {
      display: inline-block;
      margin: 4px 0;
      margin-right: 4px;

      &:last-child {
        margin-right: 0;
      }
    }
  }
</style>
